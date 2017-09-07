library(class)
x = c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
y = c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)
xandy = cbind(x, y)
xy_train = xandy[1:8, ]
xy_test = xandy[9:10, ]
ycl = y[1:8]

pred = knn(train = xy_train, test = xy_test, cl = ycl, k =5)
pred

y[9:10]