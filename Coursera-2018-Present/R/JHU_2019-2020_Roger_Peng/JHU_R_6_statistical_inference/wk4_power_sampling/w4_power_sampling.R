getwd()

library(swirl)
# install_from_swirl("Statistical Inference")

swirl()

#####################################
#   statistical inference week 4    #
#####################################

########################
#   lesson 1: power    #
########################

2
3
2
2
4

myplot(34)

myplot(33.3)

myplot(30)

myplot(28)

3
3

3
4

z <- qnorm(.95)

pnorm(30+z, 30, lower.tail = FALSE)

pnorm(30+z, 32, lower.tail = FALSE)

# A greater standard deviation means more variability in the data so the test will be less powerful
1

pnorm(30+z,32, sd=1, lower.tail = FALSE)

pnorm(30+z*2, mean=32, sd=2, lower.tail = FALSE)

3
2

1
3

1

2
1

2


# omitting one of four arguments still allows R to solve for it, with same results
power.t.test(n = 16, delta = 2 / 4, sd=1,type = "one.sample", alt = "one.sided")$power

power.t.test(n = 16, delta = 2, sd=4,type = "one.sample", alt = "one.sided")$power

power.t.test(n = 16, delta = 100, sd=200,type = "one.sample", alt = "one.sided")$power

# solving for sample size n
power.t.test(power = .8, delta = 2 / 4, sd=1, type = "one.sample", alt = "one.sided")$n

power.t.test(power = .8, delta = 2, sd=4, type = "one.sample", alt = "one.sided")$n

power.t.test(power = .8, delta = 100, sd=200, type = "one.sample", alt = "one.sided")$n


# solving for delta
power.t.test(n = 26, power = .8, sd=1, type = "one.sample", alt = "one.sided")$delta

power.t.test(n = 27, power = .8, sd=1, type = "one.sample", alt = "one.sided")$delta

2
1
1

2
1
3
4
2
2

1

###################################
#   lesson 2: multiple testing    #
###################################
1
2

3
2

3
4

3

1
1
2

2
3

# p hacking
2

4

4
2

head(pValues)

sum(pValues < 0.05)

# controlling FWER
sum(p.adjust(pValues, method = "bonferroni") < 0.05)

# controlling FDR
sum(p.adjust(pValues, method = "BH") < 0.05)

tail(trueStatus)

# creating a crosstab of booleans
table(pValues2 < 0.05, trueStatus)

# % of false positives
24/(500)

# overadjusts
table(p.adjust(pValues2, method = "bonferroni") < 0.05, trueStatus)

# tradeoff 
table(p.adjust(pValues2, method = "BH") < 0.05, trueStatus)


#############################
#   lesson 3: resampling    #
#############################

# The basic bootstrap principle uses OBSERVED 
# data to construct an ESTIMATED population distribution using random sampling with replacement

3
1

2

# computing expected value of a dice roll
sum(1:6)/6

print(g2)
1

head(sh)
nh

median(resampledMedians)
median(sh)

sam <- sample(fh, nh*B, replace = TRUE)

# assigning sam to a matrix
resam <- matrix(sam, nrow = B, ncol = nh)

# takes median of each row
meds <- apply(resam, 1, FUN = median)

median(fh) - median(meds)

# standard error of meds
sd(meds)

sd(resampledMedians)

# calculating 95% confidence interval
quantile(resampledMedians, c(.025, .975))

# calculating CI for fathers' dataset, using meds vector
quantile(meds, c(.025, .975)) #nonparametric method

# finding dimension of insect sprays
dim(InsectSprays)

# checking vars
names(InsectSprays)

# checking max min counts
range(Bdata$count)
range(Cdata$count)

BCcounts
group

# checking to see how function is defined
testStat

# checking diff in stats by group
obs <- testStat(BCcounts, group)
obs

# checkin diff in means manually
mean(Bdata$count - Cdata$count)

3

# sampling from a vector
sample(group)

# running 10000 iterations of mean diff calculation
perms <- sapply(1:10000, function(i) testStat(BCcounts, sample(group)))
  
mean(perms > obs)
  
testStat(DEcounts, group)  

perms <- sapply(1:10000, function(i) testStat(DEcounts, sample(group)))



