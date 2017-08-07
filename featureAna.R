library(readr)
library(ggplot2)
library(MASS)
## load dataset
processed_data = read_csv("~/Documents/scripts/traitsPredictor/processed_data.csv")
processed_data = subset(processed_data, select = -c(X1))
## subset dataset 
val = names(processed_data)[1:10]
sext = processed_data[, 1:11]
## fit model
pairs(sext[, 1:10])
full = lm(sEXT ~., data = sext)
step(full, steps = 10000, k = 2, direction = "both")
m2 = lm(sEXT ~ sadness + positive + surprise + fear, data = sext)
m3 = lm(sEXT ~ sadness + positive + fear, data = sext)
summary(m2)
anova(m2, m3)
