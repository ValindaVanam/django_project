# n = int(input("enter the number"))
# i=1
# while i<=n:
#     print(i, end=" ")
#     i+=1

# ch=input("enter your charecter: ").casefold()
# if ch.isalpha():
#     if ch in "aeiou":
#         print("Given alpahbet is Vowel")
#     else:
#         print("Given alphabet is Consonent")
# else:
#     print("Given charecter is not a alphabet")

# n=int(input("enter sum of numbers"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

# n=int(input("enter N number to print even numbers"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1

# n=int(input("enter N number to print even numbers"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1

# n=int(input("enter N number to print even numbers"))
# i,j=0,1
# while i<=n:
#     print(i, end=" ")
#     i,j=j,i+j

# st=input("enter string").casefold()
# i=0
# while i<len(st):
#     if st[i] in "aeiou":
#         print(st[i], end=" ")
#     i+=1

# Assignment- WAP to return the sum of digits in a given number
# st = (input("enter number"))
# sum= 0
# for digit in str(st):
#     sum+=int(digit)
# print(sum)

#Amstrong number
# num=int(input("Enter"))
# no_of_digitst = len(str(num))
# temp = num
# sum=0
# while num>=1:
#     digit = num%10
#     sum+= digit**no_of_digitst
#     num//=10
#
# if temp  == sum:
#     print("Amstrong number")
# else:
#     print("Not an amstrong number")

# num= int(input("enter"))
# rev=num
# while num >=1:
#     digit = num%10
#     rev = num*10+digit
#     num//=10
# if rev==num:
#     print('Palindrome')
# else:
#     print("not a palindrome")

# num= int(input("enter"))
# sum=0
# i=1
# while i<num:
#     if num%i==0:
#         sum +=i
#     i+=1
# if sum==num:
#     print("Perfect number")
# else:
#     print("not a perfect number")

# input_string = input("enter string")
# temp = liat(input_string.split(','))
# while True:
#     rev = reversed(str(temp))
#     break
#
# if rev == temp:
#     print(rev)
# else:
#     print("not a palindrome")






