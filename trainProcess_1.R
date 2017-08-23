library(readr)
trainV2 <- read_csv("~/Documents/scripts/traitsPredictor/clean/trainV2.csv", 
                    col_names = FALSE)    
colnames(trainV2) = c('anticipation', 'joy', 'negative', 'sadness', 'disgust', 
                      'positive', 'anger', 'surprise', 'fear', 'trust',
                      'sEXT', 'sNEU', 'sAGR', 'sCON', 'sOPN',
                      'cEXT', 'cNEU', 'cAGR', 'cCON', 'cOPN')
extY = subset(trainV2, cEXT == 1)
extN = subset(trainV2, cEXT == 0)
neuY = subset(trainV2, cNEU == 1)
neuN = subset(trainV2, cNEU == 0)
agrY = subset(trainV2, cAGR == 1)
agrN = subset(trainV2, cAGR == 0)
conY = subset(trainV2, cCON == 1)
conN = subset(trainV2, cCON == 0)
opnY = subset(trainV2, cOPN == 1)
opnN = subset(trainV2, cOPN == 0)
###################################
extY = extY[, 1:15]
extN = extN[, 1:15]
neuY = neuY[, 1:15]
neuN = neuN[, 1:15]
agrY = agrY[, 1:15]
agrN = agrN[, 1:15]
conY = conY[, 1:15]
conN = conN[, 1:15]
opnY = opnY[, 1:15]
opnN = opnN[, 1:15]
##################################
write_csv(extY, "extY.csv")
write_csv(extN, "extN.csv")
write_csv(neuY, "neuY.csv")
write_csv(neuN, "neuN.csv")
write_csv(agrY, "agrY.csv")
write_csv(agrN, "agrN.csv")
write_csv(opnY, "opnY.csv")
write_csv(opnN, "opnN.csv")
write_csv(conY, "conY.csv")
write_csv(conN, "conN.csv")

