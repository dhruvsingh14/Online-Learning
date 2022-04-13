getwd()

library(swirl)
# install_from_swirl("Regression Models")

swirl()

#################################
#   regression models week 2    #
#################################

#####################################
#   lesson 1: Residual Variation    #
#####################################

fit <- lm(child ~ parent, galton)

# taking square root of sum of squared residuals / qty
sqrt(sum(fit$residuals^2)/(n-2))

# looking at the sigma portion of fit summary
summary(fit)$sigma

sqrt(deviance(fit)/(n-2))

# total variation
# Yi-mean(Yi)

# residual variation
# Yi-Yi_hat

# storing away children's heights
mu <- mean(galton$child)

# centering data => subtracting the mean from each data point
sTot <- sum((galton$child - mu)^2)

sRes <- deviance(fit)

# regression variation
1- sRes/sTot

# extracting generated reg variation as comparison
summary(fit)$r.squared

cor(galton$child, galton$parent)^2


########################################
#   lesson 2: Intro to Multivar Reg    #
########################################

ones <- rep(1, nrow(galton))

# using -1 suppresses the intercept
lm(child ~ ones + parent - 1, galton)

lm(child ~ ones + parent, galton)

1

# Gaussian Elimination
# subtracting mean from regressor and regressed vars, eliminates slope
# and passes regression line through the origin

# sometimes replaces variables w/ their residuals (kind of like errors) as a form of estimation

1

# the mean of a variable = coeff from regressing var against 1
# mean(var) = lm(var ~ 1, data)$coeff
lm(child ~ 1, galton)

head(trees)
3

# storing reg for later use
fit <- lm(Volume ~ Girth + Height + Constant - 1, trees)

# eliminating girth from dataset
trees2 <- eliminate("Girth", trees)
head(trees2)

2

# plotting reduced model, fewer regressors, to see size of constant unchanged
fit2 <- lm(Volume ~ Height + Constant - 1, trees2)

lapply(list(fit, fit2), coef)

2


#####################################
#   lesson 3: Multivar Reg  Eg.s    #
#####################################
4

# predicting fertility
all <- lm(Fertility ~ ., swiss)

# summarizing all predictor model
summary(all)

1

# generating model in one regressor
summary(lm(Fertility ~ Agriculture, swiss))
4
1

# checking correlations between variables
cor(swiss$Examination, swiss$Education)
cor(swiss$Agriculture, swiss$Education)

all

# running makelms()
makelms()

1

# model with added extraneous information remains unchanged
ec <- swiss$Examination + swiss$Catholic
efit <- lm(Fertility ~ . + ec, swiss)

# verifying
all$coefficients - efit$coefficients
3
3

