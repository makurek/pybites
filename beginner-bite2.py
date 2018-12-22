"""
In this bite you will work with a list of names.
First you will write a function to take out duplicates and title case them.
Then you will sort the list in alphabetical descending order by surname and
lastly determine what the shortest first name is.
For this exercise you can assume there is always one name and one surname.
With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    new_list = []
    for item in names:
        if item not in new_list:
            new_list.append(item)
    return new_list

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    return sorted(names, key=lambda x: x.split(" ")[-1])



def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    # ...


l = dedup_and_title_case_names(NAMES)
print(l)
l = sort_by_surname_desc(l)
print(l)