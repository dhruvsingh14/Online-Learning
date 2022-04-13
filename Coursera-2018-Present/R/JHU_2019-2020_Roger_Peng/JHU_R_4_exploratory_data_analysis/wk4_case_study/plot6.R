library(ggplot2)
library(ggthemes)

# setting data directory
getwd()
dir <- getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/InProgress/R_4_exploratory_data_analysis/wk4_case_study/exdata_data_NEI_data")

# plot 6: motor vehicles
x <- readRDS("summarySCC_PM25.rds")
y <- readRDS("Source_Classification_Code.rds")

# checking var types
str(x)
summary(x)

# subsetting data to baltimore city and los angeles
x_sub <- subset(x, fips == "24510" | fips == "06037")

# using on-road as vehicle 
x_sub <- x_sub[x_sub$type == "ON-ROAD",]

# collapsing to totals by year and area
ag <- aggregate(Emissions~year+fips, data = x_sub, FUN = sum)

# plotting motor emissions trends comparison
g <- ggplot(ag, aes(year, Emissions, color = fips))
g + geom_point(size = 3, shape = 22, color = "red", stroke = 2, fill = "gray") + geom_line(size = 1.25, color = "darkblue") + 
  xlab("Emissions") + ylab("Year") + ggtitle("LA vs Ba.: Motor Emissions Trends")  + 
  theme_stata() + facet_wrap(~fips)

# resetting dir to script branch
setwd(dir)

# saving it to png
dev.copy(png, file = "plot6.png", width = 480, height = 480)
dev.off()

# LA sees greater changes in motor vehicle emissions over time