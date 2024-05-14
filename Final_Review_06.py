class stack:
# Task 1
    def __init__(self, size): # DO NOT modify this line
    # remove pass and replace with you code
        self.capacity=size
        self.content=[None]*size
        self.tos=0
    # Task 2
    def __str__(self): # DO NOT modify this line
    # remove pass and replace with you code
        l=[]
        for i in self.content:
            l.append(i)
        return 
    # Task 3
    def push(self, data): # DO NOT modify this line
    # remove pass and replace with you code
        pass
    # Task 4
    def pop(self): # DO NOT modify this line
    # remove pass and replace with you code
        pass
    # Task 5
def main():
    n=int(input())
    a=stack(n)
    # print(stack(n))
# (1) get an integer number, n, from keyboard
# (2) create an empty stack with capacity equal n + 1, and
# print the stack created
# (3) get n integer numbers from keyboard one line at time
# each time the input is entered the data should be added tostack created in (2)
# print the stack after all data are added
# (4) remove all elements except the bottom most of the stack,and calculate
# the summation of removed elements and print the summationto screen
# (5) print the stack properties (DO NOT use show_stack())main()
main()