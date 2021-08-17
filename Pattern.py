
# coding: utf-8

# In[13]:


#3-* * *


n=int(input("Enter number:"))
for number in range(n):
    print("*",end =' ')


# In[6]:


#square patter with "*"
#3- * * *
#   * * *
#   * * * 

n=int(input("Enter number:"))
for number in range(n):
    print("* " * n)


# In[8]:


#square pattern with numbers
n=int(input("Enter number:"))
for i in range(n):
    print((str(i+1)+" ")*n)


# In[9]:


#square pattern with alphabet
n=int(input("Enter number:"))
for i in range(n):
    print((chr(65+i)+" ")*n)


# In[19]:


#Right angled triangle with "*"
n=int(input("Enter number of rows :"))
for i in range(n):
        print((i+1)* "* ",end ="  ")
        print()
    


# In[21]:


#inverse right angled triangle
n=int(input("Enter number of rows :"))
for i in range(n):
    print("* " * (n-i))


# In[18]:


#Right angled triangle with "*"
n=int(input("Enter number of rows :"))
for i in range(n):
    for j in range(i+1):
        print("* ",end =" ")
    print()


# In[5]:


#print pyramid with "*"
n=int(input("Enter number of rows :"))
for i in range(n):
    print(" "*(n-i-1)+"* " * (i+1))


# In[7]:


#print inverted pyramid
n=int(input("Enter number of rows :"))
for i in range(n):
    print(" "*(i)+"* " * (n-i))


# In[15]:


#Print Diamond
n=int(input("Enter number of rows :"))
for i in range(n):
    print(" "*(n-i-1)+"* " * (i+1))
for i in range(n-1):
    print(" "*(i+1)+"* "*(n-i-1))

