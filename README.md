# Traits Predictor

## Brief Introduction

This is a simple Python personality predictor. Basically, it will cluster all users with Big Five test style, and try to group users by the same trait.

### Methods

In this project, k-means and unigram are mainly used. 

### Features
- Predicting users' personality traits.
- Grouping people by users' personality trait

### Data

User selection is randomly selected from [here](http://friendorfollow.com/twitter/most-followers/), and the word feature data is collected from [here](https://github.com/mhbashari/NRC-Persian-Lexicon).

### Limitation

Since only raw data (users' tweets) is analyzed, and there is no valid Big Five test results for these users, so it's impossible to get label data and quantized score for each trait. Therefore, the only feasible solution is k-means and there is no way to evaluate the performance, except PCA. However, PCA dimension reduction will lose certain amount of information, so human-interpretation would have to take some loss, which may decrease the accuracy of evaluation.

Also, at this time, this predictor cannot give an accurate description of each trait for every user due to reasons metioned above. So, this preditor can only report like "user A is more positive than user B, since user A used more postive words, such as xxx, xxx, xxx, than user B". 

Any ideas of improvement are welcome!

### Files
- ```fileProcess.py```: pulling data from twitter given some test usernames.
- ```tweetProcess.py```: data processing of raw data pulled from ```fileProcess.py```
- ```featureExtraction.py```: feature extraction and I/O to better format.
- ```featureBuild.py```: classifying users into clusters, using K-means, based on their tweets' feature.

## Citation
- Nasukawa, T., & Yi, J. (2003, October). Sentiment analysis: Capturing favorability using natural language processing. In Proceedings of the 2nd international conference on Knowledge capture (pp. 70-77). ACM.
- Yang, H., & Li, Y. (2013). Identifying user needs from social media. IBM Research Division, San Jose, 11.
- Gou, L., Zhou, M. X., & Yang, H. (2014, April). KnowMe and ShareMe: understanding automatically discovered personality traits from social media and user sharing preferences. In Proceedings of the 32nd annual ACM conference on Human factors in computing systems (pp. 955-964). ACM.
- Vinciarelli, A., & Mohammadi, G. (2014). A survey of personality computing. IEEE Transactions on Affective Computing, 5(3), 273-291.
- Mohammad, S., Zhu, X., Martin, J.: Semantic role labeling of emotions in tweets. In: Proceedings of the WASSA, pp. 32–41 (2014)
- Farnadi, G., Sitaraman, G., Sushmita, S., Celli, F., Kosinski, M., Stillwell, D., ... & De Cock, M. (2016). Computational personality recognition in social media. User modeling and user-adapted interaction, 26(2-3), 109-142.

