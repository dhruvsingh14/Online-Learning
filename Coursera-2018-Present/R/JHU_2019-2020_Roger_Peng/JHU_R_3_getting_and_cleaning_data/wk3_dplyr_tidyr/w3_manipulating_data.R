getwd()

# install.packages("swirl")
# packageVersion("swirl")

library(swirl)
# install_from_swirl("Getting and Cleaning Data")
swirl()

#########################################
# dplyr swirl course: manipulating data #
#########################################

mydf <- read.csv(path2csv, stringsAsFactors = FALSE)

dim(mydf)

head(mydf)

library(dplyr)

packageVersion("dplyr")

# working with a tibble
cran <- tbl_df(mydf)

rm("mydf")

cran
?select # subsets columns

select(cran, ip_id, package, country) # order specified determines order returned

5:20

select(cran, r_arch:country) # shorthand for selecting multiple consecutive columns
select(cran, country:r_arch)
cran

select(cran, -time) # omits columns

-5:20
-(5:20)

select(cran, -(X:size))

filter(cran, package == "swirl") # subsets rows
filter(cran, r_version == "3.1.1", country == "US") # filters like an 'and' condition

?Comparison

filter(cran, r_version <= "3.0.2", country == "IN")
filter(cran, country == "US" | country == "IN")
filter(cran, size > 100500, r_os == "linux-gnu")

is.na(c(3, 5, NA, 10)) # filtering by missing values
!is.na(c(3, 5, NA, 10)) 
filter(cran, !is.na(r_version))

cran2 <- select(cran, size:ip_id)
arrange(cran2, ip_id) # sorts observations in ascending or descending order 
arrange(cran2, desc(ip_id))
arrange(cran2, package, ip_id) # sorting on mutiple variables, starting from the left
arrange(cran2, country, desc(r_version), ip_id)

cran3 <- select(cran, ip_id, package, size)
cran3

mutate(cran3, size_mb = size / 2^20) # creating new column using existing one
mutate(cran3, size_mb = size / 2^20, size_gb = size_mb / 2^10)
mutate(cran3, correct_size = size + 1000)

summarize(cran, avg_bytes = mean(size)) # using summarize to collapse rows

##################################################
# dplyr swirl course: grouping and chaining data #
##################################################

library(dplyr)
cran <- tbl_df(mydf) # assigns df to tibble, for wider print functionality
rm("mydf")

cran # printing

# grouping by category
?group_by
by_package <- group_by(cran, package)
by_package

# very interesting, summary statistics by group
summarize(by_package, mean(size))

# forming summary stats table
pack_sum <- summarize(by_package,
                      count = n(),
                      unique = n_distinct(ip_id), # faster than unique command
                      countries = n_distinct(country),
                      avg_bytes = mean(size))

pack_sum

quantile(pack_sum$count, probs = 0.99) # determining 99th percentile value

top_counts <- filter(pack_sum, count > 679) # subsetting using filter, condition

top_counts
View(top_counts)

?arrange
?desc

top_counts_sorted <- arrange(top_counts, desc(count))
View(top_counts_sorted)

quantile(pack_sum$unique, probs = 0.99) # determining 99th percentile value
top_unique <- filter(pack_sum, unique > 465)

View(top_unique)
top_unique_sorted <- arrange(top_unique, desc(unique))
View(top_unique_sorted)

# really interesting example in embedding functions
# maybe its just the fomatting
result2 <-
  arrange(
    filter(
      summarize(
        group_by(cran,
                 package
        ),
        count = n(),
        unique = n_distinct(ip_id),
        countries = n_distinct(country),
        avg_bytes = mean(size)
      ),
      countries > 60
    ),
    desc(countries),
    avg_bytes
  )

print(result2)

# introducing chaining, key componenent of dplyr

# advantage: bypasses intermediary saving to objects

# chaining example:
result3 <-
  cran %>%
  group_by(package) %>%
  summarize(count = n(),
            unique = n_distinct(ip_id),
            countries = n_distinct(country),
            avg_bytes = mean(size)
  ) %>%
  filter(countries > 60) %>%
  arrange(desc(countries), avg_bytes)

# Print result to console
print(result3)

# read chaining operator as 'then'
View(result3)

# more chaining experience
cran %>%
  select(ip_id, country, package, size) %>%
  mutate(size_mb = size / 2^20) %>%
  filter(size_mb <= 0.5) %>%
  arrange(desc(size_mb)) %>%
  print()

####################################
# tidyr swirl course: tidying data #
####################################
library(tidyr)
3

students
?gather

gather(students, sex, count, -grade)

students2

# gathering multiple columns tracking the the same var
res <- gather(students2, sex_class, count, -grade)
res

?separate

# separating column into 2 vars
separate(data = res, col = sex_class, into = c("sex", "class"))

# example of chaining with wide to long, then separating
students2 %>%
  gather(sex_class, count, -grade) %>%
  separate(sex_class, c("sex", "class")) %>%
  print


students3

# gathering multiple columns into the key = class, value = grade columns
students3 %>%
  gather(class, grade, class1:class5 , na.rm = TRUE) %>%
  print


# 2-step gather all into a var column, then spread column by group
?spread
students3 %>%
  gather(class, grade, class1:class5, na.rm = TRUE) %>%
  spread(test, grade) %>%
  print

# using mutate and parse number to extract numeric portion of string
library(readr)
parse_number("class5")

students3 %>%
  gather(class, grade, class1:class5, na.rm = TRUE) %>%
  spread(test, grade) %>%
  mutate(class = parse_number(class)) %>%
  print

students4

# removing duplicate rows
student_info <- students4 %>%
  select(id, name, sex) %>%
  unique %>%
  print


passed
failed

passed <- passed %>% mutate(status = "passed")
failed <- failed %>% mutate(status = "failed")

bind_rows(passed, failed)

sat

## gathering all absolute scores by sex, and part
# creating columns for sum and proportion within range
sat %>%
  select(-contains("total")) %>%
  gather(part_sex, count, -score_range) %>%
  separate(part_sex, c("part", "sex")) %>%
  group_by(part, sex) %>%
  mutate(total = sum(count),
         prop = count / total
  ) %>% print
