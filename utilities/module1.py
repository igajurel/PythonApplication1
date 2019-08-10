
class Utilities:
    def add(a, b):
        return a+b

    def subtract(a,b):
        return abs(a-b)

    #Write a function that returns the largest element in a list.
    def findLargestInList(inp_list):
        outp_list = inp_list
        largest_number = outp_list[0]
        for i in range(1,len(inp_list)):
            if inp_list[i] > largest_number:
                largest_number = inp_list[i]

        print("Largest Number = ", largest_number)
        return largest_number


