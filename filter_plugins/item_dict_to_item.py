#!/usr/bin/python3
#
# itemdict_to_item.py
# This iterates through a list of dictionaries,
#   extracts a dictionary value and combines
#   the values into a list.
#
# Example:
#   my_list[{'my_key': 'value1'},{'my_key': 'value2'}]
#
#   Apply the filter as so:
#     {{ my_list | itemdict_to_item('my_key') }}
#
#   Returned result:
#     ['value1', 'value2']
#
class FilterModule(object):
  def filters(self):
    return {'itemdict_to_item': self.extracted_values}

  def extracted_values(self, passed_list, passed_key):
    # We'll store the list items in here to return.
    ret_list = []
    
    # Iterate through each list item.
    # 'item' represents the dictionary within the list.
    # If the requested key exists, its respective value
    # will be appended to ret_list.
    for item in passed_list:
      if passed_key in item:
        ret_list.append(item[passed_key])
        
    return ret_list
