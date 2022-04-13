library(dplyr)

getwd()
setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_3_data_cleaning/wk4_text_date_frmts/getdata_projectfiles_UCI HAR Dataset/UCI HAR Dataset")

dir <- getwd()

# reading in test directory
x <- list.files(pattern = ".txt$", recursive = TRUE)

# reading in relevant data sets, subsetted
x_subs <- c(x[1:2], x[15:16], x[27:28])

for (i in 1:length(x_subs)) {
  if (1 <= i & i <= 2) {
    y <- strsplit(x_subs[i], ".txt")
    y <- y[[1]][1]
  } else {
    y <- strsplit(x_subs[i], "/")
    y <- y[[1]][2]
    y <- strsplit(y, ".txt")
    y <- y[[1]][1]
  }
  assign(y, read.delim(paste(dir, x_subs[i], sep = "/"), header = FALSE, sep = "", dec = "."))
}
rm(x, x_subs, y, dir, i)

# preparing to combine main test and training sets

# naming columns using features data frame
names_vec <- as.character(features[,2])
rm(features)

# cleaning names
names_vec <- gsub("\\()-", "", names_vec)
names_vec <- gsub("\\()", "", names_vec)
names_vec <- gsub("-", "_", names_train)

# assigning varnames
names(X_train) <- names_vec
names(X_test) <- names_vec

# subsetting to mean and std dev columns
mean <- grepl("mean", names_vec)
std <- grepl("std", names_vec)
rm(names_vec)

sum(mean) # 46 columns
sum(std) # 33 columns

# subsetting to mean std vars using logical
train_subs <- X_train[std | mean]
test_subs <- X_test[std | mean]
rm(X_train, X_test, std, mean)

# binding test and training sets to activity identifiers
train_set <- cbind(y_train, train_subs)
test_set <- cbind(y_test, test_subs)
rm(y_train, y_test, train_subs, test_subs)

# converting num id to char
train_set$V1 <- as.character(train_set$V1)
test_set$V1 <- as.character(test_set$V1)
activity_labels$V1 <- as.character(activity_labels$V1)

# merging
m1 <- merge(x = activity_labels, y = train_set, by = 'V1')
m2 <- merge(x = activity_labels, y = test_set, by = 'V1')
rm(train_set, test_set, activity_labels)

# dropping num id col
m1 <- m1[-c(1)]
m2 <- m2[-c(1)]

# renaming id col
names(m1)[1] <- "activity"
names(m2)[1] <- "activity"

# merging
m3 <- rbind(m1, m2)
  

# summarizing means by activity group
x <- aggregate(. ~ activity, data = m3, mean)
write.table(x, 'clean_table.txt', row.names = FALSE)

?write.table
