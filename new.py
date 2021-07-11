# # # # from sys import argv
# # # # a=argv[1:]
# # # # sum=0
# # # # for x in a:
# # # #     b=int(x)
# # # #     sum=sum+b
# # # # print('The sum',sum)


# # # # print('hello' 'mr'  'how are you')



# # # # print('%0.2f' %(2.3333))
# # # print('hi {} sal is {}'.format('aa',100 ))

# # name=input('Enter your Name:')
# # if name=='Nihol':
# #     print('Hello %s welcome in python' %name)
# # else:
# #     print('Hello %s welcome' %name)
# #     print('kem cho')  
# # print('it\'s wonderful')
# # 
# # even or odd


# num=int(input('enter the number:'))
# if num==0:
#     print('you enter number is (%d)' %num)
# elif num%2==0:
#     print('you enter number is (%d) even number' %num)
# else:
#     print('you enter number is (%d) odd number' %num)



# even or odd  by command line:
# from sys import argv
# x=argv[1:]

# for y in x :
#     n=eval(y)
#     if n==0:
#         print('you enter number is (%d) zero' %n)
#     elif n%2==0:
#         print('you enter number is (%f) even number' %n)
#     else:
#         print('you enter number is (%f) odd number' %n)




# to check whether the given number is in between 1 and 100
# # # by input():
# num=int(input('Enter number :'))
# if num==0:
#     print('Entered number is (%d)invalid number' %num)
# elif num>=1 and num<=100:
#     print('Entered number is (%d) between 1 to 100' %num)
# else :
#     print('Entered number is (%d) is not between 1 to 100' %num)

# # by command line argument:
# from sys import argv
# x=argv[1:]
# for y in x:
#     n=int(y)
#     if n==0:
#         print('Entered number is (%d)invalid number' %n)
#     elif n>=1 and n<=100:
#         print('Entered number is (%d) between 1 to 100' %n)
#     else :
#         print('Entered number is (%d) is not between 1 to 100' %n)


# a single dgit read and convert into englsh word
# by input()

# num=int(input('Enter The Nummber:'))
# if num>9:
#     print('Enter number (%d) is invalid' %num)
# elif num>=0 and num<=9:
#      print('enter number (%d) is valid' %num)   
#      if num==0:
#          print('Enter The Number (%d) is zero' %num)
#      elif num==1:
#          print('Enter The Number (%d) is one' %num)
#      elif num==2:
#          print('Enter The Number (%d) is two' %num)
#      elif num==3:
#          print('Enter The Number (%d) is three' %num)
#      elif num==4:
#          print('Enter The Number (%d) is four' %num)
#      elif num==5:
#          print('Enter The Number (%d) is five' %num)
#      elif num==6:
#          print('Enter The Number (%d) is six' %num) 
#      elif num==7:
#          print('Enter The Number (%d) is seven' %num) 
#      elif num==8:
#          print('Enter The Number (%d) is eight' %num) 
#      else :
#          print('Enter The Number (%d) is nine' %num)     


# by command line 
# from sys import argv
# x=argv[1:]
# for y in x:
#     num=int(y)
#     if num>9:
#         print('Enter number (%d) is invalid' %num)
#     elif num>=0 and num<=9:
#         print('enter number (%d) is valid' %num)   
#         if num==0:
#          print('Enter The Number (%d) is zero' %num)
#         elif num==1:
#          print('Enter The Number (%d) is one' %num)
#         elif num==2:
#          print('Enter The Number (%d) is two' %num)
#         elif num==3:
#          print('Enter The Number (%d) is three' %num)
#         elif num==4:
#          print('Enter The Number (%d) is four' %num)
#         elif num==5:
#          print('Enter The Number (%d) is five' %num)
#         elif num==6:
#          print('Enter The Number (%d) is six' %num) 
#         elif num==7:
#          print('Enter The Number (%d) is seven' %num) 
#         elif num==8:
#          print('Enter The Number (%d) is eight' %num) 
#         else :
#          print('Enter The Number (%d) is nine' %num)  


# by dict

# for x in 2*'hello':
#     print(x)



# To print the sum of numbers present in the given list???

# by command line

# from sys import argv
# x=argv[1:]
# sum=0
# for y in x:
#     n=int(y)
#     sum=sum+n
# print('Sum of given list is = %d' %(sum))
    



# by input()


# l=eval(input('enter list:'))   
# sum=0s
# for x in l:  
#     sum=sum+x
# print('the sum is=%d'%sum)


# sum of n natural number
# n=int(input('Enter Number:'))
# sum=0
# for x in range(0,n+1):
#     sum=sum+x
# print('The Sum Of first {} Number: {}'.format(n,sum))  
      
# enter user name or password

# i=1
# while True and i<=4:
#     USERNAME=input('ENTER OUR USERNAME:')
#     PASSWORD=input('ENTER YOUR PASSWORD:')  
#     if USERNAME=="nihol" and PASSWORD=="nihol123":
#         print('*welcome',end="*")
#         break
#     else:
#         print((10*'*')+'youe input is not valid: better lauk next time'+(10*'*'))
#     i=i+1  
# else:
#     print('Your all attemps is done')        



# disign of A
# def a():
#     for i in range(0,7):
        
#         if (i==0):
#             print(' '+3*'* ')
#         elif (i==1) or (i==2) or (i==4) or (i==5) or (i==6):
#             print('*'+3*' '+2*' '+'*')
#         elif (i==3):
#             print((6-3+1)*'* ')   
#     return None
# print(a())

# plz note here return value is none because we use a function = a() if we don't give return none value so itcan by defalut take a none




# for x in range(10,0,-1):
#     print(x,end=' \t')




# l=eval(input('enter list:'))
# sum=""  #here we must type list in str list only:ex.['a','b','c']
# for x in l:
#     sum=sum+x
# print('the sum :',sum)


# s1='durga'
# s2='mia'
# s=s1+s2
# del s 
# print (s)


# Table 1 to 10 :

# for i in range(1):
#     for j in range(1,11):
#         print("  "*3+str(j),end='')
# print()
# print('_ _'*25)
# for row in range(10):
#     row+=1
#     if row==1 or row<=9:
#         print("\n"+str(row)+"   |",end=' ')
#     if row==10:
#         print("\n"+str(row)+"  |",end=' ')
    
   
#     for col in range(10):
#         if row==0 or row==1:
#             print("  "+str(col+1),end="  ")
#         elif row==2 or row<=4:
#             print("  "+str((col+1)*row),end="  ")
#         elif row==5 or row<=9:
#             print("  "+str((col+1)*row),end="  ")    
#         elif row==10:
#             print(" "+str((col+1)*row),end="   ")
    
# print()  #if here we reduce print so we get output without space
s1=input('Enter main string:')
s2=input('Enter sub string:')
s3=s1[::-1]
print(s3)
n=0
for i in s1:
    for j in s2:
        if j in i:
            # print(s1.rfind('{} at {}'.format(i,j)))
        
            n=s1.find('%s' %(j))
            
            print('%s in index %s' %(j,n))
           
print('\nthanks')    
