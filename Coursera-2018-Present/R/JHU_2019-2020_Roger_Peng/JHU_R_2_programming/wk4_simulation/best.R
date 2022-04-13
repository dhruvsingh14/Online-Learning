setwd("C:/Users/dhnsingh/Dropbox/Misc/Coursera/R_2_r_programming/wk4_simulation/rprog_data_ProgAssignment3-data")

# writing a function to find best hospital in a state
best <- function(state, outcome){
  ## reading outcome data
  outcomeData <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
  if (!(state %in% outcomeData$State)){
    x = "invalid state"
    x
  } else {
    outcomeData2 <- subset(outcomeData, State == state)
    
    outcomeData2 <- outcomeData2[c(2, 11, 17, 23)]
    names(outcomeData2) <- c("hospital", "heart attack", "heart failure", "pneumonia")
    
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
