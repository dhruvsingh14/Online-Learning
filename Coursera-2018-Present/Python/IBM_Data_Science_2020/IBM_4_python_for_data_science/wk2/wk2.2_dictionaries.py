#######################
# wk2.2: dictionaries #
#######################

################
# Dictionaries #
################

##########################
# What are Dictionaries? #
##########################
# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
print(Dict)

# Access to the value by the key
Dict["key1"]

# Access to the value by the key
Dict[(0, 1)]

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

########
# Keys #
########
# Get value by keys
release_year_dict['Thriller']

# Get value by key
release_year_dict['The Bodyguard']

# Get all the keys in dictionary
print(release_year_dict.keys())

# Get all the values in dictionary
print(release_year_dict.values())

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
print(release_year_dict)

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
print(release_year_dict)
# keys perform the same role as indices

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict

########################
# Quiz on Dictionaries #
########################
# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic)

# a)
print(soundtrack_dic.keys())

# b)
print(soundtrack_dic.values())


# a) creating album sales dictionary
album_sales_dict = {"Back in Black":50, "The Bodyguard":50, "Thriller":65}

# b) total sales for thriller
print(album_sales_dict["Thriller"])

# c) album names
print(album_sales_dict.keys())

# d) recording sales
print(album_sales_dict.values())

####################
# Week 2: Quiz 2.2 #
####################
# q1
print({"The Bodyguard":"1992", "Saturday Night Fever":"1977"}.keys())

# comment: dictionaries are kind of like metadata in a sense








# in order to display plot within window
# plt.show()
