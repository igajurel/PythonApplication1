
class Utilities:
    def add(a, b):
        return a+b

    def subtract(a,b):
        return abs(a-b)

    #Write a function that returns the largest element in a list.
    #O(n) time complexity
    def findLargestInList(inp_list):
        outp_list = inp_list
        largest_number = outp_list[0]
        for i in range(1,len(inp_list)):
            if inp_list[i] > largest_number:
                largest_number = inp_list[i]

        print("Largest Number = ", largest_number)
        return largest_number

    #Write function that reverses a list, preferably in place.
    #O(n) time complexity
    def reversethelist(inp_list):
        print("Original List = ",inp_list)
        outp_list = []
        for i in range(len(inp_list)-1,-1,-1):
            outp_list.append(inp_list[i])
        print("Reversed List = ",outp_list)
        return outp_list

    #Write a function that checks whether an element occurs in a list.
    #O(n) or O(log(n) with binary search - does it require already sorted list)
    def isElementPresent(inp_list, element):
        isElementPresent = False
        for i in range(0,len(inp_list)):
            #print(inp_list[i])
            if element == inp_list[i]:
                isElementPresent = True
                break
        print("The statement that element",element,"is present in the input list ",inp_list,"is",isElementPresent)

    #Write a function that returns the elements on odd positions in a list.
    #O(n), however, it has been improvised to not iterate the unnecessary even position elements towards the end of input list
    def pullOddElements(inp_list):
        list_odd_elements = []
        if(len(inp_list)%2 == 0): 
            last_element = len(inp_list)-1
        else:
            last_element = len(inp_list)

        for i in range(0,last_element):
            print(i)
            if (i+1)%2 == 1:
                list_odd_elements.append(inp_list[i])
        print("The elements which are in odd position are-", list_odd_elements)
        return list_odd_elements

    #Write a function that computes the running total of a list.
    #O(n)
    def computeRunningTotal(inp_list):
        running_total = inp_list[0]
        for i in range(1,len(inp_list)):
            running_total += inp_list[i]
            print(running_total)

    #Write a function that tests whether a string is a palindrome.
    #O(creating a list out of string) + O(n) - reversed string + O(comparing the string)
    def checkPalindrome(inp_string):
        list_inp_string = list(inp_string)
        print(list_inp_string)
        reversed_string = Utilities.reversethelist(list_inp_string)
        if(list_inp_string==reversed_string):
            return True
        return False

    #O(creating a list out of string) + O(n/2 as only half way traversal)  
    #best case if first and last element itself doesn't match
    def checkPalindromeOptimized(inp_string):
        inp_list = list(inp_string)
        i = 0
        j = len(inp_list)
        while(i<=j):
            #print(i)
            #print(j)
            if inp_list[i] != inp_list[j-1]:
                return False
            i = i+1
            j = j-1

        return True