getwd()

setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_2_r_programming/wk4_simulation/rprog_data_ProgAssignment3-data")

outcome <- read.csv("outcome-of-care-measures.csv", colClasses = "character")

head(outcome)

# checking number of rows
nrow(outcome)
ncol(outcome)

# listing col names
names(outcome)

# plotting death rates from heart attack
outcome[,11] <- as.numeric(outcome[,11])
hist(outcome[,11])

###########
# Part II #
###########

# writing a function to find best hospital in a state
best <- function(state, outcome){
  ## reading outcome data
  outcomeData <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  options(warn=-1)
  
  # checking if state is valid
  if (!(state %in% outcomeData$State)){
    x = "invalid state"
    x
  } else {
    outcomeData2 <- subset(outcomeData, State == state)
    
    outcomeData2 <- outcomeData2[c(2, 11, 17, 23)]
    names(outcomeData2) <- c("hospital", "heart attack", "heart failure", "pneumonia")
    
    # checking if outcome is valid
    if (!(outcome %in% names(outcomeData2))){
      x2 = "invalid outcome"
      x2
    } else {
      outcomeData2[,2] <- as.numeric(outcomeData2[,2])
      outcomeData2[,3] <- as.numeric(outcomeData2[,3])
      outcomeData2[,4] <- as.numeric(outcomeData2[,4])
      
      if (outcome == "heart attack") {
        outcomeData2 <- outcomeData2[order(outcomeData2[,2]),]
      } 
      if (outcome == "heart failure") {
        outcomeData2 <- outcomeData2[order(outcomeData2[,3]),]
      } 
      if (outcome == "pneumonia") {
        outcomeData2 <- outcomeData2[order(outcomeData2[,4]),]
      } 
      
      outcomeData2[1,1]
      
    }
    
  }
  
}

best("AL", "pneumonia")
best("TX", "heart attack")
best("TX", "heart failure")
best("MD", "heart attack")
best("MD", "pneumonia")
best("BB", "heart attack")
best("NY", "hert attack")

# works!

# quiz responses below

best("SC", "heart attack")
best("NY", "pneumonia")
best("AK", "pneumonia")



############
# Part III #
############


state = "MD"
outcome = "heart attack"
num = "worst"

rm(state, outcome, num)

rankhospital <- function(state, outcome, num = "best") {
  ## reading outcome data
  outcomeData <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  # suppressing NAs coercion message
  options(warn=-1)
  
  ## Check that state and outcome are valid
  if (!(state %in% outcomeData$State)){
    stop("invalid state")
  } else {
    # subsetting data by entered
    outcomeData2 <- subset(outcomeData, State == state)
    
    # subsetting data by 30 day mortality rates for outcomes
    outcomeData2 <- outcomeData2[c(2, 11, 17, 23)]
    names(outcomeData2) <- c("hospital", "heart attack", "heart failure", "pneumonia")
    
    # checking if outcome is valid
    if (!(outcome %in% names(outcomeData2))){
      stop("invalid outcome")
    } else {
      # converting char columns to numeric
      outcomeData2[,2] <- as.numeric(outcomeData2[,2])
      outcomeData2[,3] <- as.numeric(outcomeData2[,3])
      outcomeData2[,4] <- as.numeric(outcomeData2[,4])
      
      if (outcome == "heart attack") {
        # subsetting by outcome
        outcomeData2 <- outcomeData2[c(1, 2)]
        # ordering by outcome and name
        outcomeData2 <- outcomeData2[order(outcomeData2[,2], outcomeData2[,1]),]
        # subsetting to exlude rows with na
        outcomeData2 <- subset(outcomeData2, !is.na(outcomeData2[,2]))
        # adding index column to rank
        outcomeData2$rank <- seq.int(nrow(outcomeData2))
      } 
      if (outcome == "heart failure") {
        outcomeData2 <- outcomeData2[c(1, 3)]
        outcomeData2 <- outcomeData2[order(outcomeData2[,2], outcomeData2[,1]),]
        outcomeData2 <- subset(outcomeData2, !is.na(outcomeData2[,2]))
        outcomeData2$rank <- seq.int(nrow(outcomeData2))
      } 
      if (outcome == "pneumonia") {
        outcomeData2 <- outcomeData2[c(1, 4)]
        outcomeData2 <- outcomeData2[order(outcomeData2[,2], outcomeData2[,1]),]
        outcomeData2 <- subset(outcomeData2, !is.na(outcomeData2[,2]))
        outcomeData2$rank <- seq.int(nrow(outcomeData2))
      } 
      
      # giving final print command for requested name
      if (num == "best") {
        outcomeData2[1,1]
      } else
      if (num == "worst") {
        outcomeData2[nrow(outcomeData2), 1]
      } else
      if (num > nrow(outcomeData2)) {
        x <- "NA"
        x
      } else {
        x <- as.numeric(num)
        outcomeData2[x,1]
      }
      
    }
    
  }
  
}

rankhospital("TX", "heart failure", 4)
rankhospital("MD", "heart attack", "worst")
rankhospital("MN", "heart attack", 5000)

