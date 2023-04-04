""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import TextIO
import io

# Sample Data (Used by Docstring examples)
# What a Profile File might look like.
EXAMPLE_PROFILE_DATA = '''Katsopolis, Jesse
Parent Council
Rock N Rollers
Tanner, Danny R
Donaldson-Katsopolis, Rebecca
Gladstone, Joey

Donaldson-Katsopolis, Rebecca
Gibbler, Kimmy

Tanner, Stephanie J
Tanner, Michelle
Gibbler, Kimmy

Tanner, Danny R
Parent Council
Tanner-Fuller, DJ
Gladstone, Joey
Katsopolis, Jesse

Gibbler, Kimmy
Smash Club
Rock N Rollers

Gladstone, Joey
Comics R Us
Parent Council

Tanner, Michelle
Comet Club
'''


P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
       'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions




def item_count(my_dict):
   
    num_items = 0
    for value in my_dict.values():
        num_items += len(value)

    return num_items


def key_count(my_dict):
	return len(my_dict.keys())





def update_dict(key: str, value: str,
                key_to_values: dict[str, list[str]]) -> None:
	"""Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """
	if key not in key_to_values:
		key_to_values[key] = []
	if value not in key_to_values[key]:
		key_to_values[key].append(value)


# Required functions

def load_profiles(profiles_file: TextIO) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.
    >>> data = io.StringIO(EXAMPLE_PROFILE_DATA) # this treats a str as a file
    >>> result = load_profiles(data)
    >>> result == (P2F, P2C)
    True
    """
    P2F = {}
    P2C = {}

    # read the contents of the file into the list with each line being an element of the list
    l = profiles_file.readlines()

    # loop to remove start and end whitespaces from each line of file
    for i in range(len(l)):
        l[i] = l[i].strip()

    flag = 0

    # loop over the contents of the file
    for i in range(len(l)):
        # if flag is 0, then the line has a person name
        if flag == 0:
            s = l[i].split(',')
            s.reverse()
            person_name = ' '.join(s).strip()  # Remove any whitespace before and after the name
            P2C[person_name] = []
            P2F[person_name] = []
            flag = 1
        elif len(l[i]) == 0:
            flag = 0
        elif ',' not in l[i]:
            P2C[person_name].append(l[i].strip())  # Remove any whitespace before and after the club name
        elif ',' in l[i]:
            t = l[i].split(',')
            t.reverse()
            temp = ' '.join(t).strip()  # Remove any whitespace before and after the friend's name
            P2F[person_name].append(temp.strip()) # Remove any whitespace before and after the friend's name

    # remove records with empty values from P2F
    l = []
    for k in P2F.keys():
        if len(P2F[k]) == 0:
            l.append(k)

    for i in l:
        P2F.pop(i)

    # remove records with empty values from P2C
    l = []
    for k in P2C.keys():
        if len(P2C[k]) == 0:
            l.append(k)

    for i in l:
        P2C.pop(i)

    # Sort the values in both dictionaries in alphabetical order
    for k in P2F.keys():
        P2F[k].sort()

    for k in P2C.keys():
        P2C[k].sort()

    return (P2F, P2C)

    


	
   
    
   
	











    
    
   

    







    
    

    # TODO: add a second docstring example above (create a new constant
    #       referring to a sample profiles data file at the top of this module
    #       and use that within your docstring example)
    # TODO: design and write the function body


def get_average_club_count(person_to_clubs: dict[str, list[str]]) -> int:
	"""Return the average number of clubs that a person in person_to_clubs
    belongs to, rounded down to the nearest integer (i.e. use // instead of /).

    >>> get_average_club_count(P2C)
    1
    >>> get_average_club_count(P2F)
    2
    """
	return item_count(person_to_clubs) // key_count(person_to_clubs)
    


def get_last_to_first(
    person_to_friends: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a "last name to first name(s)" dictionary with the people from
	    the
	"person to friends" dictionary person_to_friends.
    
	>>> get_last_to_first(P2F) == {
	...    'Katsopolis': ['Jesse'],
	...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
	...    'Gladstone': ['Joey'],
	...    'Donaldson-Katsopolis': ['Rebecca'],
	...    'Gibbler': ['Kimmy'],
	...    'Tanner-Fuller': ['DJ']}
	True
	"""    

    last_to_first = {}
    for person, friends in person_to_friends.items():
        name_parts = person.rsplit(" ", 1)
        last = name_parts[-1]
        first = name_parts[0]
        if last in last_to_first:
            if first not in last_to_first[last]:
                last_to_first[last].append(first)
        else:
            last_to_first[last] = [first]
        for friend in friends:
            name_parts = friend.rsplit(" ", 1)
            last = name_parts[-1]
            first = name_parts[0]
            if last in last_to_first:
                if first not in last_to_first[last]:
                    last_to_first[last].append(first)
            else:
                last_to_first[last] = [first]
    return last_to_first






def invert_and_sort(key_to_value: dict[object, object]) -> dict[object, list]:
    """Return key_to_value inverted so that each key in the returned dict
    is a value from the original dict (for non-list values) or each item from a
    value (for list values), and each value in the returned dict
    is a list of the corresponding keys from the original key_to_value.
    The value lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    >>> club_to_score = {'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}
    >>> invert_and_sort(club_to_score) == {
    ...  3: ['Parent Council'], 2: ['Orchestra', 'Smash Club']}
    True
    """
    
    inverted_dict = {}
    for key, value in key_to_value.items():
        if type(value) == list:
            for item in value:
                if item in inverted_dict:
                    inverted_dict[item].append(key)
                else:
                    inverted_dict[item] = [key]
        else:
            if value in inverted_dict:
                inverted_dict[value].append(key)
            else:
                inverted_dict[value] = [key]
    for value in inverted_dict.values():
        value.sort()
    return inverted_dict
    


#def get_clubs_of_friends(person_to_friends: dict[str, list[str]],
                         #person_to_clubs: dict[str, list[str]],
                         #person: str) -> list[str]:
    #"""Return a list, sorted in alphabetical order, of the clubs in
    #person_to_clubs that person's friends from person_to_friends
    #belong to, excluding the clubs that person belongs to.  Each club
    #appears in the returned list once per each of the person's friends
    #who belong to it.

    #>>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    #['Comics R Us', 'Rock N Rollers']
    #"""
    #clubs = {}
    #for friend in person_to_friends[person]:
        #if friend in person_to_clubs:
            #for club in person_to_clubs[friend]:
                #if club not in person_to_clubs[person]:
                    #clubs[club] = clubs.get(club, 0) + 1

    #return sorted([club for club, count in clubs.items() for i in range(count)])


def get_clubs_of_friends(person_to_friends: dict[str, list[str]],
                          person_to_clubs: dict[str, list[str]],
                          person: str) -> list[str]:
    """Return a sorted list of the clubs that at least one of the friends
    of person belongs to, excluding the clubs person belongs to. If person
    has no friends, return an empty list.

    >>> P2F = {'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller', 'Joey Gladstone'], \
    'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone', 'Rebecca Donaldson-Katsopolis'], \
    'Joey Gladstone': ['Danny R Tanner', 'Jesse Katsopolis'], \
    'DJ Tanner-Fuller': ['Danny R Tanner'], \
    'Rebecca Donaldson-Katsopolis': ['Jesse Katsopolis', 'Kimmy Gibbler'], \
    'Kimmy Gibbler': ['Rebecca Donaldson-Katsopolis', 'Stephanie J Tanner'], \
    'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'], \
    'Michelle Tanner': ['Stephanie J Tanner'], \
    'Steve Hale': []}
    >>> P2C = {'Danny R Tanner': ['Parent Council'], \
    'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'], \
    'Joey Gladstone': ['Comics R Us', 'Parent Council'], \
    'DJ Tanner-Fuller': [], \
    'Rebecca Donaldson-Katsopolis': ['Rock N Rollers', 'Smash Club'], \
    'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'], \
    'Stephanie J Tanner': [], \
    'Michelle Tanner': ['Comet Club'], \
    'Steve Hale': []}
    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    """
    clubs = set()
    friends = person_to_friends.get(person, [])
    for friend in friends:
        clubs.update(person_to_clubs.get(friend, []))
    clubs.difference_update(person_to_clubs.get(person, []))
    return sorted(list(clubs))





	
    # TODO: add a second docstring example above
    # TODO: design and write the function body
    



	
    # TODO: add a second docstring example above
    # TODO: design and write the function body

    
    


def recommend_clubs(P2F, P2C, person):
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """    

    if person not in P2F and person not in P2C:
        return []
    club_count = {}
    if person in P2C:
        for club in P2C[person]:
            club_count[club] = 1
    for friend in P2F.get(person, []):
        if friend in P2C:
            for club in P2C[friend]:
                if club not in club_count:
                    club_count[club] = 0
                club_count[club] += 1
    return [(club, count) for club, count in club_count.items()]

    

if __name__ == '__main__':
	pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
