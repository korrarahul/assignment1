a=input()
length_of_a=len(a)-1
remove_char=a[:length_of_a-2]
resultant=remove_char+a[length_of_a-1]
print(resultant[::-1])
b=int(input("enter the number1 "))
c=int(input("enter the number2 "))
print("sum of b and c is",b+c)
print("sub of b and c is",b-c)
print("mul of b and c is",b*c)
print("div of b and c is",b/c)