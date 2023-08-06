# qbc: a Python package for Query-by-Committee Active Learning
QBC Active Learning is a method used to increase sample efficency in situations where there is a low quantity of data. This implementation provides an automated pipeline to train a model ensemble using QBC active learning with arbitrary base learners.

Three methods from the literature (`QBag`, `QBoost`, `ACTIVE-DECORATE`), as well as one original approach (`jackAL`) based on the jackknife are implemented currently. Modifications and extensions to the articles are proposed and explained in the accompanying paper. 

![performance on the breast cancer dataset](cancer.PNG)

# Abstract: 

The field of active learning has many different approaches. 
This work focuses on the Query-by-Committee (QbC) framework, which uses ensembling methods to find the best sample to query for a label. 
Three methods from the literature are reviewed and implemented: QBag, QBoost, and ACTIVE-DECORATE. 
QBag, which is based on the bagging resampling method, has the advantage of simplicity, but QBoost (based on AdaBoost) often gives a larger performance increase. 
ACTIVE-DECORATE uses synthetic data to augment a sample of the training set. 
Once an ensemble of classifiers is trained on the current corpus, the algorithm then queries for the next labeled sample by finding  the maximum “disagreement” of the models. 
This is done via a variety of methods, including entropy and absolute divergence from the mean. Overall, the QbC method allows comparable or greater accuracy to a classifier trained on the whole dataset, but with a vastly reduced number of required samples. 
This work summarizes multiple approaches in the literature to QbC via bagging and boosting, and additionally proposes a new QbC framework called jackAL based on the jackknife; this method offers an advantage over the others because it allows the model to maximize small quantities of data, which is often the case when active learning is required. 
A variation on the jackknife, jackknife-k is explored as well.
Additionally, all code is implemented in Python and made available as open-source software on GitHub.

# Author
[Benjamin Pierce](mailto:bgpierc@sandia.gov)

# Sources
1. M. H. Quenouille, “Problems in Plane Sampling,” The Annals of Mathematical Statistics, vol. 20, no. 3, pp. 355–375, Sep. 1949, publisher: Institute of Mathematical Statistics. [Online]. Available: https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-20/issue-3/Problems-in-Plane-Sampling/10.1214/aoms/1177729989.full

2. L. Breiman, “Bagging Predictors,” Machine Learning, vol. 24, no. 2, pp. 123–140, Aug. 1996. [Online](https://doi.org/10.1023/A:1018054314350)

3. R. E. Schapire, “The strength of weak learnability,” Machine Learning, vol. 5, no. 2, pp. 197–227, Jun. 1990. [Online](https://doi.org/10.1007/BF00116037)

4. S. Argamon-Engelson and I. Dagan, “Committee-Based Sample Selection for Probabilistic Classifiers,” Journal of Artificial Intelligence Research, vol. 11, pp. 335–360, Nov. 1999, arXiv:1106.0220 [Online(http://arxiv.org/abs/1106.0220)

5. B. Settles, “Active Learning Literature Survey,” University of Wisconsin-Madison Department of Computer Sciences, Technical Report, 2009, accepted: 2012-03-15T17:23:56Z. [Online](https://minds.wisconsin.edu/handle/1793/60660)

6. N. Abe and H. Mamitsuka, “Query Learning Strategies Using Boosting and Bagging.” Madison, Wisconsin, USA, Jan. 1998, pp. 1–9.

7. R. L. Milidi ́u, D. Schwabe, and E. Motta, “Active Learning with Bagging for NLP Tasks,” in Advances in Computer Science, Engineering & Applications. Springer, 2012, pp. 141–147.

8. C. K ̈orner and S. Wrobel, “Multi-class Ensemble-Based Active Learning,” in Machine Learning: ECML 2006, ser. Lecture Notes in Computer Science. Springer, 2006, pp. 687–694. 

9. P. Melville and R. J. Mooney, “Creating diversity in ensembles using artificial data,” Information Fusion, vol. 6, no. 1, pp. 99–111, Mar. 2005. [Online](https://www.sciencedirect.com/science/article/pii/S156625350400034X)


10. ——, “Diverse ensembles for active learning,” in Proceedings of the twenty-first international conference on Machine learning, ser. ICML ’04, New York, NY, USA, Jul. 2004, p. 74. [Online](https://doi.org/10.1145/1015330.1015385)


11. C. F. J. Wu, “Jackknife, Bootstrap and Other Resampling Methods in Regression Analysis,” The Annals of Statistics, vol. 14, no. 4, pp. 1261–1295, Dec. 1986, publisher: Institute of Mathematical Statistics. [Online](https://projecteuclid.org/journals/annals-of-statistics/volume-14/issue 4/Jackknife-Bootstrap-and-Other-Resampling-Methods-in-Regression-Analysis/10.1214/aos/1176350142.full)


# License
MIT, see `LICENSE` for a copy of the license, or [avalible online](https://www.mit.edu/~amini/LICENSE.md)