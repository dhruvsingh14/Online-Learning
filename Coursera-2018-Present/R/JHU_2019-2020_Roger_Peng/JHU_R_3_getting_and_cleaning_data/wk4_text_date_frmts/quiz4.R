# quiz 4

getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_3_data_cleaning/wk4_text_date_frmts")

# install.packages('httr', repos='http://cran.us.r-project.org')
# install.packages('sqldf', repos='http://cran.us.r-project.org')
# install.packages('RMySQL', repos='http://cran.us.r-project.org')
# install.packages('curl', repos='http://cran.us.r-project.org')
# install.packages('jpeg', repos='http://cran.us.r-project.org')
# install.packages('gtools', repos='http://cran.us.r-project.org')
# install.packages('quantmod', repos='http://cran.us.r-project.org')
# install.packages('lubridate', repos='http://cran.us.r-project.org')

library(httr)
library(sqldf)
library(curl)
library(data.table)
library(jpeg)
library(gtools)
library(quantmod)
library(lubridate)

######
# q1 #
######

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileUrl, destfile="Idaho_acs.csv", method="curl")
Idaho_acs <- fread("Idaho_acs.csv")

names_vec <- names(Idaho_acs)

names_split <- strsplit(names_vec, "wgtp")
names_split[123]

######
# q2 #
######

# downloading gdp csv file
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
download.file(fileUrl, destfile="gdp.csv", method="curl")

# reading in gdp
gdp <- fread("gdp.csv", skip = 3, header = T)
gdp <- gdp[c(-1), ]

names(gdp)[5] <- "GDP"
gdp$GDP <- gsub(",", "", gdp$GDP)
gdp$GDP <- as.numeric(gdp$GDP)
gdp$Ranking <- as.numeric(gdp$Ranking)

gdp_vect <- gdp$GDP[!is.na(gdp$Ranking)]


mean(gdp_vect)


######
# q3 #
######

# ^ acts as an anchor for position
grep("^United",gdp$Economy)

?grep


######
# q4 #
######

# downloading gdp csv file
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv"
download.file(fileUrl, destfile="gdp.csv", method="curl")

# reading in gdp
gdp <- fread("gdp.csv", skip = 3, header = T)
gdp <- gdp[c(-1), ]

names(gdp)[1] <- "CountryCode"
names(gdp)[5] <- "GDP"
gdp$GDP <- gsub(",", "", gdp$GDP)
gdp$GDP <- as.numeric(gdp$GDP)
gdp$Ranking <- as.numeric(gdp$Ranking)

gdp <- gdp[!is.na(gdp$Ranking)]


# downloading educ csv file
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv"
download.file(fileUrl, destfile="educ.csv", method="curl")

# reading in educ
educ <- fread("educ.csv")

m1 <- merge(gdp, educ, by = "CountryCode")

fisc_var <- grepl("June", m1$`Special Notes`)
sum(fisc_var)

fisc_df <- m1[grep("Fiscal year end: June 30", m1$`Special Notes`)]


######
# q5 #
######

# downloading data on amazon's stock price
amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn)

amzn <- as.data.frame(amzn)


setDT(amzn, keep.rownames = TRUE)[]

amzn$year <- year(amzn$rn)
amzn$day <- wday(amzn$rn)

summary(amzn[year == 2012])
summary(amzn[year == 2012 & day == 2])

?lubridate
?wday
