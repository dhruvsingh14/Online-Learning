# setting data directory
getwd()
dir <- getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/InProgress/R_4_exploratory_data_analysis/wk4_case_study/exdata_data_NEI_data")

# plot 2: total emmissions trends in baltimore, md 
x <- readRDS("summarySCC_PM25.rds")
y <- readRDS("Source_Classification_Code.rds")

# checking var types
str(x)
summary(x)

# subsetting data to baltimore, md
x_sub <- subset(x, fips == "24510")

# collapsing to totals by year 
ag <- aggregate(Emissions~year, data = x_sub, FUN = sum)

# plotting emissions totals in baltimore, md
par(bg = "lightblue")
plot(ag$year, ag$Emissions, cex = 3, pch = 18, col = "maroon",
     main = "Baltimore: Total Emissions over Time", 
     xlab = "Total Emissions", ylab = "Year")
lines(ag$year, ag$Emissions, col = "white", lwd = 2)

# resetting dir to script branch
setwd(dir)

# saving it to png
dev.copy(png, file = "plot2.png", width = 480, height = 480)
dev.off()

# trend shows total emissions decrease over time