
# coding: utf-8

# ## 1

# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.

# In[10]:


s=[]
summ=0
flag=True
while flag:
    num=int(input())
    if s:
        if num==0:
            flag=False
        else:
            s.append(num)
    else:
        if num==0:
            print("처음에는 0 말고 다른 숫자를 입력해주세요.")
        else:
            s.append(num)
        
for i in s:
    summ=int(i)+summ

print(summ/len(s))


# ## 2

# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.

# In[12]:


print("Cel  ","Faren  ")
for i in range(1,101):
    print(i,"   ", round(i*1.8+32,2))
    


# ## 3

# Exercise 51 included a table that shows the conversion from letter grades to grade
# points at a particular academic institution. In this exercise you will compute the
# grade point average of an arbitrary number of letter grades entered by the user. The
# user will enter a blank line to indicate that all of the grades have been provided. For
# example, if the user enters A, followed by C+, followed by B, followed by a blank
# line then your program should report a grade point average of 3.1.
# You may find your solution to Exercise 51 helpful when completing this exercise.
# Your program does not need to do any error checking. It can assume that each value
# entered by the user will always be a valid letter grade or a blank line.

# In[13]:


a=dict()
summ=0
a['A+']=4.5
a['A']=4.0
a['B+']=3.5
a['B']=3.0
a['C+']=2.5
a['C']=2.0
a['D']=1.0
a['F']=0.0
g=[]
flag=True

while flag:
    grade=input()
    if grade:
        if grade in ['A+','A','B+','B','C+','C','D','F']:
            g.append(grade)
        else:
            print("학점을 다시 입력해주십시오")
    else:
        flag=False

for i in g:
    summ=a[i]+summ
GPA=summ/len(g)
print(GPA)


# ## 4

# A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and
# 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group
# from the user, with one age entered on each line. The user will enter a blank line to
# indicate that there are no more guests in the group. Then your program should display
# the admission cost for the group with an appropriate message. The cost should be
# displayed using two decimal places.

# In[45]:


baby=0
children=0
adults=0
senior=0
summ=0
flag=True
while flag:
    guest = input()
    if guest:
        if 0<=int(guest)<3:
            baby=baby+1
        elif 2<int(guest)<13:
            children=children+1
        elif 12<int(guest)<66:
            adults=adults+1
        elif 65<int(guest)<150:
            senior=senior+1
        else:
            print("나이를 다시 입력해주십시오")
    else:
        flag=False
        
    

print("Total: $",baby*0+children*14.00+adults*23.00+senior*18.00)
print(baby,"Baby(ies) Free!")
print("Children: $",children*14.00)
print("Adults: $",adults*14.00)
print("Senior: $",senior*18.00)


# ## 5

# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromicwords. Write a program
# that reads a string from the user and uses a loop to determines whether or not it is a
# palindrome. Display the result, including a meaningful output message.

# In[3]:


a=input("단어를 입력해주십시오")
s=''
for i in a:
    s=s+i

if s==a:
    print("Palindrome입니다!")
else:
    print("Palindrome이 아닙니다!")


# ## 6

# In this exercise you will create a program that displays a multiplication table that
# shows the products of all combinations of integers from 1 times 1 up to and including
# 10 times 10. Your multiplication table should include a row of labels across the top
# of it containing the numbers 1 through 10. It should also include labels down the left
# side consisting of the numbers 1 through 10. The expected output from the program
# is shown below:

# When completing this exercise you will probably find it helpful to be able to
# print out a value without moving down to the next line. This can be accomplished
# by added end="" as the last parameter to your print statement. For example,
# print("A") will display the letter A and then move down to the next line. The
# statement print("A", end="") will display the letter A without moving down
# to the next line, causing the next print statement to display its result on the same line
# as the letter A.

# In[13]:


for i in range(1,11):
    print("  ")
    for k in range(1,11):
        print (i*k,"  ", end="")


# ## 7

# The greatest common divisor of two positive integers, n and m, is the largest number,
# d, which divides evenly into both n and m. There are several algorithms that can be
# used to solve this problem, including:
# Initialize d to the smaller of m and n.
# While d does not evenly divide m or d does not evenly divide n do
# Decrease the value of d by 1
# Report d as the greatest common divisor of n and m
# Write a program that reads two positive integers from the user and uses this algorithm
# to determine and report their greatest common divisor.

# In[21]:


a=int(input("first number"))
b=int(input("second number"))
flag=True

if a<b:
    F=b
elif b<a: 
    F=b
else:
    F=a
d=F
while flag and d>0:
    if a%d==0 and b%d==0:
        print(d,"은/는 최대공약수!")
        flag=False
    else:
        d=d-1


# ## 8

# Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then
# it should compute the equivalent decimal number by processing each digit in the
# binary number. Finally, your program should display the equivalent decimal number
# with an appropriate message.

# In[34]:


binary=input()
summ=0

for i in range(len(binary)):
    summ=2**(len(binary)-i-1)*int(binary[i])+summ
print(summ)


# ## 9

# Write a program that converts a decimal (base 10) number to binary (base 2). Read the
# decimal number from the user as an integer and then use the division algorithm shown
# below to perform the conversion. When the algorithm completes, result contains the
# binary representation of the number. Display the result, along with an appropriate
# message.

# In[41]:


word=int(input())
a=[]
s=''
while word>0.5:
    a.append(word%2)
    word=word//2
for i in a:
    s=str(i)+s
print(s)

