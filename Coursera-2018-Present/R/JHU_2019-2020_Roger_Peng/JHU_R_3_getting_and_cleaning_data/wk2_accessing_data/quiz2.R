# quiz 2

getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_3_data_cleaning/wk2_accessing_data")


# install.packages('httr', repos='http://cran.us.r-project.org')
# install.packages('sqldf', repos='http://cran.us.r-project.org')
# install.packages('RMySQL', repos='http://cran.us.r-project.org')
# install.packages('curl', repos='http://cran.us.r-project.org')

library(httr)
library(sqldf)
library(RMySQL)
library(curl)
library(data.table)

######
# q1 #
######
myapp <- oauth_app("github",
                   key = "bf31d6736dab3d8c6e3a",
                   secret = "b7e1cf8e0e5ca186507fdf67492cfd3cd9e5d86f"
)

myapp = oauth_app()

# skipping for now

######
# q2 #
######

if (!file.exists("data")) {
  dir.create("data")
}

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(fileUrl, destfile="acs.csv", method="curl")
acs <- fread("acs.csv")

sqldf("select pwgtp1 from acs where AGEP < 50")

######
# q3 #
######

unique(acs$AGEP)
sqldf("select distinct AGEP from acs")

######
# q4 #
######

con = url("http://biostat.jhsph.edu/~jleek/contact.html")
htmlCode = readLines(con)
close(con)

htmlCode

nchar(htmlCode[10])
nchar(htmlCode[20])
nchar(htmlCode[30])
nchar(htmlCode[100])


######
# q5 #
######

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for"
download.file(fileUrl, destfile="fixed_width.for", method="curl")
fwf <- read.fwf("fixed_width.for", widths = c(10, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4))

?read.fwf

col4 <- fwf[(5:nrow(fwf)), 6]

col4 <- as.character(col4)
col4 <- as.numeric(col4)

head(col4)
tail(col4)
dim(col4)

sum(col4)

# return to input correct answer before final course submission
# 32426.7
