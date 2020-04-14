#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

# this will choose one and remove it
def choose_and_remove(items):
    # pick an item index
    if items:
        index = random.randrange( len(items) )
        return items.pop(index)
    # nothing left!
    return None

def get_max_list(l):
    index=None
    if(l[0]==l[1]):
        index=random.randrange(0,2)
    elif(l[0]>l[1]):
        index=0
    else:
        index=1
    return(index)


# In[ ]:




