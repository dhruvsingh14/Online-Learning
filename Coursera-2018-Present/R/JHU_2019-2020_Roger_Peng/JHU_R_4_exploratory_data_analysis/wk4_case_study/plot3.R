# install.packages('ggthemes', repos='http://cran.us.r-project.org')

library(ggplot2)
library(ggthemes)

# setting data directory
getwd()
dir <- getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/InProgress/R_4_exploratory_data_analysis/wk4_case_study/exdata_data_NEI_data")

# plot 3: total emmissions trends in baltimore, md by emmission type
x <- readRDS("summarySCC_PM25.rds")
y <- readRDS("Source_Classification_Code.rds")

# checking var types
str(x)
summary(x)

# subsetting data to baltimore, md
x_sub <- subset(x, fips == "24510")

# collapsing to totals by year and type
ag <- aggregate(Emissions~year+type, data = x_sub, FUN = sum)

# plotting emissions totals in baltimore, md by type
g <- ggplot(ag, aes(year, Emissions, color = type))
g + geom_point(size = 2.5) + geom_line(size = 1.25) + 
  xlab("Emissions") + ylab("Year") + ggtitle("Emissions by Type")  + 
  theme_wsj()

# resetting dir to script branch
setwd(dir)

# saving it to png
dev.copy(png, file = "plot3.png", width = 480, height = 480)
dev.off()

# all emissions types decrease except point emissions