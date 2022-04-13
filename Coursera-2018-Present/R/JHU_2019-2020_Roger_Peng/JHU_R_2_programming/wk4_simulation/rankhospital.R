setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_2_r_programming/wk4_simulation/rprog_data_ProgAssignment3-data")

# writing a function to return hospital name by mortality rank for given outcome

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
