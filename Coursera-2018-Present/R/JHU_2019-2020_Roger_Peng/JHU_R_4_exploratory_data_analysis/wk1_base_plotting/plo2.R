library(lubridate)

getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_4_exploratory_data_analysis/wk1_base_plotting")


# reading in entire dataset
x <- read.delim("meter_subset.txt", header = TRUE, sep = "", dec = ".")

# converting read in factors to date time
x$date_time <- ymd_hms(x$date_time)
x$date_time <- as.POSIXct(x$date_time)

# rendering plot
plot(x$date_time, x$Global_active_power,
     type = "l", 
     xlab = "", 
     ylab = "Global Active Power (kilowatts)")

# saving it to png
dev.copy(png, file = "plot2.png", width = 480, height = 480)
dev.off()
