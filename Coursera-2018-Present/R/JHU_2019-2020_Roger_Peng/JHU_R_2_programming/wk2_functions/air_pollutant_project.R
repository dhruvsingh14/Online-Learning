getwd()

############################
## solution part 1 of 3: ###
############################

# writing a function to calculate the mean of specified columns, for specified files
# method: using loops to read in files and complete.cases: this one works

specdata <- "C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_2/wk2/rprog_data_specdata/specdata"
data <- list.files(specdata)
d <- data.frame(matrix(ncol = 4, nrow = 0))

pollutantmean <- function(directory, pollutant, id = 1:332){
  for (i in id){
    dt <- read.csv(paste(specdata, "/",data[i], sep = ''))
    d <- rbind(d, dt)
  }
  good <- complete.cases(d)
  if (pollutant == "sulfate") {
    d_comp <- d[good, ][,2]
  }
  if (pollutant == "nitrate") {
    d_comp <- d[good, ][,3]
  }
  mean <- mean(d_comp)
  mean
}

# testing function
pollutantmean(specdata, "sulfate", 1:10)
pollutantmean(specdata, "nitrate", 70:72)



############################
## solution part 2 of 3: ###
############################

# function for reporting number of complete observations per file

specdata <- "C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_2/wk2/rprog_data_specdata/specdata"
data <- list.files(specdata)
d <- data.frame(matrix(ncol = 4, nrow = 0))

complete <- function(directory, id= 1:332) {
  for (i in id){
    dt <- read.csv(paste(specdata, "/",data[i], sep = ''))
    d <- rbind(d, dt)
  }
  good <- complete.cases(d)
  d_comp <- d[good, ][,]
  d_comp$nobs <- 1 
  aggregate(nobs ~ ID, data = d_comp, FUN = sum)
}



############################
## solution part 3 of 3: ###
############################

# running tests:

specdata <- "C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_2/wk2/rprog_data_specdata/specdata"
data <- list.files(specdata)
d <- data.frame(matrix(ncol = 4, nrow = 0))

# func for dataframe with observations per id
obs_func <- function(directory, id = 1:332) {
  for (i in id){
    dt <- read.csv(paste(specdata, "/",data[i], sep = ''))
    d <- rbind(d, dt)
  }
  good <- complete.cases(d)
  d_comp <- d[good, ][,]
  d_comp$nobs <- 1 
  aggregate(nobs ~ ID, data = d_comp, FUN = sum)
}
x_obs <- obs_func(specdata, id=1:length(data))

corr <- function(directory, threshold = 0){
  # applying threshold criteria to df with obs
  x_thresh <- subset(x_obs, nobs > threshold)
  
  # get vector id's from subset using threshold
  id_vect <- x_thresh$ID
  
  # using id vector to read in appropriate files, append
  concat <- function(directory, id = 1:332) {
    for (i in id){
      dt <- read.csv(paste(specdata, "/",data[i], sep = ''))
      d <- rbind(d, dt)
    }
    good <- complete.cases(d)
    d_comp <- d[good, ][,]
  }
  x <- concat(specdata, id_vect)
  # using threshold appended files to calc corr per id
  cor_vect <- 0
  for(i in id_vect){
    id_cor <- subset(x, ID == i) 
    x_cor <- cor(id_cor$sulfate, id_cor$nitrate)
    cor_vect <- c(cor_vect, x_cor)
  }
  # output vector of corrs
  cor_vect <- cor_vect[-c(1)]
  cor_vect
}


cr <- corr(specdata, 150)
head(cr)

## [1] -0.01895754 -0.14051254 -0.04389737 -0.06815956 -0.12350667 -0.07588814

summary(cr)
## Min.  1st Qu.   Median     Mean  3rd Qu.     Max. 
## -0.21057 -0.04999  0.09463  0.12525  0.26844  0.76313 


cr <- corr(specdata, 400)
head(cr)
## [1] -0.01895754 -0.04389737 -0.06815956 -0.07588814  0.76312884 -0.15782860

summary(cr)
##  Min.  1st Qu.   Median     Mean  3rd Qu.     Max.
## -0.17623 -0.03109  0.10021  0.13969  0.26849  0.76313

cr <- corr(specdata, 5000)
summary(cr)
## Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##