# the following are quiz responses
rankhospital("NC", "heart attack", "worst")
rankhospital("WA", "heart attack", 7)
rankhospital("TX", "pneumonia", 10)
rankhospital("NY", "heart attack", 7)




############
# Part IV #
############

outcome = "heart failure"
num = "best"

rm(outcome, num)


rankall <- function(outcome, num = "best") {
  ## reading outcome data
  outcomeData <- read.csv("outcome-of-care-measures.csv", colClasses = "character")

  # suppressing NAs coercion message
  options(warn=-1)
  
  # subsetting data by 30 day mortality rates for outcomes
  outcomeData2 <- outcomeData[c(2, 7, 11, 17, 23)]
  names(outcomeData2) <- c("hospital", "state", "heart attack", "heart failure", "pneumonia")
  
  ## checking if outcome is valid
  if (!(outcome %in% names(outcomeData2))){
    stop("invalid outcome")
  } else {
    # converting char columns to numeric
    outcomeData2[,3] <- as.numeric(outcomeData2[,3])
    outcomeData2[,4] <- as.numeric(outcomeData2[,4])
    outcomeData2[,5] <- as.numeric(outcomeData2[,5])
    
    ## subsetting based on outcome to name, state, outcome
    if (outcome == "heart attack") {
      outcomeData2 <- outcomeData2[c(1, 2, 3)]
      # ordering by state, outcome, and name
      outcomeData2 <- outcomeData2[order(outcomeData2[,2], outcomeData2[,3], outcomeData2[,1]),]
      # subsetting to exlude rows with na
      outcomeData2 <- subset(outcomeData2, !is.na(outcomeData2[,3]))
      # adding index column to rank
      outcomeData2$state_rank <- ave(outcomeData2[,3], outcomeData2$state, FUN = seq_along)
    } 
    if (outcome == "heart failure") {
      outcomeData2 <- outcomeData2[c(1, 2, 4)]
      # working with only 3 columns at this point: name, state, outcome
      outcomeData2 <- outcomeData2[order(outcomeData2[,2], outcomeData2[,3], outcomeData2[,1]),]
      outcomeData2 <- subset(outcomeData2, !is.na(outcomeData2[,3]))
      outcomeData2$state_rank <- ave(outcomeData2[,3], outcomeData2$state, FUN = seq_along)
    } 
    if (outcome == "pneumonia") {
      outcomeData2 <- outcomeData2[c(1, 2, 5)]
      outcomeData2 <- outcomeData2[order(outcomeData2[,2], outcomeData2[,3], outcomeData2[,1]),]
      outcomeData2 <- subset(outcomeData2, !is.na(outcomeData2[3]))
      outcomeData2$state_rank <- ave(outcomeData2[,3], outcomeData2$state, FUN = seq_along)
    } 
    
    ## subsetting based on num value
    if (num == "best") {
      outcomeData_print <- subset(outcomeData2, state_rank == 1)
    } else
    if (num == "worst") {
      outcomeData3 <- aggregate(state_rank ~ state, data = outcomeData2, max)
      outcomeData_ranked <- merge(outcomeData2, outcomeData3, by = c("state", "state_rank"))
      outcomeData_print <- outcomeData_ranked[c(3, 1, 4, 2)]
    }
    else
    {
      # producing a count column for outcomes within each state
      outcomeData3 <- aggregate(state_rank ~ state, data = outcomeData2, max)
      names(outcomeData3)[2] <- "count"
      
      # attaching column to original data
      outcomeData_ranked <- merge(outcomeData2, outcomeData3, by = "state")
      
      for (i in 1:nrow(outcomeData_ranked)) {
        
        if (num > outcomeData_ranked$count[i]) {
          outcomeData_ranked$Rank[i] <- 0
          outcomeData_ranked$hospital[i] <- "NA"
        } else {
          outcomeData_ranked$Rank[i] <- outcomeData_ranked$state_rank[i]
        }
      }
      outcomeData_ranked <- outcomeData_ranked[c(2, 1, 3, 6)]
      names(outcomeData_ranked)[4] <- "state_rank"
    }
    
    ## outputting dataframe with hospital name and state name for numeric num input
    if (num != "best" & num != "worst") {
      outcomeData_print <- subset(outcomeData_ranked, state_rank == num | state_rank == 0)
      outcomeData_print <- aggregate(.~state+hospital, outcomeData_print, FUN = sum)
      outcomeData_print <- outcomeData_print[order(outcomeData_print[,1]),]
      
      for (i in 1:nrow(outcomeData_print)) {
        if (outcomeData_print$hospital[i] == "NA") {
          outcomeData_print$hospital[i] <- NA
          outcomeData_print$state_rank[i] <- NA
        }
      }
    }
    outcomeData_output <- outcomeData_print[c(2, 1)]
    row.names(outcomeData_output) <- NULL
    outcomeData_output
  }
}

head(rankall("heart attack", 20), 10)
tail(rankall("pneumonia", "worst"), 3)
tail(rankall("heart failure"), 10)

rankall("heart attack", 20) # checks out piecewise, good
rankall("pneumonia", "worst") # checks out piece wise, good!
rankall("heart failure")
