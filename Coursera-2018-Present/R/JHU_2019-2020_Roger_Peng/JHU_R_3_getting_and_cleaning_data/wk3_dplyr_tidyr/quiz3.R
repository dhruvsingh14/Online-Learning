# quiz 3

getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_3_data_cleaning/wk3_dplyr_tidyr")

# install.packages('httr', repos='http://cran.us.r-project.org')
# install.packages('sqldf', repos='http://cran.us.r-project.org')
# install.packages('RMySQL', repos='http://cran.us.r-project.org')
# install.packages('curl', repos='http://cran.us.r-project.org')
# install.packages('jpeg', repos='http://cran.us.r-project.org')
# install.packages('gtools', repos='http://cran.us.r-project.org')

library(httr)
library(sqldf)
library(curl)
library(data.table)
library(jpeg)
library(gtools)


######
# q1 #
######

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileUrl, destfile="Idaho_acs.csv", method="curl")
Idaho_acs <- fread("Idaho_acs.csv")

agricultureLogical <- Idaho_acs$ACR == 3  & Idaho_acs$AGS == 6
which(agricultureLogical)


######
# q2 #
######

# downloading image file
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fjeff.jpg"
download.file(fileUrl, destfile="jeff_leek.jpg", method="curl")

# reading in image
jeff_leek <- readJPEG("jeff_leek.jpg", native = TRUE)

quantile(jeff_leek, c(.30, .80))


######
# q3 #
######

# downloading gdp csv file
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
download.file(fileUrl, destfile="gdp.csv", method="curl")

# reading in gdp
gdp <- fread("gdp.csv", skip = 3, header = T)
gdp <- gdp[c(-1), ]
names(gdp)[1] <- "CountryCode"
names(gdp)[5] <- "GDP"
gdp$CountryCode <- toupper(gdp$CountryCode)


# downloading education csv file
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(fileUrl, destfile="educ.csv", method="curl")

# reading in gdp
educ <- fread("educ.csv")
educ$CountryCode <- toupper(educ$CountryCode)

m1 <- merge(gdp, educ, by = "CountryCode")
m1$GDP <- gsub(",", "", m1$GDP)
m1$GDP <- as.numeric(m1$GDP)

summary(m1$Ranking)

m1$Ranking <- as.numeric(m1$Ranking)

m2 <- m1[!is.na(m1$Ranking)]
m2 <- m2[order(GDP),]


######
# q4 #
######



high <- m2[m2$`Income Group` == "High income: OECD"]
mean(high$Ranking)

high_non <- m2[m2$`Income Group` == "High income: nonOECD"]
mean(high_non$Ranking)

######
# q5 #
######

quantile(m2$Ranking, c(.20, .40, .60, .80))

quantiles <- quantcut(m2$Ranking, 5)
table(quantiles)
table(quantiles, m2$`Income Group`)
