library(readr)
library(ggplot2)
library(MASS)
library(leaps)
library(car)
## load dataset
processed_data = read_csv("~/Documents/scripts/traitsPredictor/processed_data.csv")
processed_data = subset(processed_data, select = -c(X1))
## subset dataset 
val = names(processed_data)[1:10]
sext = processed_data[, 1:11]
## fit model
sext1 = sext[1:200, ]
full = lm(sext~., data = sext1)
t = regsubsets(sEXT ~ ., data = sext1, nbest = 5)
plot(t)
subsets(t, statistic = "adjr2")
m1 = lm(sEXT~sadness + positive + surprise + fear, data = sext1)
summary(m1)
anova(m1)
m2 = lm(sEXT ~ negative + sadness + positive + surprise + fear, data = sext1)
summary(m2)
anova(m1, m2)
