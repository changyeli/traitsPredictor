library(readr)
library(leaps)
library(car)
library(e1071)
## load dataset
processed_data = read_csv("~/Documents/scripts/traitsPredictor/processed_data.csv")
## subset dataset 
val = names(processed_data)[1:10]
sext = processed_data[, 1:11]
## fit model, "traditional stat way"
sext1 = sext[1:200, ]
sext2 = sext[201:250, ]
full = lm(sEXT~., data = sext1)
t = regsubsets(sEXT ~ ., data = sext1, nbest = 10)
plot(t)
subsets(t, statistic = "adjr2", legend = FALSE)
step(full, scale = 0, direction = "backward")
m1 = lm(sEXT ~ positive + fear, data = sext1)
m2 = lm(sEXT ~ sadness + positive + surprise + fear, data = sext1)
m3 = lm(sEXT ~ sadness + positive + fear, data = sext1)
m4 = lm(sEXT ~ sadness + disgust + positive + surprise + fear, data = sext1)
m5 = lm(sEXT ~ negative + sadness + positive + surprise + fear, data = sext1)
m6 = lm(sEXT ~ sadness + disgust + anger + surprise + fear, data = sext1)
m7 = lm(sEXT ~ joy + negative + sadness + positive + surprise + fear, data = sext1)
m8 = lm(sEXT ~ anger + joy + negative + sadness + positive + surprise + fear + trust, data = sext1)
## calculate rMSE and MAE
evaluate = function(actually, predicted){
  error = actually - predicted
  print(sqrt(mean(error)))
  print(mean(abs(error)))
}
pre = predict(m1, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m2, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m3, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m4, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m5, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m6, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m7, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

pre = predict(m8, newdata = sext2)
evaluate(sext2$sEXT, pre)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)

## Support Vector Regression
model1 = svm(sEXT ~ sadness + positive + surprise + fear, data = sext1)
pre = predict(model1, sext2)
plot(sext2$sEXT)
points(pre, col = "red", pch = 16)
pre
