#Create a calculator using the Test Driven Development cycle following the steps below. 
# 
# 1. Write tests and a method called add that takes 2 ints as parameters and adds them together.
# 2. Now modify that method to take any amount of integers
# 3. Now have add() throw an Error when a negative number is passed in
# 4. Now write a new method called operation() that takes a string with the value "subtract", "mulitply", or "divide" and 2 integers as parameters that calculates the result of the operation applied to the 2 integers. Return a message informing the user that the operation is not supported if the string is not a supported operation.
'''
Below is the steps of the above.  Separated out into the different parts for simplicity
'''

''' 
#Part 1
#Adds two numbers together
#def add(num1, num2):
#    result = num1 + num2
#    return result 
'''

''' 
#Part 2
#Allowing passing of unlimited numbers
def add(*num):
    result = sum(num)
    return result
'''

#Part 3 
#Addition of unlimited integrers and erroring with negative numbers
def add(*numbers):
    for num in numbers:
        if num < 0:
            raise TypeError('no negative numbers please')
        else:
            result = sum(numbers)
            return result

#Part 4
#Additional operations and Error out if invalid operation is entered
def operation(string, num1, num2):
    if string == "subtract":
        result = num1 - num2
        return result
    elif string == "multiply":
        result = num1 * num2
        return result
    elif string == "divide":
        result = num1 / num2
        return result
    else:
        raise TypeError('not a valid operation')