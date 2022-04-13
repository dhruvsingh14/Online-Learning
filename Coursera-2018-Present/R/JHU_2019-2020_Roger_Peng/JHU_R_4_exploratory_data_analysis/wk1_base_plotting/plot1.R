getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_4_exploratory_data_analysis/wk1_base_plotting")


# reading in entire dataset
x <- read.delim("meter_subset.txt", header = TRUE, sep = "", dec = ".")

# rendering plot
hist(x$Global_active_power, col = "red", xlab = "Global Active Power (kilowatts)", main = "Global Active Power")

# saving it to png
dev.copy(png, file = "plot1.png", width = 480, height = 480)
dev.off()
