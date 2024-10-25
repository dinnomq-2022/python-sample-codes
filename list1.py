def count_containing(list, character):
    '''
    returns the number of items in list that contain
    the given character
    '''
    count = 0
    for item in list:
        if character in item:
            print(character,"exists in string", item)
            count+=1
        elif character not in item:
            print(character,"does not exists in string", item)
            count+=1
    return count
count_containing(["Winona","Winonna","Jose"],"in")