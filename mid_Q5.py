# function1
def create_record():
    a,b=[],input() # get input from keyboard: messy travel records
    while b!='q':
        a.append(b)
        b=input()
    return a # return: records - a list of lists of records
# function2
def sort_list(records):
# input: a list of lists of record
    return sorted(records)
# return: sorted_records - sorted version of the input
# function3
def create_output(sorted_records): # input: sorted records
# return: (1) a list of user’s name and (2) a list of trip’s details with the
# index of each list corresponding to one another
    n=[]
    for i in sorted_records:
        i=i.split()
        if i not in n:
            n.append(i[0])
    c=n[0]
    for i in sorted_records:
        i=i.split()
        print(c,i[0])
        if c==i[0]:
            print('{}:{}'.format(i[1],i[2]))
        else:
            c=i[0]
    return "No records" if len(n)==0 else n
# the main function
def main():
    print(create_output(sort_list(create_record())))
# call these three methods
# print out the sorted output in the correct format back to the user
exec(input())