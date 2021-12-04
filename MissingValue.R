
install.packages("readr")
library(readr) 

install.packages("missForest")
library(missForest)

claimants <- read.csv(file.choose())
sum(is.na(claimants)) 
summary(claimants)

claimants$CLMSEX[is.na(claimants$CLMSEX)] <- mean(claimants$CLMSEX, na.rm = TRUE)
sum(is.na(claimants$CLMSEX)) 

claimants$CLMINSUR[is.na(claimants$CLMINSUR)] <- mean(claimants$CLMINSUR, na.rm = TRUE)
sum(is.na(claimants$CLMINSUR)) 

claimants$SEATBELT[is.na(claimants$SEATBELT)] <- mean(claimants$SEATBELT, na.rm = TRUE)
sum(is.na(claimants$SEATBELT)) 

claimants$CLMAGE[is.na(claimants$CLMAGE)] <- mean(claimants$CLMAGE, na.rm = TRUE)
sum(is.na(claimants$CLMAGE)) 

