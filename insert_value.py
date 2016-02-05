# if index is not in range of the list, return false

# start from end
# shift values over +1
# stop when i of forloop == index

def insertValAt(index, myList, value):
    if (index > len(myList) or index < 0):
        return False

    else:
        # loop through the array starting from the end
        i = len(myList)

        # increase length of array
        myList.append(0)

        while i > index:
            myList[i] = myList[i - 1]
            i -= 1

        myList[index] = value

        return myList


