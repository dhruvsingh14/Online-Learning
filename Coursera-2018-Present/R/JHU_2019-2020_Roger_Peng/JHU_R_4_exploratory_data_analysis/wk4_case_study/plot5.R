library(ggplot2)
library(ggthemes)

# setting data directory
getwd()
dir <- getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/InProgress/R_4_exploratory_data_analysis/wk4_case_study/exdata_data_NEI_data")

# plot 5: motor vehicles
x <- readRDS("summarySCC_PM25.rds")
y <- readRDS("Source_Classification_Code.rds")

# checking var types
str(x)
summary(x)

# subsetting data to baltimore, md
x_sub <- subset(x, fips == "24510")

# using on-road as vehicle 
x_sub <- x_sub[x_sub$type == "ON-ROAD",]

# collapsing to totals by year
ag <- aggregate(Emissions~year, data = x_sub, FUN = sum)

# plotting motor emissions trends
g <- ggplot(ag, aes(year, Emissions))
g + geom_point(size = 3, shape = 22, color = "red", stroke = 2, fill = "gray") + geom_line(size = 1.25, color = "darkblue") + 
  xlab("Emissions") + ylab("Year") + ggtitle("Baltimore: Motor Emissions Trends")  + 
  theme_stata()

# resetting dir to script branch
setwd(dir)

# saving it to png
dev.copy(png, file = "plot5.png", width = 480, height = 480)
dev.off()

# motor emissions in baltimore city drop over time