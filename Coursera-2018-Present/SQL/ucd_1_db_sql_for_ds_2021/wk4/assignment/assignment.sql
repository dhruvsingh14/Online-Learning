-- Programmer: Dhruv Singh
-- Date Modified: 06/13/21
-- Title: Week 4: Assignment
-- Topic: Analyzing Yelp Data
-- DBMS: PostgreSQL

-- Part 1: total rows
select COUNT(*)
    from Attribute
select COUNT(*)
    from Business
select COUNT(*)
    from Category
select COUNT(*)
    from Checkin
select COUNT(*)
    from elite_years
select COUNT(*)
    from friend
select COUNT(*)
    from hours
select COUNT(*)
    from photo
select COUNT(*)
    from review
select COUNT(*)
    from tip
select COUNT(*)
    from user

-- Part 2: total distrinct rows
select COUNT(DISTINCT id)
    from Business
select COUNT(DISTINCT business_id)
    from Hours
select COUNT(DISTINCT business_id)
    from Category
select COUNT(DISTINCT business_id)
    from Attribute
select COUNT(DISTINCT id)
    from Review
select COUNT(DISTINCT business_id)
    from Checkin
select COUNT(DISTINCT id)
    from Photo
select COUNT(DISTINCT business_id)
    from Tip
select COUNT(DISTINCT id)
    from User
select COUNT(DISTINCT user_id)
    from Friend
select COUNT(DISTINCT user_id)
    from Elite_years

-- Part 3: Any nulls in User table
SELECT *
  FROM User
  WHERE id IS NULL OR
    name IS NULL OR
    review_count IS NULL OR
    yelping_since IS NULL OR
    useful IS NULL OR
    funny IS NULL OR
    cool IS NULL OR
    fans IS NULL OR
    average_stars IS NULL OR
    compliment_hot IS NULL OR
    compliment_more IS NULL OR
    compliment_profile IS NULL OR
    compliment_cute IS NULL OR
    compliment_list IS NULL OR
    compliment_note IS NULL OR
    compliment_plain IS NULL OR
    compliment_cool IS NULL OR
    compliment_funny IS NULL OR
    compliment_writer IS NULL OR
    compliment_photos

-- Part 4: Summary Stats
SELECT MIN(Stars), MAX(Stars), AVG(Stars)
  FROM Review

SELECT MIN(Stars), MAX(Stars), AVG(Stars)
  FROM Business

SELECT MIN(Likes), MAX(Likes), AVG(Likes)
  FROM Tip

SELECT MIN(Count), MAX(Count), AVG(Count)
  FROM Checkin

SELECT MIN(Review_count), MAX(Review_count), AVG(Review_count)
  FROM User

-- Part 5: most reviews by city
SELECT city, SUM(review_count) AS total_reviews
  FROM business
  GROUP BY city
  ORDER BY SUM(review_count) DESC

-- Part 6: i. ratings per city
SELECT stars, COUNT(stars) AS frequency
  FROM business
  WHERE city = 'Avon'
  GROUP BY stars

-- Part 6: ii. ratings per city
SELECT stars, COUNT(stars) AS frequency
  FROM business
  WHERE city = 'Beachwood'
  GROUP BY stars

-- Part 7: top 3 reviews
SELECT name, SUM(review_count) AS total_reviews
  FROM user
  GROUP BY name
  ORDER BY SUM(review_count) DESC
  LIMIT 3

-- Part 8: fan reviews correlation
SELECT name, SUM(review_count) AS total_reviews, SUM(fans) AS total_fans
  FROM user
  GROUP BY name
  ORDER BY SUM(fans) DESC

-- Part 9: review with love in them vs. hate
SELECT COUNT(*)
  FROM review
  WHERE text LIKE '%love%'

SELECT COUNT(*)
  FROM review
  WHERE text LIKE '%hate%'

-- Part 10: top 10 users with the most fans
SELECT name, SUM(fans) AS total_fans
  FROM user
  GROUP BY name
  ORDER BY SUM(fans) DESC
  LIMIT 10

-- part 11.1: hour distribution by rating
SELECT name, city, avg(stars) AS avg_stars, hours, category
  FROM business, hours, category
  WHERE business.id = hours.business_id
    AND business.id = category.business_id
    AND city = 'Toronto'
    AND category = 'Restaurants'
  GROUP BY name, stars
  ORDER BY avg_stars

-- part 11.2: 2 category comparison, # reviews
SELECT city, category, SUM(review_count) AS total_reviews
  FROM business, category
  WHERE business.id = category.business_id
    AND city = 'Toronto'
    AND category IN ('Restaurants', 'Bars')
  GROUP BY category
  ORDER BY SUM(review_count) DESC

-- part 11.3: location assessment
SELECT name, city, category, neighborhood
  FROM business, category
  WHERE business.id = category.business_id
    AND city = 'Toronto'
    AND category IN ('Restaurants', 'Bars')
  GROUP BY name, category
  ORDER BY category

-- part 12: difference by is open
SELECT is_open, SUM(review_count), AVG(stars)
  FROM business
  GROUP BY is_open

------------------------
-- Part 3 of Analysis --
------------------------

-- using stars as a target variable
SELECT business.id, business.stars, business.review_count, review.id, review.useful, review.funny, review.cool
  FROM business INNER JOIN review
  ON business.id = review.id

















-- end of script
