import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import entropy
from scipy import stats
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor

class ActiveLearner(object):
    def __init__(self, base_learner, dtype = 'discrete'):
        """
        Base class for active learning model

        Parameters
        ----------
        base_learner: sklearn.BaseEstimator
            Model that implements a `fit` and `predict` method like the sklearn API
        dtype: str
            Type of the input data. Assumed continuous if `dtype != 'discrete'`

        """
        self.base_learner = base_learner
        self.ensemble = []
        self.dtype = dtype
    
    def fit(self, X, y):
        raise NotImplementedError("This is the base class for Active Learning and as such does not implement a fit method")
    
    def predict(self, X, models = None):
        """
        Using the ensemble, make predictions

        Parameters
        ----------
        X: np.array
            Data in the form (n_samples, m_features)
        models: list
            If not operating on self, a list of models
        
        
        Returns
        -------
        preds: np.array
            (n_samples, 1) numpy array of the model predictions
            
        """
        preds_mat = []
        if models is None:
            models = self.ensemble
        if len(models) == 1:
            return models[0].predict(X)
        for model in models:
            preds_model = model.predict(X)
            preds_mat.append(preds_model)
            
        preds_mat = np.array(preds_mat)
        if self.dtype == 'discrete':
            return stats.mode(preds_mat)[0].squeeze()
        else:
            return np.mean(preds_mat, axis = 0)
    
    def disagreement(self, votes):
        """
        Entropy based disagreement function

        Parameters
        ----------
        votes: np.array
            The predictions of individual models
            
        Returns
        -------
        disagree: numeric
            The disagreement of the models based on Shannon's entropy
            

        """
        value,counts = np.unique(votes, return_counts=True)
        return entropy(counts, base=2)
    
    def mean_disagreement(self, votes):
        """
        Mean based disagreement function

        Parameters
        ----------
        votes: np.array
            The predictions of individual models
            
        Returns
        -------
        disagree: numeric
            The disagreement of the models based on absolute difference from the mean

        """
        
        return np.max(np.abs(np.mean(votes)-votes))
    
    def select_sample(self, potential_to_query, corpus):
        max_dis = 0
        max_dis_sample = potential_to_query[0]
        for sample in potential_to_query:
            votes = []
            for model in self.ensemble:
                vote = model.predict(sample[:-1].reshape(1,-1))
                votes.append(vote[0])
            if self.dtype == 'discrete':
                dis = self.disagreement(votes)
            else:
                dis = self.mean_disagreement(votes)
            if dis > max_dis:
                max_dis = dis
                max_dis_sample = sample

        corpus = np.vstack([corpus, max_dis_sample])
        return corpus
    
