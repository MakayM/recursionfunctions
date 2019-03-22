def sum_array(array):
    '''Return sum of all items in array'''
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))



def factorial(n):

    '''Return n!'''
    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1

    return result


def reverse(word):

    '''Return word in reverse'''

    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
