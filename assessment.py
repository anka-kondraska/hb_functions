# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_cost_with_tax(state_abbreviation, cost_amount, tax_amount=0.05):
    """Function to calculate total cost with tax, dafault tax_amount equals 5%"""

    if state_abbreviation == "CA":
        tax_amount = 0.07
    total_cost = cost_amount + cost_amount * tax_amount
    return total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_berry(fruit_of_your_choosing):
    """Function checks if fruit is strawberry, cherry or blackberry"""

    if fruit_of_your_choosing in "strawberry cherry blackberry":
        return True
    return False

def shipping_cost(fruit):
    """Function to calculate shipping cost based on the fruit"""

    if is_berry(fruit):
        return 0
    return 5

def is_hometown(town):
    """Function to determine whether you are from Suwalki"""

    if town == "Suwalki":
        return True
    return False

def full_name(first_name, last_name):
    """Function to concatenate your first and last name"""

    return first_name + ' ' + last_name


 def hometown_greeting(town, first_name, last_name):
    """Function to greet you depending if your hometown is Suwalki """

    if is_hometown(town):
        print "Hi {}, we're from the same place!" .format(full_name(first_name, last_name))
    else:
        print "Hi {}, where are you from?" .format(full_name(first_name, last_name))





#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def increment(x=1):
    """Function to increment x into a function with in a funtction"""

    def add(y):
        """Function within a function to add x and y"""
        return y + x
    return add

addfive = increment(x=5)
addfive(y=5)
addfive(y=20)

def add_num_to_list(number, number_list):
    """Function to append a number to a list"""

    number_list.append(number)
    return number_list


#####################################################################