def is_divisible(x, y):				#calls the is_divisible function from Section 6.4
  if x % y == 0:
    return True
  else:
    return False

def is_power(x, y):					#defines the is power function that takes two arguments base x and power of y as for the is power function 
    assert x > 0, 'base x should be a positive integer'				#asserts both arguments to be positive integers
    assert y > 0 , 'power of y should be a positive integer'
    if is_divisible(x, y) == False:	 #calls the is divisible function, returns False if numbers are not divisible
     return False
    elif y == 1 and x != 1:      	#only positive integer that is a power of "1" is "1" itself. 
     return False
    elif x == y:        #stops recursion when divison of powers is complete
     return True
    else:
     is_divisible(x, y) == True #calls the is divisible function, returns True if numbers are divisible 
     return is_power(x/y, y)		#recursive call to is_power functionprint("is_power(10, 2) returns: ", is_power(10, 2)) 
     
print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))