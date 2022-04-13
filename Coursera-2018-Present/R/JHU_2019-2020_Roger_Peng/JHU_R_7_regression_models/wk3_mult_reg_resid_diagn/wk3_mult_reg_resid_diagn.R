getwd()

library(swirl)
# install_from_swirl("Regression Models")

swirl()

#################################
#   regression models week 3    #
#################################

#################################
#   lesson 1: Multivar Egs.2    #
#################################

# insect spray data
6
B

# dimension of the data
dim(InsectSprays)

# displaying first 15 rows
head(InsectSprays, 15)

# displaying array
sC

# checking column counts
summary(InsectSprays[,2])

# checking column classes
sapply(InsectSprays, class)

# generating linear model to predict count
fit <- lm(count ~ spray, InsectSprays)
summary(fit)$coef

est <- summary(fit)$coef[,1]

mean(sA)

4

mean(sB)

# model without intercept
nfit <- lm(count ~ spray - 1, InsectSprays)

# when intercept included, sA is base reference group
# when intercept ommitted, sA has explicit estimate
summary(nfit)$coef

1

# w/o intercepts, estimates are w reference to 0 as base group
# est are means, and test for sign diff from 0

1

# using r function relevel to set diff baseline from sA
# created a new predictor variable, reordering factor to make C baseline
spray2 <- relevel(InsectSprays$spray, "C")

fit2 <- lm(count ~ spray2, InsectSprays)
summary(fit2)$coef

# since sray C doesn't doesn't have coef, we see it is the baseline
3

# verifying answer matching intercept
mean(sC)

# now estimator for spray A = coeff A + intercept

# calculating spray2B's t value
(fit$coef[2] - fit$coef[3])/1.6011


#################################
#   lesson 2: Multivar Egs.3    #
#################################

dim(hunger)

# each row represents a sample
948

# checking column names
names(hunger)

# predicting hunger rates
fit <- lm(Numeric ~ Year, hunger)
summary(fit)$coef
1
3
1

# subsetting model prediction to gender = female
lmF <- lm(Numeric[hunger$Sex == "Female"] ~ Year[hunger$Sex == "Female"], hunger)
lmM <- lm(Numeric[hunger$Sex == "Male"] ~ Year[hunger$Sex == "Male"], hunger)

3

lmBoth <- lm(Numeric ~ Year + Sex, hunger)
summary(lmBoth)

3
1
1

# adding interacted variable to model
lmInter <- lm(Numeric ~ Year + Sex + Sex*Year, hunger)
summary(lmInter)
1
3
3
2
1

# some notes on interacted coefficients, when predictors held constant

# Suppose we have two interacting predictors and one of them is held constant. 
# The expected change in the outcome for a unit change in the other predictor is the
# coefficient of that changing predictor + 
# the coefficient of the interaction * the value of the predictor held constant.


########################################################
#   lesson 3: Residuals, Diagnostics, and Variation    #
########################################################

# addressing influential outlier
fit <- lm(y ~ x, out2)

# residuals vs. fitted plot
plot(fit, which = 1)

1
1

# creating a model without the influential outlier
fitno <- lm(y ~ x, out2[-1,])

# residuals vs. fitted plot
plot(fitno, which = 1)

# checking change induced by including influential
coef(fit) - coef(fitno)

head(dfbeta(fit))

# preparing to calculate influence from residuals ratio
resno <- out2[1, "y"] - predict(fitno, out2[1,])

# calculating influence of outlier
1 - resid(fit)[1]/resno

# hatvalues
head(hatvalues(fit))

# calculating sample standard deviation of fit's residual
sigma <- sqrt(deviance(fit)/df.residual(fit))

# computing the standardized residual
rstd <- resid(fit)/(sigma*sqrt(1-hatvalues(fit))) 

# comparing two columns side by side using a simple head + cbind
head(cbind(rstd, rstandard(fit)))

plot(fit, which = 3)

# diagnostic plot
plot(fit, which=2)
1

# calculating the sample deviation of residual
sigma1 <- sqrt(deviance(fitno)/df.residual(fitno))

# calculating studentized residual
resid(fit)[1] / (sigma1 * sqrt(1-hatvalues(fit)[1]))

# comparing the studentized residual with those of the other sample
head(rstudent(fit))

# cook's distance - tells how much a sample changes a model
# comparing models with and without outlier included, we have
dy <- predict(fitno, out2) - predict(fit, out2)

# calculating outlier's cook's distance
sum(dy^2)/(2*sigma^2) 

# displaying diagnostic plot for cook's distance
plot(fit, which=5)

