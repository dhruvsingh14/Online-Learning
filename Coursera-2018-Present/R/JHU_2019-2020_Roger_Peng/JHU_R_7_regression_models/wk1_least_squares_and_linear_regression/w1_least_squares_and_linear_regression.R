getwd()

# install.packages('manipulate', repos='http://cran.us.r-project.org')

library(manipulate)

library(swirl)
# install_from_swirl("Regression Models")

swirl()

#################################
#   regression models week 1    #
#################################

###############################
#   lesson 1: introduction    #
###############################

# measurement error adjusts plots to make them appear the same
plot(child ~ parent, galton)

# jitter means disrupting near similar points w/ m.e. to make them appear dispersed
plot(jitter(child, 4) ~ parent, galton)

# overlaying regression line
regrline <- lm(child ~ parent, galton)
abline(regrline, lwd = 3, col = 'red')

# Coefficients:
#             Estimate  Std. Error  t value  Pr(>|t|)    
# (Intercept) 23.94153    2.81088   8.517    <2e-16 ***
#   parent    0.64629     0.04114   15.711   <2e-16 ***

# recall coeff +- 2*se yields confidence bands

# examining of fitted regline
summary(regrline) # slope of 0.64


############################
#   lesson 2: residuals    #
############################

# likelihood of residuals (or errors) being positive or negative same
# residuals must be uncorrelated with predictors

# reg line
fit <- lm(child ~ parent, galton)

# residual vector
fit$residuals

# regression diagnostics
summary(fit)

# hyp: residuals mean = 0
mean(fit$residuals)
# -2.359884e-15

# checking residual - predictor correlation
cov(fit$residuals, galton$parent)

# residuals = est(ht) - actual(ht)
# deviance function helps calculate this

# extracting intercept
ols.ic <- fit$coef[1]

# extracting slope
ols.slope <- fit$coef[2]

# sample code
# #Here are the vectors of variations or tweaks
# sltweak <- c(.01, .02, .03, -.01, -.02, -.03) #one for the slope
# ictweak <- c(.1, .2, .3, -.1, -.2, -.3)  #one for the intercept
# lhs <- numeric()
# rhs <- numeric()
# #left side of eqn is the sum of squares of residuals of the tweaked regression line
# for (n in 1:6) lhs[n] <- sqe(ols.slope+sltweak[n],ols.ic+ictweak[n])
# #right side of eqn is the sum of squares of original residuals + sum of squares of two tweaks
# for (n in 1:6) rhs[n] <- sqe(ols.slope,ols.ic) + sum(est(sltweak[n],ictweak[n])^2)

# testing equality
lhs - rhs
all.equal(lhs, rhs) # almost like a ttest

# calculating variation in children's heights
varChild <- var(galton$child)

# calculating variance in residuals
varRes <- var(fit$residuals)

# calculating variance in estimates (y - coordinates)
varEst <- var(est(ols.slope, ols.ic))

# testing equality of variance in data and sum of variances in est, and residuals
# var(data) = var(estimate) + var(residuals)
all.equal(varChild, varRes + varEst)
# var(est) always less than var(data)

# example data 2: CA earthquakes data, mulivar

# generating reg line, and saving as a var, generates all subcomponents
# eg: residuals, coefficients, all as variables, or elements of reg var
efit <- lm(accel ~ mag+dist, attenu)
mean(efit$residuals) # mean is damn near 0

cov(efit$residuals, attenu$mag) # corr resid vs mag. predictor
cov(efit$residuals, attenu$dist) # corr resid vs dist. predictor


###########################################
#   lesson 3: least squares estimation    #
###########################################

4

1

4

# corr doesn't change from normalization
cor(gpa_nor, gch_nor)

3

l_nor <- lm(gch_nor ~ gpa_nor)

3
3

1

