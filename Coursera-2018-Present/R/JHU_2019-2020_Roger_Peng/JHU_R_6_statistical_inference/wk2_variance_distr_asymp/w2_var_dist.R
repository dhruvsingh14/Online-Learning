getwd()

library(swirl)
# install_from_swirl("Statistical Inference")

swirl()

#####################################
#   statistical inference week 2    #
#####################################


###########################
#   lesson 1: variance    #
###########################

# sqrd values for dice roll for computing variance
dice_sqr

# creating componentwise weights for fair dice roll
ex2_fair <- sum(dice_sqr * dice_fair)

# computing sample variance of fair dice
ex2_fair - 3.5^2

# computing sample variance high value loaded dice
sum(dice_sqr * dice_high) - edh^2

4
2
4
3

# how much sample averages vary
sd(apply(matrix(rnorm(10000),1000),1,mean))

# s/sqrt(n) is the standard error of the sample mean
1/sqrt(10)
3

# std error of mean of unif sample size
1/sqrt(120)

# checking calculation using simulation
sd(apply(matrix(runif(10000),1000),1,mean))

# s.e. poisson(4) = 2/sqrt(n)
2/sqrt(10)

# checking using simulation
sd(apply(matrix(rpois(10000,4),1000),1,mean))


# computing se for 10 coin flips
3
1/(2*sqrt(10))
sd(apply(matrix(sample(0:1,10000,TRUE),1000),1,mean))

1
1
3
1
3
2


#################################
#   lesson 2: common distros    #
#################################
3
4

3
1
5

3


3
3

1

# P(3H) = (5 choose 3)(0.8)^3(0.2)^2
# P(4H) = (5 choose 4)(0.8)^4(0.2)^1

# binomial distribution
pbinom(2, 5, 0.8, lower.tail = FALSE)

# std normal distribution

qnorm(.10)
1
0
2

# std dev using qnorm function
qnorm(.975, 3, 2)

# computing quantiles by hand
1.96*2 + 3


# P(X>1200)

pnorm(1200, 1020, 50, lower.tail = FALSE)

# transforming to standard normal
pnorm((1200-1020)/50, lower.tail = FALSE)

qnorm(0.75, 1020, 50, lower.tail = TRUE)

# pnorm and qnorm are inverses

pnorm(qnorm(.53))

0.53

# Poisson Distribution
ppois(3, 2.5*4, lower.tail = TRUE, log.p = FALSE)

# poisson as approximating binom in certain cases
pbinom(5, 1000, 0.01, lower.tail = TRUE, log.p = FALSE)

# poisson distribution
ppois(5, 1000*0.01)


##############################
#   lesson 3: asymptotics    #
##############################
1
coinPlot(10)

coinPlot(10000)
1

3
4

qnorm(.95)
1
3
2
2
3

# Wald CI
.6 + c(-1,1)*qnorm(.975)*sqrt(.6*.4/100)

play()
binom.test(60, 100)$conf.int
nxt()

mywald(.20)
ACCompar(20)

2

# est mean
lamb <- 5/94.32

# est var
lamb/94.32

# conf. interv.
lamb + c(-1,1)*qnorm(.975)*sqrt(lamb/94.32)


poisson.test(5, 94.32)$conf
1
2
1
1
2
2
4
1
3
1
1
2

