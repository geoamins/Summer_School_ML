#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# In[1]:


#arithematic operation(+,-,*,%)
#Conditions
a=10
b=23
if a<b:
    print('a is less than b')
    print("Their sum is:",a+b)
else :
    print('b is greater than a')
    print("Their difference is",a-b)

print("Their product is",a*b)
print("Their division is",a%b)

#_% for remainder division
#_/ for float division 
#_// for integer division


# ## python data structures (lists, tuples, dictionaries, sets)

# In[1]:


#lists
my_list=[42, 3.14, "Hello, World!", True, None, [1, 2, 3], {"key": "value"}, (4, 5), {1, 2, 3}]
#Append
my_list.append('faham')
my_list.insert(3,'khan')
print("heres the modified list",my_list)
#Insert
my_list.insert(2, "Khan")
print(my_list)

#Remove
my_list.remove(2)
print(my_list)

#Sort
my_list.sort()  # Sort the list in ascending order
print(my_list)
#Reverse
my_list.reverse()  # Reverse the order of the list
print(my_list)
    


# In[ ]:


#Tuple
my_tuple=(1,'faham',45,[1,3,4],';',1)  #tuples are immutable 

#index
my_tuple.index(4)
print("index:",my_tuple)
#count 
my_tuple.count(1)
print("appears",my_tuple,"times")

#converting a list to a tuple
New_list = list(my_tuple)
print("The new list is :",New_list)


# In[ ]:


#Dictionary
Ages={"Ashir":21,"Faham":17,"Aizaz":16,"Khalid":21} #contains key and a value
#adding a new key and a value
Ages['Khan']=31
print("Dictionary after adding Khan:",Ages)

#adding multiple elements to a dictionary
Ages.update({"zaid":32,"yasir":32})
print("The updated dictionary is",Ages)
#pop function
Ages.pop("Faham")
print("the value is:",Ages)
#to get the keys of all the values
keys = Ages.keys()
print("Keys:", list(keys))
#to get all the values
values = Ages.values()
print("Values:", list(values))


# In[ ]:


#Sets
my_set={1,45,"faham",3.34,}
#add()
my_set.add("khan")
print("new element is added",my_set)
#clear
#my_set.clear()
#clears all the elements

#Union of two sets or ""
A={1,2,3,5}
Union=my_set.union(A)
print("The union is:",Union)
#Intersection
Intersection=my_set.intersection(A)
print("The intersection is:",intersection)

