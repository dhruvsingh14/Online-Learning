library(lubridate)

getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_4_exploratory_data_analysis/wk1_base_plotting")


# reading in entire dataset
x <- read.delim("meter_subset.txt", header = TRUE, sep = "", dec = ".")

# converting read in factors to date time
x$date_time <- ymd_hms(x$date_time)
x$date_time <- as.POSIXct(x$date_time)

# window for 4 plots
par(mfrow = c(2, 2))

# plot1
plot(x$date_time, x$Global_active_power,
     type = "l", 
     xlab = "", 
     ylab = "Global Active Power (kilowatts)")

# plot2
plot(x$date_time, x$Voltage,
     type = "l", 
     xlab = "datetime", 
     ylab = "Voltage")

# plot3
plot(x$date_time, x$Sub_metering_1,
     type = "l",
     xlab = "", 
     ylab = "Energy sub metering")
lines(x$date_time, x$Sub_metering_2, col = "red", type = "l")
lines(x$date_time, x$Sub_metering_3, col = "blue", type = "l")
legend("topright", lty = 1, col = c("black", "red", "blue"), legend = c("Sub_metering_1", "Sub_metering_2", "Sub_metering_3"))

# plot4
plot(x$date_time, x$Global_reactive_power,
     type = "l", 
     xlab = "datetime", 
     ylab = "Global_reactive_power")

# saving it to png
dev.copy(png, file = "plot4.png", width = 480, height = 480)
dev.off()
