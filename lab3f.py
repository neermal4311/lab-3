#!/usr/bin/env python3

# Author ID: ngautam11

# Global list called my_list
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    new_item = ordered_list[-1] + 1  # Get the last item and add 1
    ordered_list.append(new_item)      # Append the new item to the list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove list from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)  # Remove item if it exists in the list

# Main code
if __name__ == '__main__':
    print(my_list)  # Output the initial list
    add_item_to_list(my_list)  # Add new items
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # Output the modified list after additions
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specified items
    print(my_list)  # Output the final list after removals
