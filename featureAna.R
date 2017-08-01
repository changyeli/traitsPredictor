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

train = read_csv("~/Documents/scripts/traitsPredictor/mypersonality_final.csv", col_names = TRUE)
train$cEXT = ifelse(train$cEXT == "y", 1, 0)
train$cAGR = ifelse(train$cAGR == "y", 1, 0)
train$cNEU = ifelse(train$cNEU == "y", 1, 0)
train$cCON = ifelse(train$cCON == "y", 1, 0)
train$cOPN = ifelse(train$cOPN == "y", 1, 0)

cEXT = subset(train, select = c(STATUS, cEXT))
cAGR = subset(train, select = c(STATUS, cAGR))
cNEU = subset(train, select = c(STATUS, cNEU))
cCON = subset(train, select = c(STATUS, cCON))
cOPN = subset(train, select = c(STATUS, cOPN))

write_csv(cEXT, "cEXT.csv")
write_csv(cAGR, "cAGR.csv")
write_csv(cNEU, "cNEU.csv")
write_csv(cCON, "cCON.csv")
write_csv(cOPN, "cOPN.csv")
