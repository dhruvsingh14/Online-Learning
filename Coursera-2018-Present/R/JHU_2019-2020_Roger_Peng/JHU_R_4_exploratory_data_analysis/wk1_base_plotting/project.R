library(lubridate)
library(dplyr)


getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_4_exploratory_data_analysis/wk1_base_plotting/exdata_data_household_power_consumption")


x <- read.delim("household_power_consumption.txt", header = TRUE, sep = ";", dec = ".")

# # calculating memory reqd.
# # first in bytes, assuming 8 bytes per cell
# 2075259 * 9 * 8 
# # then in bytes/MB
# 2075259 * 9 * 8 / 2^{20}
# # MB
# round(2075259 * 9 * 8 / 2^{20}, 2)
# # GB
# round(2075259 * 9 * 8 / 2^{20} / 2014, 2)
# # roughly 0.07 GB

# preparing the data

# converting date column
x$Date <- dmy(x$Date)
str(x)

# checking missing values in date
summary(x$Date)

# subsetting using date, to the 1st and 2nd of Feb, in 2007 
x2 <- subset(x, x$Date >= "2007-02-01" & x$Date <= "2007-02-02")
  
# converting columns
x2$Time <- as.character(x2$Time)
str(x2)

# date time columns
x2$date_time <- paste(x2$Date, x2$Time)
x2$date_time <- ymd_hms(x2$date_time)
x2$date_time <- as.POSIXct(x2$date_time)

# converting time
x2$Time <- hms(x2$Time)

# converting central columns to numeric
x3 <- data.frame(lapply(x2, as.character), stringsAsFactors = FALSE)
x3[,3:8] <- sapply(x3[,3:8], as.numeric)

# changing directory
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_4_exploratory_data_analysis/wk1_base_plotting")

# writing out data in txt format
write.table(x3, 'meter_subset.txt', row.names = FALSE)
