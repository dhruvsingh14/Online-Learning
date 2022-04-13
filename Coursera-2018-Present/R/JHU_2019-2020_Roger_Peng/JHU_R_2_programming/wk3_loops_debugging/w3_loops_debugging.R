getwd()

# packageVersion("swirl")

library(swirl)
library(datasets)


swirl()


#################
#### Quiz 3  ####
#################


# q1
data(iris)
?iris
round(mean(iris$Sepal.Length[iris$Species=='virginica']))

# q2: returns a vector of means for each column
apply(iris[, 1:4], 2, mean)

# q3
data(mtcars)
?mtcars

# the following calculate mpg by no. of cyl.

sapply(split(mtcars$mpg, mtcars$cyl), mean)

tapply(mtcars$mpg, mtcars$cyl, mean)

with(mtcars, tapply(mpg, cyl, mean))


# q4
tapply(mtcars$hp, mtcars$cyl, mean)

round(abs(82.63636 - 209.21429))

# q5
#debug(ls)
ls
