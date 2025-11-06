# creating a set
# in python there are multiple ways to create a set.
# A set object can be created by passing an iterable object into its constructor using curly braces or using a set comprehension

# lets examine syntax of these methods:
# creatign a set with curly braces
music_generes = {"rock", "pop", "jazz", "classical"}

# creating a set from a list using the set() constructor
music_generes_from_list = set(["rock", "pop", "jazz", "classical"])

# its worth noting that creating a set from a list with duplicates produces a set with duplicates removed
music_generes_with_duplicates = set(["rock", "pop", "jazz", "classical", "rock", "pop"])
print(music_generes_with_duplicates)  # Output: {'rock', 'pop', 'jazz', 'classical'}

# while we use a similar data type in sets above, sets can actually contain any combination of data types as long as they are unique values.
music_different = {70, "rock", 3.14, True}

# we can also create an empty set with one specific method:
empty_set = set()

# Note: using empty curly braces {} creates an empty dictionary, not a set.
not_empty_set = {}  # This is a dictionary, not a set


# similar to list comprehensions, we can create sets using set comprehension and a data set such as a list
items = ["country", "rock", "pop", "jazz", "rock", "classical", "pop", "punk", "reggae"]
# music_generes = {category for category in items if category[0] != "r"}
music_generes = {category for category in items if category[0] == "p"}
print(music_generes, "!!")  # Output: {'classical', 'jazz', 'pop', 'country'}

abbreviations = {word[0:3] for word in items}
print(abbreviations)  # Output: {'cou', 'cla', 'pop', 'pun', 'jaz', 'reg', 'roc'}


# exercise:
genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)
survey_abbreviated = {genre[0:3] for genre in survey_genres} # correct syntax for set comprehension
print(survey_abbreviated)
# alternative way using set() constructor
survey_abbreviated = set(genre[0:3] for genre in survey_genres) # correct syntax using set() constructor
print(survey_abbreviated)


# creating a frozen set:
# unlike a normal `set` you can only create a `frozenset` using its constructor.
# remember that using `frozenset` creates an immutable set, meaning its contents cannot be changed after creation.
frozen_music_genres = frozenset(["rock", "pop", "jazz", "classical"])
print(frozen_music_genres)  # Output: frozenset({'rock', 'pop', 'jazz', 'classical'})
# frozen_music_genres.add("hip-hop")  # This will raise an AttributeError since fro

# we can also create an empty frozenset
empty_frozen_set = frozenset()
print(empty_frozen_set)  # Output: frozenset()

# why would we need an empty frozenset?
# one use case is when we need to initialize a variable that will later hold a frozenset value, but we don't have any initial data to populate it with.
# using an empty frozenset allows us to define the variable with the correct type from the start. This can be useful in functions or methods that expect a frozenset as an argument or return type. 

# can we add data into a empty frozenset later?
# no, since frozensets are immutable, once created, their contents cannot be changed. However, we can create a new frozenset that includes additional elements by combining the empty frozenset with other data.
new_frozen_set = empty_frozen_set.union(frozenset(["hip-hop", "blues"]))
print(new_frozen_set)  # Output: frozenset({'hip-hop', 'blues'}) 

# exercise:
top_genres = ['rock', 'pop', 'rap', 'classical', 'jazz', 'country', 'latin', 'k-pop', 'punk', 'reggae']
# Write your code below!
frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)


# Adding to a set
# there are two different ways to add elements to a set:
# 1. `add()` method can add a single element to `set`

song_tags = {'counrty', 'folk', 'bluegrass', 'acoustic'}
# adding a new tag to set and try to add a duplicate tag
song_tags.add('indie')
song_tags.add('folk')  # duplicate, will not be added
print(song_tags)  # Output: {'counrty', 'folk', 'bluegrass', 'acoustic', 'indie'}

# 2. `update()` method can add multiple elements to a set from any iterable (like list, tuple, or another set)
song_tags = {'counrty', 'folk', 'bluegrass', 'acoustic'}
# adding more tags using a hashable object such as a list or tuple or another set
other_tags = ['rock', 'pop', 'indie', 'folk']  # list with a duplicate 'folk'
song_tags.update(other_tags)
print(song_tags)  # Output: {'counrty', 'folk', 'bluegrass', 'acoustic', 'rock', 'pop', 'indie'}

# there are a few things to note about adding to a Set:
# neither of these methods will add a duplicate item to a `set`
# a frozenset can not have any itenms added to it and will raise an AttributeError if you try to use either method on a frozenset.
# notice, when elements are printed, they are not printed in same order in which they were entered into `set`, this is because `set` and `frozenset` are unordered collections.

# exercise:
song_data = {'Retro words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'dance'
user_tag_3 = 'electric'

# Write your code below!
tag_set = set(song_data['Retro words'])
tag_set.add(user_tag_1)
tag_set.update([user_tag_2, user_tag_3])
print(tag_set)

song_data['Retro words'] = tag_set
print(song_data)


# removing from a set:
# there are two methods to remove elements from a set

# 1. `remove()` method can remove a single element from a set if it exists otherwise it will raise a KeyError
song_tags = {'counrty', 'folk', 'bluegrass', 'acoustic'}
song_tags.remove('folk')
print(song_tags)  # Output: {'counrty', 'bluegrass', 'acoustic'}

# song_tags.remove('folk')  # trying to remove a non-existent element will raise a KeyError

# 2. `discard()` method can remove a single element from a set, but does not raise a KeyError if the element does not exist
song_tags = {'guitar', 'country', 'bluegrass', 'acoustic'}

song_tags.discard('guitar')
print(song_tags)  # Output: {'country', 'bluegrass', 'acoustic'}

song_tags.discard('guitar')  # trying to remove a non-existent element will not raise an error

# note that items can not be removed from a frozenset using either of these methods will raise an AttributeError

# exercise: 
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])

tag_set.remove("onion")
tag_set.discard("spam")
tag_set.discard("helloworld")

song_data_users['Retro Words'] = tag_set
print(song_data_users)