class QBag(ActiveLearner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def fit(self, X, y, allowed_samples = 10, num_models = 5,  **kwargs):
        """
        Fits QBag from Abe and Mamitsuka (1998)

        Parameters
        ----------
        X,y : numpy array
            The data matrices
        allowed_samples : int, optional
            The number of samples the learner is allowed to query The default is 10.
        num_models : int, optional
            The number of models to train in the committee. The default is 5.
        kwargs: dict
            Additional keyword arguements to be passed to the base learner.

        """
        data = np.hstack((X, y[:, np.newaxis]))
        corpus = data[:1]
        query_points = data[1:]
        
        for i in range(1,allowed_samples):
            self.ensemble = []
            for j in range(num_models):
                bag = corpus[np.random.randint(corpus.shape[0], size=i), :]
                y_train = bag[:,-1]
                X_train = np.delete(bag, -1, axis = 1)
                model = self.base_learner(**kwargs)
                model.fit(X_train,y_train)
                self.ensemble.append(model)

            potential_to_query = query_points[np.random.randint(query_points.shape[0],
                                                                size=allowed_samples), :]
            corpus = self.select_sample(potential_to_query, corpus)
            
            
class QBoost(ActiveLearner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def fit(self,X, y, allowed_samples = 10, num_models = 5, **kwargs):
        """
        Fits QBoost

        Parameters
        ----------
        X,y : numpy array
            The data matrices
        allowed_samples : int, optional
            The number of samples the learner is allowed to query The default is 10.
        num_models : int, optional
            The number of models to train in the committee. The default is 5.
        kwargs: dict
            Additional keyword arguements to be passed to the base learner.

        """
        data = np.hstack((X, y[:, np.newaxis]))
        corpus = data[:1]
        query_points = data[1:]

        for i in range(1,allowed_samples):
            self.ensemble = []
            for j in range(num_models):
                bag = corpus[np.random.randint(corpus.shape[0], size=i), :]
                y_train = bag[:,-1]
                X_train = np.delete(bag, -1, axis = 1)
                model = self.base_learner(**kwargs)
                if self.dtype == 'discrete':
                    clf = AdaBoostClassifier(base_estimator = model, n_estimators=num_models, random_state=0)
                else:
                    clf = AdaBoostRegressor(base_estimator = model, n_estimators=num_models, random_state=0)
                clf.fit(X_train, y_train)
                self.ensemble.append(clf)

            potential_to_query = query_points[np.random.randint(query_points.shape[0],
                                                                size=allowed_samples), :] # TODO what should the query size be?
            corpus = self.select_sample(potential_to_query, corpus)
            
            
class ACTIVE_DECORATE(ActiveLearner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def fit(self, X, y, allowed_samples = 100, num_models = 5,begin_labels = 10, **kwargs):
        """
        Fits ACTIVE_DECORATE

        Parameters
        ----------
        X,y : numpy array
            The data matrices
        allowed_samples : int, optional
            The number of samples the learner is allowed to query The default is 10.
        num_models : int, optional
            The number of models to train in the committee. The default is 5.
        begin_labels: int
            Number of samples to start with. 
        kwargs: dict
            Additional keyword arguements to be passed to the base learner.

        """
        data = np.hstack((X, y[:, np.newaxis]))
        corpus = data[:begin_labels]
        query_points = data[begin_labels:]

        for i in range(1,allowed_samples):
            models = self.DECORATE(corpus)
            potential_to_query = query_points[np.random.randint(query_points.shape[0],
                                                                size=allowed_samples), :] 
            corpus = self.select_sample(potential_to_query, corpus)
            self.ensemble = models
    
    def gen_artficial(self, shape, low, high, mean = 0.0):
        if self.dtype == 'discrete':
            # TODO add a method to infer high and low in the discrete case
            return np.random.randint(low, high, size = shape) # they use laplace smoothing. I used a uniform for conveinance
        else:
            return np.random.normal(mean,size = shape) # TODO: make each column a seperate Gaussian 

    def get_desired_shape(self, example, len_data, R_size):
        return (int(len_data* R_size), example.shape[0])
    
    def DECORATE(self, T, C_size = 5, I_max = 10, R_size = 0.3, **kwargs):
        i = 1
        trials = 1
        y_train = T[:,-1]
        X_train = np.delete(T, -1, axis = 1)
        C_1 = self.base_learner(**kwargs)
        C_1.fit(X_train,y_train)
        C = [C_1]
        
        eps = self.ensemble_error(C, X_train, y_train)
        
        while i < C_size and trials < I_max:
            y_train = T[:,-1]
            X_train = np.delete(T, -1, axis = 1)
            R = None
            last_R = R
            R = self.gen_artficial(self.get_desired_shape(X_train[0], len(X_train), R_size),
                                 np.min(X_train),np.max(X_train), mean = np.mean(X_train)) 

            # this may not be exactly what they described, but I think it makes the most sense
            # in the binary classification context
            labels = []
            for sample in R:
                if self.dtype == 'discrete':
                    I = lambda xt: 0.0 if xt == 1 else 1.0
                    fp = I(pred)
                    
                labels.append(fp)

            T_old = T
            labels = np.array(labels)
            arr_new = np.append(R,labels.reshape(-1,1), axis = 1)
            T_new = np.append(T,arr_new, axis = 0)

            C_prime = self.base_learner(**kwargs)
            
            y_train_C = T_new[:,-1]
            X_train_C = np.delete(T_new, -1, axis = 1)

            C_prime.fit(X_train_C,y_train_C)

            C_prime_preds = C_prime.predict(X_train)

            C_prime_acc = self.ensemble_error([C_prime],T_old[:, :-1],y_train)

            C.append(C_prime)

            T = T_old
            y_train = T[:,-1]
            eps_prime = self.ensemble_error(C, T[:, :-1],y_train)
            
            if eps_prime > eps:
                i+=1
                eps = eps_prime
            else:
                C.pop()
            trials +=1
        return C
    
    def predict_dec(sample,):
        num_models = len(decorate)
        p_0 = 0
        p_1 = 0
        for model in self.ensemble:
            if self.dtype == 'discrete':
                probas = model.predict_proba(sample.reshape(1,-1))[0]
                p_0 += probas[0]
                p_1 += probas[1]
            else:
                probas = model.predict_proba(sample.reshape(1,-1))[0]
                if probas[0] == 1:
                    p_1 +=1
                else:
                    p_0 += 0 
        p_0 /= num_models
        p_1 /= num_models # generalize for n variables
        argmax = lambda x1,x2: 0 if x1 > x2 else 1
        return argmax(p_0,p_1)
             
    def ensemble_error(self,C, T, y):
        preds = self.predict(T, models = C)
        I = lambda xt,yt: 1 if xt == yt else 0
        summ = 0
        for pred,true in zip(preds,y):
            summ+=I(pred,true)
        return summ/len(y)
    
    def predict_dec_all(self, samples):
        preds = []
        for sample in samples:
            pred = predict_dec(sample)
            preds.append(pred)
        return np.array(preds)
    
    
class jackAL(ActiveLearner):
    
    def __init__(self, *args, k = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self.k = k
    def fit(self, X,y, schedule = None, allowed_samples = 100, num_models = 5, k = 1):
        """
        Fits jackAL, an original AL method based on the jackknife

        Parameters
        ----------
        X,y : numpy array
            The data matrices
        k: int
            Number of items in each bag, default 1 for original jackknife
        schedule: function
            The annealing schedule for `k`
        allowed_samples : int, optional
            The number of samples the learner is allowed to query The default is 10.
        num_models : int, optional
            The number of models to train in the committee. The default is 5.

        """
        data = np.hstack((X, y[:, np.newaxis]))
        corpus = data[:2]
        query_points = data[2:]
        for i in range(1,allowed_samples):
            if k is None or k == 1:
                self._jackknife(corpus)
            elif k is not None or schedule is not None:
                self._jackknife_k(corpus, k = k, schedule = schedule)
            else:
                raise Exception("invalid args")
            potential_to_query = query_points[np.random.randint(query_points.shape[0],
                                                                size=allowed_samples), :]
            corpus = self.select_sample(potential_to_query, corpus)
    
    def _jackknife(self,data):
        n_models = len(data)
        for i in range(n_models):
            sample = data
            sample = np.delete(sample,i, axis = 0)
            model = self.base_learner()
            y_train = data[:,-1]
            X_train = np.delete(data, -1, axis = 1)
            model.fit(X_train,y_train)
            self.ensemble.append(model)
            
    def _jackknife_k(self, data, k = 1, schedule = None, n_models = 5):
        if schedule is None:
            n_models = len(data)//k
        i = 0
        while i < n_models:
            if schedule is None:
                bag = data[np.random.randint(data.shape[0], size=len(data) - k), :]
            else:
                bag = data[np.random.randint(data.shape[0], size=len(data) - int(schedule(len(data)))), :] 
            model = self.base_learner()
            y_train = bag[:,-1]
            X_train = np.delete(bag, -1, axis = 1)
            model.fit(X_train,y_train)
            self.ensemble.append(model)
            i+=1
  
            

