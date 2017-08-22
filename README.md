# Traits Predictor

## Brief Introduction

This is a simple Python personality predictor. Basically, it will cluster users using Big Five test style classification, and try to group users by the same trait to assign trait scores.

## Features
- Predicting users' personality traits.
- Grouping people by users' personality trait

## Methods

### Data Pre-processing

- Unigram
- Word frequency

### Classification

- Stochastic Gradient Descent
- Random Forest
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Gradient Boost

### Regression

- Ridge regression
- Lasso regression
- SGD regression
- Random Forest regression
- KNN regression
- Gradient Boosting regression
- Decision Tree regression

## Model Selection

For each trait:
- Classification: model with the highest 10-fold cross validation f1 score will be selected.
- Regression: model with the lowest MSE and MAE will be selected.
- Grouping: taking median as score, if the absolute difference between mean and median is less than 0.1. Median will be assigned to classified test and validation data.


## Data

Validation user selection is randomly selected from [here](http://friendorfollow.com/twitter/most-followers/), and the word feature data is collected from [here](https://github.com/mhbashari/NRC-Persian-Lexicon). For the training data, is collected from [here](http://mypersonality.org/wiki/doku.php?id=download_databases).



## Files
- ```fileProcess.py```: pulling data from twitter given some test usernames.
- ```tweetProcess.py```: data processing of raw data pulled from ```fileProcess.py```
- ```featureExtraction.py```: feature extraction and I/O to better format.
- ```featureBuild.py```: classifying users into clusters, using K-means, based on their tweets' feature. // no longer active.
- ```trainProcess.py```: training data process.
	- Using Machine Learning techniques. This training process is aimed to predict traits' category, i.e., predict if user is an openness person.
	- Using regression method to get score predictions for each trait.
	- Grouping scores from same labeled trait in training dataset. 
- ```trainBuild.py```: training data pre-process and associated I/O.
- ```modelRun.py```: model application on validation dataset.

## Citation
- Nasukawa, T., & Yi, J. (2003, October). Sentiment analysis: Capturing favorability using natural language processing. In Proceedings of the 2nd international conference on Knowledge capture (pp. 70-77). ACM.
- Yang, H., & Li, Y. (2013). Identifying user needs from social media. IBM Research Division, San Jose, 11.
- Gou, L., Zhou, M. X., & Yang, H. (2014, April). KnowMe and ShareMe: understanding automatically discovered personality traits from social media and user sharing preferences. In Proceedings of the 32nd annual ACM conference on Human factors in computing systems (pp. 955-964). ACM.
- Vinciarelli, A., & Mohammadi, G. (2014). A survey of personality computing. IEEE Transactions on Affective Computing, 5(3), 273-291.
- Mohammad, S., Zhu, X., Martin, J.: Semantic role labeling of emotions in tweets. In: Proceedings of the WASSA, pp. 32–41 (2014)
- Farnadi, G., Sitaraman, G., Sushmita, S., Celli, F., Kosinski, M., Stillwell, D., ... & De Cock, M. (2016). Computational personality recognition in social media. User modeling and user-adapted interaction, 26(2-3), 109-142.
- Celli, F., Pianesi, F., Stillwell, D., & Kosinski, M. (2013, June). Workshop on computational personality recognition (shared task). In Proceedings of the Workshop on Computational Personality Recognition.

