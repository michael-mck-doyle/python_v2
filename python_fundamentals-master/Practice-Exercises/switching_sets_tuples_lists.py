# Note, you can switch between lists, tuples, sets...dictionaries by using the keywords:

url_list = ['http://www.example.com', 'http://www.setsareuseful.com', 'http://www.example.com']
unique_urls = set(url_list) # changes a list to a set

list_to_tuple = tuple(url_list) # changes a list to a tuple
#print(list_to_tuple)
tuple_to_set = set(list_to_tuple) # changes a tuple to a set
print(tuple_to_set)

set_to_list = list(tuple_to_set) # changes a set to a list
print(set_to_list)

set_to_tuple = tuple(tuple_to_set) # changes a set to a tuple
print(set_to_tuple)

#print(unique_urls)
# will give us: {'http://www.example.com', 'http://www.setsareuseful.com'}

'''
{'http://www.example.com', 'http://www.setsareuseful.com'} # sets have curly braces
['http://www.example.com', 'http://www.setsareuseful.com'] # lists have square braces
('http://www.example.com', 'http://www.setsareuseful.com') # tuples use regular parenthesis
'''

users = {'mary': 22, 'caroline': 26, 'harry': 22}

dict_to_list = list(users)  # converts a dictionary to a list
print(dict_to_list)

dict_to_tuple = tuple(users)  # converts a dictionary to a tuple
print(dict_to_tuple)

dict_to_set = set(users)  # converts a dictionary to a tuple
print(dict_to_set)

car_brands = ['toyota', 'VW', 'honda', 'BMW']

list_to_dict = dict(car_brands)
print(list_to_dict)
