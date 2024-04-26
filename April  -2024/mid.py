# print('mid \
#       are here')
# print("""lorem
#       jshadib ugf sdgfa gaiua
#        bdgal gba o ugfa""")

# a = 1
# print(type(a))
# n,m = m,n
# print(n,m)
# a=20
# b=66
# print ('value of a and b before incrementation')
# print('id of a:',id(a))
# print('id of b:',id(b))
# a = b
# print('Value of a and b after incrementation')
# print('id of b:  ', id(b))
# sid = [['hello' , 'hie','dobbay'],['namaste','salam']]
# print(sid[0][2])


# List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# print(List[-2])
# print(len(List))
# list = input("Enter the list : ").split()
# print(list)
# List = []
# for i in range (1,5):
#     List.append(i)
# print(List)
# List.append((5,6))
# print(List)
# List.extend([7,'hie'])
# print(List)
# List.reverse()
# print(List)
# rl = list(reversed(List))
# print(rl)
# List.remove('hie')
# print(List)
# List.pop(1)

# List = [1, 2, 3, 4, 5] 
  
# Removing element from the 
# Set using the pop() method 
# List.pop()
# print(List)

# List = ['G', 'E', 'E', 'K', 'S', 'F', 
#         'O', 'R', 'G', 'E', 'E', 'K', 'S'] 
# print("Initial List: ") 
# print(List)
# print(List[-6:-1])
# List = [1,2,3,4,5]
# eve_sq = [x**2 for x in range(1,6) if x%2 == 0]
# print(eve_sq)
# a = 1
# if a>=0 and a<10:
#     if a%2==0:
#         print('even')
#     else: print('odd')
# else:
#     print('not in range')

# num = [2,3,4,5,6,7,8,9,10]
# for i in num:
#     for j in range(1,11):
#         print(i,'*',j,"=", i*j)
#     print("-----")

# str = "sidhart"
# for i in str:
#     if i == 'd':
#       continue
#     print(i, sep =',')

# f = open("README.md",'w')
# f.write("hello how are you I am fine")

# f.write("hehhhhe")

from functools import reduce

def saman(veg,price = 40):
    print(veg)
    print(price)

saman('banana')
saman('banana',45)
def wish(*names):
    for i in names:
        print("kaiso ho ?? ", i)
wish('kus','ash','ven')
## lamba
sum = lambda x,y:x+y
print(sum(2,3))
str = "     Siddu    bhai  "
print(str.strip())


l = [1,5,633,234,533,42,23,4,2]
# nl = list(filter(lambda x:(x%2==0),l))
# print(nl)

nl = list(map(lambda x:(x*x), l))
print(nl)
nl = reduce(lambda x,y:(x+y), l)
print(nl)


str = "Hello Sid"
s1 = 'Sid'
s2 = 'is'
print(str.replace(s1,s2))
print(str)