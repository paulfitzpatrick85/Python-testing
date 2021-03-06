"""
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """


def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        # if numbers == []:  # line 24 covers this, so it can be deleted for D.R.Y's sake
        #     return False
        # else:
        # evens = 0

        evens = sum([1 for n in numbers if n % 2 == 0])   
        # for n in numbers:  # can be replace with list comprehension above
        #     if n % 2 == 0:
        #         evens += 1

        # if evens:
        #     return evens % 2 == 0  # will return true if number of 'evens' is even
        # else:
        #     return False  #replaced with below
        return True if evens and evens % 2 == 0 else False
    else:
        raise TypeError("A List was not passed into the function")


if __name__ == "__main__":
    print(even_number_of_evens(5))