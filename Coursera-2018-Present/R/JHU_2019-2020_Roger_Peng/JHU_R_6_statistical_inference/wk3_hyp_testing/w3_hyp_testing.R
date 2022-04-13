getwd()

library(swirl)
# install_from_swirl("Statistical Inference")

swirl()

#####################################
#   statistical inference week 3    #
#####################################


##############################
#   lesson 1: conf.interv    #
##############################

2
4
2
1

myplot(2)
myplot(20)

myplot2(2)
qt(.975,2)

myplot2(20)

2
sleep

# range of two vectors
range(g1)
range(g2)

# pairwise distributions
difference <- g2 - g1

mean(difference)

s <- sd(difference)

mn + c(-1,1)*qt(.975,9)*s/sqrt(10)

t.test(difference)$conf.int

sp <- (7)*(15.34)^2 + (20)*(18.23)^2

ns <- 27

sp/ns


sp <- sqrt(sp/ns)

132.86-127.44 + c(-1,1)*qt(.975,ns)*sp*sqrt(1/8+1/21)

sp <- sqrt((9*var(g1)+9*var(g2))/18)

# computing confidence intervals given quantiles, degrees of freedom, and sample size
md + c(-1,1)*qt(.975,18)*sp*sqrt(1/10+1/10)

# checking manual computation using inbuilt function
t.test(g2, g1, paired = FALSE, var.equal = TRUE)$conf

t.test(g2, g1, paired = TRUE)$conf

# calculating degrees of freedom
num <- (15.34^2/8 + 18.23^2/21)^2

den <- 15.34^4/8^2/7 + 18.23^4/21^2/20

mydf <- num/den

132.86-127.44+c(-1,1)*qt(.975,mydf)*sqrt(15.34^2/8 + 18.23^2/21)

#####################################
#   lesson 2: hypothesis testing    #
#####################################
2
2
4
1
2

# standard error of the mean formula 
10/sqrt(100)

1
2
3
3
2

2
2
2

(32-30)/(10/sqrt(16))
15

qt(.95,15)

# sample mean not falling within rejection region means fail to reject null hypothesis
3

2
2
4

2

# using R t.test function
dim(fs)

t.test(fs$fheight-fs$sheight)
4

# when significant, the test stat tells us:
# the number of estimated std errors between the sample and hypothesized means

# testing
11.7885 * sd(fs$sheight-fs$fheight)/sqrt(1078)

# twins gender hypothesis testing
mybin

8
1

###########################
#   lesson 3: p values    #
###########################

4
3
1

pt(q=2.5,df=15,lower.tail = FALSE)
2

# p-value is the smallest value of alpha at which you will reject the null hypothesis
qnorm(0.95)
qnorm(0.99)

1

# hypothesis test using probabilities
pnorm(2)
pnorm(2, lower.tail = FALSE)

mybin

pbinom(6, size = 8, prob = .5, lower.tail = FALSE)
1
2
2

# probability that X<=7
pbinom(7, size = 8, prob = .5, lower.tail = TRUE)

# switching to discrete poisson tests
ppois(9, lambda = 5, lower.tail = FALSE)
2

