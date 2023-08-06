from qbc.learners import QBag, QBoost, ACTIVE_DECORATE, jackAL
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.naive_bayes import GaussianNB,MultinomialNB
from sklearn.metrics import mean_squared_error, accuracy_score


def test_models(X, y, max_samples = 20, step = 1, model = MultinomialNB, dtype = 'discrete'):
    """
    Test models over a range of maximum allowed samples
    
    Parameters
    ----------
    x, y: np.array
        Data matrix
    max_samples: int
        Number of samples to loop through
    step: int
        At each iteration add this many samples to be queried
    model: sklearn.BaseEstimator
        Model that implements a `fit` and `predict` method like the sklearn API
    dtype: str
        Type of the input data. Assumed continuous if `dtype != 'discrete'`
        
    Returns
    -------
    accs: np.array
        Array of the values for either accuracy or MSE at each step
    samples_arr: np.array
        Range of steps that was looped over. Useful for x-axis on a graph
    
    """
    
    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

    qbag = QBag(model, dtype = dtype)
    qboost = QBoost(model, dtype = dtype)
    if dtype == 'discrete':
        acdec = ACTIVE_DECORATE(model, dtype = dtype)
    jackal = jackAL(model, k = 1, dtype = dtype)
    if dtype == 'discrete':
        models = [qbag, qboost, acdec, jackal]
    else:
        models = [qbag, qboost, jackal]

    accs = []
    samples_arr = np.arange(2, max_samples, step)
    for i in tqdm(samples_arr):
        model_acc = []
        for model in models:
            model.fit(X_train,y_train, allowed_samples = i)
            preds = model.predict(X_test)
            if dtype == 'discrete':
                acc_score = accuracy_score(y_test, preds)
            else:
                acc_score = mean_squared_error(y_test, preds)
            model_acc.append(acc_score)
        accs.append(model_acc)
    return np.array(accs), samples_arr

def plot_models(accs, samples_arr, dataset_name='Example', dtype = 'discrete'):
    """
    Test models over a range of maximum allowed samples
    
    Parameters
    ----------
    accs: np.array
        Array of the values for either accuracy or MSE at each step
    samples_arr: np.array
        Range of steps that was looped over. Useful for x-axis on a graph
    dataset_name: str
        Name of the dataset
    dtype: str
        Type of the input data. Assumed continuous if `dtype != 'discrete'`
    
    """

    if dtype == 'discrete':
        model_names = ['QBag', 'QBoost', "ACTIVE_DECORATE", 'jackAL']
    else:
        model_names = ['QBag', 'QBoost', 'jackAL']

    for i, name in enumerate(model_names):
        plt.plot(samples_arr, accs[:, i], label = name)
    plt.legend()
    if dtype == 'discrete':
        metric = 'Accuracy'
    else:
        metric = 'MSE'
    plt.title(f"{metric} vs number of samples\n{dataset_name} Dataset")
    plt.xlabel("Number of samples")
    plt.ylabel(f"{metric}")