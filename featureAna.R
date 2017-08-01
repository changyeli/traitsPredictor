library(readr)
library(reshape2)
library(ggplot2)
allData = read_csv("~/Documents/scripts/traitsPredictor/clean/allData.csv", 
                    col_names = c('anticipation', 'joy', 'negative', 'sadness', 
                                  'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust'))
labels = read_delim("~/Documents/scripts/traitsPredictor/clean/labels.txt", 
                     "\n", escape_double = FALSE, col_names = c("cluster"), 
                     trim_ws = TRUE)
allData[, 11] = labels
c1 = subset(allData, cluster == 0)
c2 = subset(allData, cluster == 1)
c3 = subset(allData, cluster == 2)
c4 = subset(allData, cluster == 3)
c5 = subset(allData, cluster == 4)
names = c('anticipation', 'joy', 'negative', 'sadness', 
          'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust')
## remove all 0 columns and labels
c1 = c1[, colSums(c1 != 0) > 0]
c2 = c2[, colSums(c2 != 0) > 0]
c2 = subset(c2, select = -c(cluster))
c3 = c3[, colSums(c3 != 0) > 0]
c3 = subset(c3, select = -c(cluster))
c4 = c4[, colSums(c4 != 0) > 0]
c4 = subset(c4, select = -c(cluster))
c5 = c5[, colSums(c5 != 0) > 0]
c5 = subset(c5, select = -c(cluster))
## histogram of cluster 1
ggplot(data = melt(c1), mapping = aes(x = value)) +
  geom_histogram(bins = 10) + facet_wrap(~variable)
## histogram of cluster 2
ggplot(data = melt(c2), mapping = aes(x = value)) +
  geom_histogram(bins = 10) + facet_wrap(~variable, scales = "free_x")
