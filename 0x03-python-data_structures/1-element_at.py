#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    value = my_list[idx]
    if value < 0:
        return None
    return value
