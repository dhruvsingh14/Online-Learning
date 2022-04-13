getwd()

#install.packages("datasets")
library(swirl)

# packageVersion("swirl")

swirl()

# quiz 4

# q1
set.seed(1)
rpois(5, 2)

# q5
set.seed(10)
x <- rep(0:1, each = 5)
e <- rnorm(10, 0, 20)
y <- 0.5 + 2 * x + e

#q8
library(datasets)
Rprof()
fit <- lm(y ~ x1 + x2)
Rprof(NULL)


### swirl lesson on simulation continued 

# sampling with replacement
?sample
flips <- sample(c(0, 1), 100, replace = TRUE, prob = c(0.3, 0.7))
flips

sum(flips)

?rbinom

# random binomial variable, 1 obs of size 100
rbinom(1, size = 100, prob = 0.7)

# random binomial variable, 100 obs of size 1
flips2 <- rbinom(100, size = 1, prob = 0.7)
flips2

sum(flips2)

?rnorm

# generating random normal numbers
rnorm(10)
rnorm(10, 100, 25)

# generating random poisson numbers
?rpois
rpois(5, 10)

# using replicate to create a matrix with a column for each random vector
my_pois <- replicate(100, rpois(5, 10))
my_pois
cm <- colMeans(my_pois)

hist(cm)

# Swirl: R Programming/ 15: Base Graphics

data(cars)

?cars

head(cars)

# getting a sense of the data using exploratory plot
plot(cars)

?plot

plot(x = cars$speed, y = cars$dist)
plot(x = cars$dist, y = cars$speed)

# labeling axes
plot(x = cars$speed, y = cars$dist, xlab = "Speed")
plot(x = cars$speed, y = cars$dist, ylab = "Stopping Distance")
plot(x = cars$speed, y = cars$dist, xlab = "Speed", ylab = "Stopping Distance")

# labeling plot
plot(cars, main = "My Plot")
plot(cars, sub = "My Plot Subtitle")
?plot

# including color
?par
plot(cars, col = 2)

# limiting x axis using bounds
plot(cars, xlim = c(10, 15))

# changing points shape
?points
plot(cars, pch = 2)

# exploring boxplots
data(mtcars)
?boxplot
boxplot(mpg ~ cyl, data = mtcars)

# exploring histograms
hist(mtcars$mpg)
