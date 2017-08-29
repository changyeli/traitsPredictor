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

- Lasso regression
- SGD regression
- KNN regression
- Gradient Boosting regression

## Model Selection

For each trait:
- Classification: model with the highest 5-fold cross validation f1 score will be selected.
- Regression: model with the lowest MSE will be selected.


## Data

Validation user selection is randomly selected from [here](http://friendorfollow.com/twitter/most-followers/), and the word feature data is collected from [here](https://github.com/mhbashari/NRC-Persian-Lexicon). For the training data, is collected from [here](http://mypersonality.org/wiki/doku.php?id=download_databases).



## Files
- ```fileProcess.py```: pulling data from twitter given some test usernames.
- ```tweetProcess.py```: data processing of raw data pulled from ```fileProcess.py```
- ```featureExtraction.py```: feature extraction and I/O to better format.
- ```trainProcess.py```: training data process.
	- Using Machine Learning techniques. This training process is aimed to predict traits' category, i.e., predict if user is an openness person.
	- Using regression method to get score predictions for each trait.
- ```trainProcess_1.R```: data subsetting using R.
- ```trainBuild.py```: training data pre-process and associated I/O.
- ```modelRun.py```: model application on validation dataset.

## Limitations and Futher Direction

1. In first version, only plain text that can be found in NRC word list is considered as training sample. For futher development, emoticon can be treated as an important feature. For example, XD, :D, ( ͡° ͜ʖ ͡°), (´･ω･`),（　ﾟ Дﾟ）, 😆, 🙄, can help us to understand the emotion behind the tweet greatly. However, some emoticons can be misleading, for example, this one → 🙂. *Update*: Found [this](https://github.com/wooorm/emoji-emotion) repo on GitHub, listing the polarity on some emoji.
2. Also for V1, the final score for each trait is calculated using weighted mean; a better evaluation method should be implemented in further development. 
3. Initially, a star graph, such as player attributes in NBA 2K and FIFA 17 ([like this one](https://cdn.pbrd.co/images/1mCEPr5r.png)), is the final output for this project. However I didn't find a suitable tool to visualize the final score. [d3.js](https://github.com/d3/d3) can be one of the solutions, but it's new to me; needs to take some time to learn it.


## Citation
- Nasukawa, T., & Yi, J. (2003, October). Sentiment analysis: Capturing favorability using natural language processing. In Proceedings of the 2nd international conference on Knowledge capture (pp. 70-77). ACM.
- Yang, H., & Li, Y. (2013). Identifying user needs from social media. IBM Research Division, San Jose, 11.
- Gou, L., Zhou, M. X., & Yang, H. (2014, April). KnowMe and ShareMe: understanding automatically discovered personality traits from social media and user sharing preferences. In Proceedings of the 32nd annual ACM conference on Human factors in computing systems (pp. 955-964). ACM.
- Vinciarelli, A., & Mohammadi, G. (2014). A survey of personality computing. IEEE Transactions on Affective Computing, 5(3), 273-291.
- Mohammad, S., Zhu, X., Martin, J.: Semantic role labeling of emotions in tweets. In: Proceedings of the WASSA, pp. 32–41 (2014)
- Farnadi, G., Sitaraman, G., Sushmita, S., Celli, F., Kosinski, M., Stillwell, D., ... & De Cock, M. (2016). Computational personality recognition in social media. User modeling and user-adapted interaction, 26(2-3), 109-142.
- Celli, F., Pianesi, F., Stillwell, D., & Kosinski, M. (2013, June). Workshop on computational personality recognition (shared task). In Proceedings of the Workshop on Computational Personality Recognition.
- Banerjee, N., Chakraborty, D., Dasgupta, K., Joshi, A., Madan, S., Mittal, S., ... & Rai, A. (2009). Contextual analysis of user interests in social media sites-An exploration with micro-blogs. IBM Research Report-RI 09012.

