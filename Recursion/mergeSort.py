#Question 3

def orderedInsertion(item, array):
    n = len(array)

    if(n==0):
        array = [item]

    elif(array[n-1] < item):
        array.append(item)

    else:
        array = orderedInsertion(item, array[0:n-1]) + array[n-1:]
    
    return array


def orderedMerge(fromArray, toArray):
    for item in fromArray:
        toArray = orderedInsertion(item,toArray)
    
    return toArray


def mergeLists(lArray, rArray):
    rlen = len(rArray)
    llen = len(lArray)

    if(rlen == 0):
        return lArray
    elif(llen == 0):
        return rArray
    else:
        minm = min([rArray[0],lArray[0]])
        if(minm == rArray[0]):
            rArray.pop(0)
        else:
            lArray.pop(0)
        return [minm] + mergeLists(lArray,rArray)


def mergeSort(array):
    n = len(array)
    if(n in [0,1]):
        return array
    else:
        m = n//2
        return mergeLists(mergeSort(array[:m]), mergeSort(array[m:]))



def main():
    list1 = [15, 40, 45]
    list2 = [5, 10, 20, 35, 50]
    list3 = [2, 3, 8, 9, 1, 4, 5, 7]
    print("Merged List: ",orderedMerge(list1,list2))
    print("Unordered List: ",list3)
    print("Merge Sorted List: ",mergeSort(list3))

main()


"""
OUTPUT:
python MergeSort.py
Merged List:  [5, 10, 15, 20, 35, 40, 45, 50]
Unordered List:  [2, 3, 8, 9, 1, 4, 5, 7]
Merge Sorted List:  [1, 2, 3, 4, 5, 7, 8, 9]

"""