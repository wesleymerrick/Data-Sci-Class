library(datasets)
library(ggplot2)

head(iris)

irisCluster = kmeans(iris[,3:4], 3)

irisCluster

table(irisCluster$cluster, iris$Species)

irisCluster$cluster = as.factor(irisCluster$cluster)

ggplot(iris,aes(Petal.Length, Petal.Width, color=irisCluster$cluster)) + geom_point()
