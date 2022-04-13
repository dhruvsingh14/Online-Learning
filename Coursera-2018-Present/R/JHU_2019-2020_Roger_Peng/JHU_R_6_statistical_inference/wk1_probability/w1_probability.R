# install.packages("swirl")
# packageVersion("swirl")

getwd()

library(swirl)

# install_from_swirl("Statistical Inference")

swirl()

#####################################
#   statistical inference week 1    #
#####################################


################################
#   lesson 1: probability 1    #
################################
deck

52

4/52

0

12/52

2/51

################################
#   lesson 2: probability 2    #
################################

# deriving pdf -> yields cdf
mypdf

# integrating
integrate(mypdf, lower = 0, upper = 1.6)

# survivor function = 1 - cdf


###################################
#   lesson 3: conditional prob    #
###################################

5
4
2
3

# Bayes' Rule
# P(B|A) = P(B&A)/P(A) = P(A|B) * P(B)/P(A)

# substituting
# P(A) = P(A|B) * P(B) + P(A|~B) * P(~B)

# obtaining converse form of Bayes'
# P(B|A) = P(A|B) * P(B) / ( P(A|B) * P(B) + P(A|~B) * P(~B) )

# HIV test example: specificity vs sensitivity
3
3

# HIV example, key values
# P(D) = 0.001 
# P(~D) = 0.999

# P(+|D) = 99.7%
# P(-|D) = 98.5%

# P(+|~D) = 1-P(-|~D)
s
# P(+|D)*P(D)
.997*.001

# P(+|~D)*P(~D) 
.015*.999

# prob of actually having disease, given positive test result
# P(D|+)
(.997*.001)/(.000997+.014985) # positive predictive value

# diagnostic likelihood ratio

# DLR+ = P(+|D)/P(+|~D)
# DLR- = P(-|D)/P(-|~D)

3
2

3
2

# post test odds vs pre test odds
3

# wrap up
2
2

1


#############################
#  lesson 4: Expectations   #
#############################

# expect value of X
1/6*(1+2+3+4+5+6)

# checking function
expect_dice

# loaded dice vector
dice_high

# running function on loaded dice
expect_dice(dice_high)
expect_dice(dice_low)

# exp value of rolling 2 loaded dice
0.5*(edh + edl)
1

# expected value as area under t*f(t)
1

# integrating function to find expected value
integrate(myfunc, 0, 2)

# examining means of sample populations
spop
mean(spop)

# taking repeat samples
allsam

# mean of each row
apply(allsam, 1, mean)
mean(smeans)

# review
2
1
1
2
2
1


#################
#  quiz week 1  #
#################

#q1
# .17 = .12 + P(M) - .06
# P(M) = .11

#q2









