library(ggplot2)
library(ggthemes)

# setting data directory
getwd()
dir <- getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/InProgress/R_4_exploratory_data_analysis/wk4_case_study/exdata_data_NEI_data")

# plot 4: coal
x <- readRDS("summarySCC_PM25.rds")
y <- readRDS("Source_Classification_Code.rds")

# checking var types
str(x)
summary(x)

# checking coal emissions types
summary(grep("coal", y$Short.Name))
summary(grep("coal", y$SCC.Level.Three))


# subsetting columns
x <- x[c("SCC", "Emissions", "year")]
y <- y[c("SCC", "Short.Name", "SCC.Level.Three")]

# subsetting to labels capturing coal caused pollution
y_coal <- y[grepl("Coal", y$Short.Name)|grepl("coal", y$Short.Name)|grepl("Coal", y$SCC.Level.Three)|grepl("coal", y$SCC.Level.Three),]

# merging emissions for rows caused by coal
mrg <- merge(x, y_coal, by = "SCC", all.y = TRUE)

# collapsing to totals by year and type
ag <- aggregate(Emissions~year, data = mrg, FUN = sum)

# plotting coal emissions trends
g <- ggplot(ag, aes(year, Emissions))
g + geom_point(size = 3, color = "black") + geom_line(size = 1.25, color = "gray") + 
  xlab("Emissions") + ylab("Year") + ggtitle("Coal Emissions Trends")  + 
  theme_economist() + scale_color_economist()

# resetting dir to script branch
setwd(dir)

# saving it to png
dev.copy(png, file = "plot4.png", width = 480, height = 480)
dev.off()

# coal emissions drop over time