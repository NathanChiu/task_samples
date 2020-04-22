# orig = ['one', 'two', 'three',]
# add = ['one', 'two', 'five', 'six]
# remove = ['two', 'five']
# result = ['three', 'six', 'one']

def sort_lists(orig, add, remove):
    result = []
    #create list, excluding elements in remove and elements that have been previously added.
    [result.append(item) for item in orig+add if item not in remove and item not in result]
    #reverse alphabetical
    result = sorted(result, reverse=True)
    #by length
    result = sorted(result, key=len, reverse=True)
    return result


if __name__ == "__main__":
    orig = ['one', 'two', 'three',]
    add = ['one', 'two', 'five', 'six']
    remove = ['two', 'five']
    print(sort_lists(orig,add,remove))

    #double check ordering with 'seven' (same length as 'three', and 'sup' (same length as 'six'))
    orig = ['one', 'two', 'three',]
    add = ['seven', 'one', 'two', 'five', 'six', 'sup']
    remove = ['two', 'five']
    print(sort_lists(orig,add,remove))
