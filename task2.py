foryou = []
print('What do you want to do?')
database = input("do it: ") # in here put either rewrite, add, or read_it

if database == 'rewrite':
       yourwords = input('what do you want to write: ')
       with open('data.txt', 'w') as file:
           file.write(yourwords)
           file.close
elif database == 'add' :
     yourwords2 = input('what do you want to add: ')
     with open('data.txt', 'a') as file :
          file.write(yourwords2)
          file.close
elif database == 'read_it':
     with open('data.txt', 'r') as file:
          yourfile = file.readline()
          print(yourfile)
          file.close


     






