getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_3_data_cleaning/wk1_getting_data/data")

# install.packages("swirl")
# install.packages("xlsx")
# install.packages("XML")
# install.packages("curl")
# install.packages("data.table")

# packageVersion("swirl")

# library(swirl)
library(xlsx)
library(XML)
library(curl)
library(data.table)

# install_from_swirl("Getting and Cleaning Data")
# swirl()

# week 1 quiz

# q1: reading csv
if (!file.exists("data")) {
  dir.create("data")
}

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileurl, destfile = "./data/acs.csv", method = "curl")
list.files("data")

acs <- read.csv("./data/acs.csv")
summary(acs$VAL == 24)

# q2
# guessed

# q3: reading xlsx, with rows subsetted
dat <- read.xlsx("getdata_data_DATA.gov_NGAP.xlsx", sheetIndex = 1, 
                 rowIndex = 18:23, colIndex = 7:15, header = TRUE)

sum(dat$Zip*dat$Ext, na.rm = T)

# q4: reading xml
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"

download.file(fileUrl, "restaurants.xml", method="curl")
doc <- xmlTreeParse(destfile, useInternalNodes=TRUE)
rootNode <- xmlRoot(doc)

# solution copied from elsewhere, must master download methods using curl
zipcodes <- xpathSApply(rootNode, "//zipcode", xmlValue)
length(which(zipcodes==21231))

# q5: downloading files using url
fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(fileUrl, destfile="Idaho_acs.csv", method="curl")
DT <- fread("Idaho_acs.csv")

?fread

# q6 
guessing
