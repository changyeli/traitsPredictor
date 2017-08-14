# Traits Predictor

## Brief Introduction

This is a simple Python personality predictor. Basically, it will cluster all users with Big Five test style, and try to group users by the same trait.

### Methods

- Unigram
- Multiple Layer Perceptron
- Support Vector Machines
- Bernoulli Naive Bayes
- K Nearest Neighbors

### Model Selection

For each trait, model with the highest 10-fold cross validation score will be selected.

- Openness: Bernoulli Naive Bayes, with correct rate 74%
- Conscientiousness: Bernoulli Naive Bayes, with correct rate 53%
- Extroversion: Bernoulli Naive Bayes with correct rate 56%
- Agreeableness: MLP with correct rate 52%
- Neuroticism: Bernoulli Naive Bayes, with correct rate 62%

### Features
- Predicting users' personality traits.
- Grouping people by users' personality trait

### Data

User selection is randomly selected from [here](http://friendorfollow.com/twitter/most-followers/), and the word feature data is collected from [here](https://github.com/mhbashari/NRC-Persian-Lexicon). For the training data, is collected from [here](http://mypersonality.org/wiki/doku.php?id=download_databases).



### Files
- ```fileProcess.py```: pulling data from twitter given some test usernames.
- ```tweetProcess.py```: data processing of raw data pulled from ```fileProcess.py```
- ```featureExtraction.py```: feature extraction and I/O to better format.
- ```featureBuild.py```: classifying users into clusters, using K-means, based on their tweets' feature.
- ```featureAna.R```: feature analysis.
- ```trainProcess.py```: training data process, using Machine Learning techniques. This training process is aimed to predict traits' category, i.e., predict if user is an openness person.
- ```trainBuild.py```: training data process, to get an average score for each trait. At this point, I'm lacking of an accurate method of predicting trait score based on unigram using multivariate linear regression. So currently the score is predicted based on the median of the trait score from training sample. Due to limited sample, the score prediction at this point may not be accurate, but it points to a direction for future development in some ways. Any ideas to improve is welcome!

## Citation
- Nasukawa, T., & Yi, J. (2003, October). Sentiment analysis: Capturing favorability using natural language processing. In Proceedings of the 2nd international conference on Knowledge capture (pp. 70-77). ACM.
- Yang, H., & Li, Y. (2013). Identifying user needs from social media. IBM Research Division, San Jose, 11.
- Gou, L., Zhou, M. X., & Yang, H. (2014, April). KnowMe and ShareMe: understanding automatically discovered personality traits from social media and user sharing preferences. In Proceedings of the 32nd annual ACM conference on Human factors in computing systems (pp. 955-964). ACM.
- Vinciarelli, A., & Mohammadi, G. (2014). A survey of personality computing. IEEE Transactions on Affective Computing, 5(3), 273-291.
- Mohammad, S., Zhu, X., Martin, J.: Semantic role labeling of emotions in tweets. In: Proceedings of the WASSA, pp. 32–41 (2014)
- Farnadi, G., Sitaraman, G., Sushmita, S., Celli, F., Kosinski, M., Stillwell, D., ... & De Cock, M. (2016). Computational personality recognition in social media. User modeling and user-adapted interaction, 26(2-3), 109-142.
- Celli, F., Pianesi, F., Stillwell, D., & Kosinski, M. (2013, June). Workshop on computational personality recognition (shared task). In Proceedings of the Workshop on Computational Personality Recognition.

