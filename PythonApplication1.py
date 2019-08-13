
from utilities.module1 import Utilities

total = Utilities.add(1,3)
print("SUm=",total)

print("===================")

list_x = [1,2,3,5,4]
Utilities.findLargestInList(list_x)

print("===================")

Utilities.reversethelist(list_x)

print("===================")

Utilities.isElementPresent(list_x,5)


print("===================")

Utilities.pullOddElements(list_x)

list_x_y = [1,2,3,5]
Utilities.pullOddElements(list_x_y)

print("===================")

Utilities.computeRunningTotal(list_x)

print("===================")

#x_string = "sansa"
x_string = "madam"
is_inpstr_palindrome = Utilities.checkPalindrome(x_string)
print("The statement that the given string",x_string,"is a Palindrome is",is_inpstr_palindrome)


#xy_string = "madam"
#xy_string = "abdba"
#xy_string = "abcda"
xy_string = "isxi"
is_inpstr_palindrome_opt = Utilities.checkPalindromeOptimized(xy_string)
print("*Optimized* - The statement that the given string",xy_string,"is a Palindrome is",is_inpstr_palindrome_opt)


