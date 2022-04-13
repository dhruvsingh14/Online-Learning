getwd()

# install.packages("swirl")
# packageVersion("swirl")

library(swirl)

swirl()


boring_function <- function(x) {
  x
}

my_mean <- function(my_vector) {
  sum(my_vector)/length(my_vector)
  # Remember: the last expression evaluated will be returned! 
}

remainder <- function(num, divisor=2) {
  num %% divisor
  # Remember: the last expression evaluated will be returned! 
}

evaluate <- function(func, dat){
  func(dat)
  # Remember: the last expression evaluated will be returned! 
}

telegram <- function(...){
  paste ("START", ..., "STOP", sep = " ", collapse = NULL)
}

mad_libs <- function(...){
  args <- list(...)
  place <- args[["place"]]
  adjective <- args[["adjective"]]
  noun <- args[["noun"]]
  # Don't modify any code below this comment.
  # Notice the variables you'll need to create in order for the code below to
  # be functional!
  paste("News from", place, "today where", adjective, "students took to the streets in protest of the new", noun, "being installed on campus.")
}

"%p%" <- function(...){ # Remember to add arguments!
  paste(..., sep = " ", collapse = NULL)
}


# quiz 2 week 2

# q1
cube <- function(x, n) {
  x^3
}

cube(3)

# q2
x <- 1:10
if(x > 5) {
  x <- 0
}

# q3 
f <- function(x) {
  g <- function(y) {
    y + z
  }
  z <- 4
  x + g(x)
}

z <- 10
f(3)


# q4
x <- 5
y <- if(x < 3) {
  NA
} else {
  10
}


# q5
h <- function(x, y = NULL, d = 3L) {
  z <- cbind(x, d)
  if(!is.null(y))
    z <- z + y
  else
    z <- z + f
  g <- x + y / z
  if(d == 3L)
    return(g)
  g <- g + 10
  g
}
