take = str(input("What is your problem? "))
list = take.split()
print(list)
dict = {'internet': {"not":{"working":"check your coonection"}}, 'no': "Reset the wifi"}
j=0
for i in range(j,len(list)):
    if list[i] in dict:
       
        search(j,i)
        print(dict[list[i]])
def output(newlist):
    dict[]
