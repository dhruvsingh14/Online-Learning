# install.packages('ggplot2movies', repos='http://cran.us.r-project.org')

library(nlme)
library(lattice)
library(datasets)
library(ggplot2)
library(ggplot2movies)


# q2
xyplot(weight ~ Time | Diet, BodyWeight)

# q4
data(airquality)
p <- xyplot(Ozone ~ Wind | factor(Month), data = airquality)

# q9
g <- ggplot(movies, aes(votes, rating))
print(g)

# q10
qplot(votes, rating, data = movies)




