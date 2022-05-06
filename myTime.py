#!/usr/bin/env python
# coding: utf-8

# In[18]:


import time
#%Y-%m-%d-%H:%M:%S
#help(time.strftime)

def GetTime(format):
    return time.strftime(format,time.localtime())

if __name__ == '__main__':
    print(GetTime("%Y-%m-%d"))
    print(GetTime("%Y-%m-%d-%H:%M:%S"))
    print(GetTime("%Y-%m-%d-%H:%M:%S %a %A"))
    
    


# In[ ]:




