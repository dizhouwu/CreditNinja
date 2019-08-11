#!/usr/bin/env python
# coding: utf-8

# In[76]:


class Object:
    def __init__(self, original, original_loc, new_str, new_str_size):
        self.orig= original
        self.original_loc = original_loc
        self.new_str = new_str
        self.new_str_size = new_str_size
        
def strangeSort(mapping, nums):
    obj_list = []
    
    def convert_to_new_str(old_str: str):
        char_pos_all = ''
        for char in old_str:
            char_pos = mapping.index(int(char))
            char_pos_all += str(char_pos)
        
        return char_pos_all
        
    for num in nums:
        num_obj = Object(num,nums.index(num),convert_to_new_str(num),len(convert_to_new_str(num)))
        obj_list.append(num_obj)
    
    sort_list = sorted(obj_list, key = lambda x: int(x.new_str))
    sort_res = []
    
    for obj_item in sort_list:
        obj_tmp = obj_item.orig
        sort_res.append(obj_tmp)
    
    return sort_res


# In[77]:


strangeSort([2,1,4,8,6,3,0,9,7,5,8], ['12','02','4','023','65','83','224','50'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




