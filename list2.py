def get_item():
    enter_item = input ("Enter a string or a number: ")
    
    return enter_item


def occurs_exactly_once(list, item):
    '''
    returns True if the item occurs
    exactly once in the list, False otherwise
    '''
    if item in list:
        index1 = list.index(item)
        if item in list[index1+1:]:
            return False
        else:
            return True
    else:
        return False
    
item = get_item()

my_item = ["Zenki", str(2), "Dante", str(4), str(2), str(5), "Zenki", "Zasha"]
result =  occurs_exactly_once(my_item, item)

print(f"Does {item} occur exactly once in the list? {result}")
