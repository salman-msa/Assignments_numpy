#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[4]:


arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
arr1


# In[5]:


arr1.reshape(2,5)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[6]:


arr2 = np.array([[0,1,2,3,4],[5,6,7,8,9]])
arr3 = np.array([[1,1,1,1,1],[1,1,1,1,1]])
np.vstack((arr2,arr3))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[7]:


np.hstack((arr2,arr3))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[8]:


arr = np.array([[0,1,2,3,4],[5,6,7,8,9]])
arr.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[14]:


arr = np.array([[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14]])
arr


# In[15]:


arr.reshape(-1)


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[16]:


arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
arr


# In[17]:


arr.reshape(5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[24]:


arr = np.arange(25).reshape(5,5)
print(arr)
np.square(arr)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[37]:


np.random.seed(6)
arr8 = np.random.randint(50, size=(5,6))
print(arr8)
np.mean(arr8)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[40]:


np.std(arr8)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[39]:


np.median(arr8)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[42]:


arr8.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[44]:


arr12 = np.arange(16).reshape(4,4)
print(arr12)
np.diagonal(arr12)


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[45]:


np.linalg.det(arr12)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[50]:


arr = np.arange(10)
print(arr)
print(np.percentile(arr, 5))
print(np.percentile(arr, 95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[58]:


arr = np.arange(15).reshape(5,3)
arr_sum = np.sum(arr)
np.isnan(arr_sum)

