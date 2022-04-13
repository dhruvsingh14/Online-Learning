# setting data directory
getwd()
dir <- getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/InProgress/R_4_exploratory_data_analysis/wk4_case_study/exdata_data_NEI_data")

# plot 1: total emmissions trends 
x <- readRDS("summarySCC_PM25.rds")
y <- readRDS("Source_Classification_Code.rds")

# checking var types
str(x)
summary(x)

# collapsing to totals by year
ag <- aggregate(Emissions~year, data = x, FUN = sum)

# plotting totals
par(bg = "yellow")
plot(ag$year, ag$Emissions, cex = 3, pch = 18, col = "darkgreen",
     main = "Total Emissions over Time", 
     xlab = "Total Emissions", ylab = "Year")
lines(ag$year, ag$Emissions, col = "red", lwd = 2)

# resetting dir to script branch
setwd(dir)

# saving it to png
dev.copy(png, file = "plot1.png", width = 480, height = 480)
dev.off()

# trend shows total emissions decrease over time
