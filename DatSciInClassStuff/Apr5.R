library(e1071)
data("iris")
summary(iris)
attach(iris)
Species
x = subset(iris, select=-Species)
View(x)
y = Species
model = svm(x, y)
summary(model)
t = data.frame(6, 3, 5, 1.2)
summary(x)
predict(model, t)

testX = x[81, ]
predict(model, testX)

