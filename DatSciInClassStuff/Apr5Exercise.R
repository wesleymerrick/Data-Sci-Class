library(e1071)
setwd("C:/Users/Wesley/PycharmProjects/DatSciInClassStuff")
my.data = read.csv(file = "nyt1.csv", header = TRUE, nrows = 200) # train on the first 200 entries of nyt1.csv

attach(my.data)

x = subset(my.data, select=c(Age, Impressions))
y = Gender

model = svm(x, y)
summary(model)

t = data.frame(20, 8) # predict the gender (0 or 1) of a 20 year-old individual with 8 impressions
summary(x)
predict(model, t)
