getwd()

# install.packages("swirl")
# packageVersion("swirl")

library(swirl)
install_from_swirl("R Programming")

swirl()

# week 1, quiz 1

# q4
x <- 4
class(x)

# q5
x <- c(4, "a", TRUE)
class(x)

# q6
x <- c(1, 3, 5)
y <- c(3, 2, 10)

cbind(x, y)

# q8
x <- list(2, "a", "b", TRUE)
x[[2]]
class(x[[2]])

# q9
x <- 1:4
y <- 2:3

x+y

# q10
x <- c(3, 5, 1, 12, 10, 6)
x

x[x <= 5]
x[x %in% 1:5]
x[x < 6]

# q11
ozone_data <- read.csv("hw1_data.csv")

# q12
ozone_data[1:2,]

# q14
ozone_data[152:153,]

#q15
ozone_data[47,]

# q16
sum(is.na(ozone_data$Ozone))
sum(is.na(ozone_data[,1]))

# q17
good <- ozone_data$Ozone[!is.na(ozone_data$Ozone)]
mean(good)

# q18
oz_subs <- subset(ozone_data, Ozone > 31  & Temp > 90)
mean(oz_subs$Solar.R)

# q19
oz_subs2 <- subset(ozone_data, Month == 6)
mean(oz_subs2$Temp)

# q20
summary(ozone_data$Ozone[ozone_data$Month == 5])
