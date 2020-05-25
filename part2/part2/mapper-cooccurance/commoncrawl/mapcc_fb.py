#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:
import sys, re

# size of the context window
window = 2
cc =0
# input comes from STDIN (standard input)
fileaz=sys.stdin
wd_occ = ["facebook","user","social","compani","site","stock","share","peopl","financ","twitter"]
for line in sys.stdin:
    #for line in sys.stdin:
    for i in wd_occ:
        line = line.strip()
        line=line.lower()
    # split the line into words
        #if i in line:
        words = line.split()
        for j in xrange(len(words)-1):
            #for k in range(i+1,len(words)):
            if words[j] == i:
                print ("%s-%s\t%s" % (words[j],words[j+1], 1))


# In[ ]:




