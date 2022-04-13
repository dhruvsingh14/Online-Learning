getwd()

# q8
source("rankall.R")

# testing
# head(rankall("heart attack", 20), 10)

r <- rankall("heart attack", 4)
as.character(subset(r, state == "HI")$hospital)

# q9
r <- rankall("pneumonia", "worst")
as.character(subset(r, state == "NJ")$hospital)

# q10
r <- rankall("heart failure", 10)
as.character(subset(r, state == "NV")$hospital)
