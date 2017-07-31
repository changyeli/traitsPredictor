library(readr)
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
