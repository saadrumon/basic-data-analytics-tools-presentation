require("datasets")
data("iris")
head(iris)
summary(iris)

X <- iris[,c(1, 2)]
y <- iris[,"Species"]

normalize <- function(x) {
  return ((x-min(x))/(max(x)-min(x)))
}

X$Sepal.Length <- normalize(X$Sepal.Length)
X$Sepal.Width <- normalize(X$Sepal.Width)
head(X)

result <- kmeans(X, 3)

result$size
result$centers

plot(X, col=result$cluster)
plot(X, col=y)
