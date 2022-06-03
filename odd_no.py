#Odd numbers are those numbers which can't be divided by two 
# eg. 3, 5, 7, 9 , 11 etc........
From  = int(input('Odd number  \n\tfrom : ')) # don't use from in lowercase because it is reserved keyword 
To = int(input('\tTo: '))
print(f'So ODD numbers b/w {From} to {To} are : ')
for num in range(From , To+1):
    if (num%2 !=0):
        print(num) 

