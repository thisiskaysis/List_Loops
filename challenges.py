def add_chocolate(shopping_list: list):
    """My housemate is a real health-nut, but I like chocolate. This function 
    adds the string "chocolate" to any list it receives, and returns the 
    modified list. That way our shopping list is always correct.

    Arguments:
        - shopping_list: a list of strings

    Returns:
        - the same list, with the string "chocolate" added to the end
    """

    shopping_list.append("chocolate")
    return shopping_list

def lou_bega(lyrics_list: list):
    """This function accepts a list of strings and adds the words 
    "A little bit of " to the front of each.
    
    Arguments:
        - lyrics_list: a list of strings
    
    Returns:
        - the same list, but each string now has "A little bit of " 
        prepended to it.

    Example input: 
        [
            "Monica in my life", 
            "Erica by my side", 
            "Rita's all I need"
        ]
        
    Example output: 
        [
            "A little bit of Monica in my life", 
            "A little bit of Erica by my side", 
            "A little bit of Rita's all I need"
        ]
    """
    add = "A little bit of "
    new_lyrics = list(add + lyrics for lyrics in lyrics_list)
    return new_lyrics

#OR new_list = []
#for lyric in lyrics_list:
#   new_lyric = ("A little bit of " + lyric)
#   new_list.append(new_lyric)
#return new_list

def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    
    guest_list = []

    while True:
        name = input("Enter guest name: ")
        if name == '':
            break
        guest_list.append(name)
    
    return guest_list
   



def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """
    
    result_list = []

    for number in range(2, some_number):
        calculate = float(some_number / number)
        result_list.append(calculate)

    has_integer = any(result.is_integer() for result in result_list)

    if some_number < 2:
        return False
    elif has_integer != True:
        return True
    else:
        return False

