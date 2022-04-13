getwd()

library(swirl)
# install_from_swirl("Regression Models")

swirl()

#################################
#   regression models week 4    #
#################################

#############################################
#   lesson 1: variance inflation factors    #
#############################################

# issue i: including too few vars --> bias
# issue ii: including too many vars --> errors

# issue ii is also called variance inflation
# note: variance inflation is due to correlated regressors
3
1
2

# vifSims is an excellent example of calculating multiple simulations of 
# a dependent variable, and the associated coefficients for variables used to simulate it

# here, a 1000 simulations, to be later aggregated to produce one estimate
rgp1()
2

rgp2()

# using car package to estimate vif's: variance inflation estimators
head(swiss)

# regressing fertility outcomes on all 5 measures
mdl <- lm(Fertility ~ Infant.Mortality + Catholic + Education + Examination + Agriculture, swiss)

# calculating vif's for each of 5 regressors
vif(mdl)
# vif's can be used to mentally scale down our estimators in the case of correlation within

# ommitting examination from our model
mdl2 <- lm(Fertility ~ Infant.Mortality + Catholic + Education + Agriculture, swiss)
vif(mdl2)
# lower vif for coefficient is good
# highly correlated vars can be ommitted to lower vif score per coefficient
2
2
2


##############################################
#  lesson 2: Overfitting and Underfitting    #
##############################################
1
3

# 2 x 150 matrix, row1: x1 coef est sans x3, row2: x1 coef sans x2
x1c <- simbias()

# finding mean regressor estimates of each row
apply(x1c, 1, mean)

# exemplifying analysis of variance # swiss data
fit1 <- lm(Fertility ~ Agriculture, swiss)
fit3 <- lm(Fertility ~ Agriculture + Examination + Education, swiss)

# checking significance
anova(fit1, fit3)

1
3

deviance(fit3)

# calculating F value manually
# denom
d <- deviance(fit3)/43

# num
n <- (deviance(fit1) - deviance(fit3))/2

# F value
n/d

# calculating p value 
pf(n/d, 2, 43, lower.tail = FALSE)

# shapiro wilk to test the residuals
shapiro.test(fit3$residuals)

# checking each successive models significance wrt to prev
anova(fit1, fit3, fit5, fit6)

2

# including more regressors decreases residual sum of squares
3
3

##################################
#   lesson 3: binary outcomes    #
##################################
1
4

ravenData

# using glm model to predict wins from points scored
mdl <- glm(ravenWinNum ~ ravenScore, family = binomial, ravenData)

# predicting log odds of wins
lodds <- predict(mdl, data.frame(ravenScore=c(0, 3, 6)))

# converting log odds to probabilities to increase readability
exp(lodds)/(1+exp(lodds))

# checking sd of fit
summary(mdl)

# yields 95% upper and lower bounds of confidence interval
exp(confint(mdl))

1

# lower bound of coef log odds suggest slight decrease in prob of winning at the lower end
2

# using reg to minim var
# using negative log likelihoods in place of variance
anova(mdl)

# using chi square to test whether coef is diff from 0
qchisq(0.95, 1)


#################################
#   lesson 4: count outcomes    #
#################################

# expected rate of occurence: lambda
# mean of poisson = var of poisson = lambda

# checking sample var vs theor var
var(rpois(1000, 50))
3
Yes

View(hits)

# checking date type 
class(hits[,'date'])

# performing operations on dates
as.integer(head(hits[,'date']))

# using poisson to predict site visits by date
mdl <- glm(visits ~ date, poisson, hits)

# checking coefficients and significance
summary(mdl)

# getting the 95 % conf int
exp(confint(mdl, 'date'))

# checking date of max hits to website 
# the following prints the row num / index - where row num indicates sample number
which.max(hits[,'visits'])

# printing max hits row
hits[704,]

# extracting row 704 obs for fitted.values for comparison
lambda <- mdl$fitted.values[704] 

# checking 95th percentile of poisson distribution
qpois(.95, lambda)

# using log(visits+1) in order to avoid division by 0
# setting offset parameter to log(visits+1)
mdl2 <- glm(simplystats ~ date, poisson, hits, offset = log(visits+1))

# checking mdl2's 95th percentile to see if the actual visits - 64 - are approached by our predicted model
# prediction at 95th percentile shows 47 visits, a ways off from 64
qpois(.95, mdl2$fitted.values[704])

2
3
3



