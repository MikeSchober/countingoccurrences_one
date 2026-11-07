
import math

def bound_search(l, e, start = None, stop = None, bound = None):
    '''
    Takes list of integers sorted in ascending order and the number of occurrences of a given integer using the binary search algorithm
    Args:
        l: sorted list (list)
        e: integer we want to find (int)
        start: index at which we want to start searching (inclusive) (int)---default value is zero
        stop: index before which we want to stop searching (not inclusive) (int)---default value is length of the original list
        bound: string value that determines which bound is found (str)
    Returns:
        if e is found (in upper-bound search): the index number after the last occurrence of e 
        if e is found (in lower-bound search): index number of first occurrence
        if e not found: returns either the first or last index in the list
    '''

    #default values defined
    if start == None: start = 0
    if stop == None: stop = len(l)
    if bound == None: bound = 'top'

    #return start value if not found
    if (stop == start): 
        print(f'return: {start}')
        return start

    #middle value
    mid = math.floor((stop - start) / 2) + start

    print(f'start: {start}, stop: {stop}, mid: {mid}, subarray: {l[start:stop]}')

    if (bound == 'top'):
        if l[mid] > e:
            return bound_search(l,e, start, mid)
        else:
            return bound_search(l,e, (mid + 1), stop)

    if (bound == 'btm'):
        if l[mid] >= e:
            return bound_search(l,e, 0, mid, 'btm')
        else:
            return bound_search(l,e,(mid + 1), stop, 'btm')
        

def count_occur(l, e):
    return (bound_search(l,e)) - (bound_search(l,e, None, None, "btm"))


sorted_list = [2,2,3,3,5]
print(f'{count_occur(sorted_list, 3)} occurrences')
