
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
    def pullOddElements(inp_list):
        list_odd_elements = []
        for i in range(0,len(inp_list)):
            if (i+1)%2 == 1:
                list_odd_elements.append(inp_list[i])
        print("The elements which are in odd position are-", list_odd_elements)
        return list_odd_elements

