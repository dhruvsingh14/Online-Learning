getwd()

# install.packages("swirl")
# packageVersion("swirl")

library(swirl)
# install_from_swirl("Getting and Cleaning Data")
swirl()

#########################################
#     lubridate swirl course            #
#########################################

Sys.getlocale("LC_TIME")

library(lubridate)

help(package = lubridate)

# stores todays date
this_day <- today()
this_day

# extracts year from date variable
year(this_day)

# extracts day of the week 
wday(this_day)
wday(this_day, label = TRUE)

this_moment <- now()
this_moment

minute(this_moment)

# parsing date using ymd adds time component beneath the surface
my_date <- ymd("1989-05-17")
my_date
class(my_date)

ymd("1989 May 17")

# use mdy to parse month day year ordering
mdy("March 12, 1975")

# numeric form of dd mm yyyy
dmy(25081985)

ymd("1920-1-2")

dt1
# parsing date time
ymd_hms(dt1)

# parsing time
hms("03:22:14")

dt2

# parsing a vector of dates
ymd(dt2)

update(this_moment, hours = 8, minutes = 34, seconds = 55)
this_moment

this_moment <- update(this_moment, hours = 20, minutes = 50)
this_moment

## itinerary exercise
nyc <- now("America/New_York")
nyc

depart <- nyc + days(2)
depart

depart <- update(depart, hours = 17, minutes = 34)
depart

arrive <- depart + hours(15) + minutes(50)

?with_tz
arrive <- with_tz(arrive, "Asia/Hong_Kong")
arrive

last_time <- mdy("June 17, 2008", tz = "Singapore")
last_time

?interval
how_long <- interval(last_time, arrive)

as.period(how_long)


