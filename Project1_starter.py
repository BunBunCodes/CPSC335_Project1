# Author: Edith Cruz
# CPSC 335
# Project 1

import re

# turns a single list into a double list
def turnDouble(listA):
    res = []
    i = 0
    
    while i < len(listA)-1:
        res.append([listA[i], listA[i+1]])
        i += 2
    
    return res

#combines two lists into one and sorts them by order of their beginning time
def sortLists(listA, listB):
    size1 = len(listA)
    size2 = len(listB)
    res = []                         # will store the resulting list of all the times sorted
    i, j = 0, 0                         # instatiating the variables needed
    
    while i < size1 and j < size2:
        if listA[i] < listB[j]:
            res.append(listA[i])
            i += 1
 
        else:
            res.append(listB[j])
            j += 1
            
    res = res + listA[i:] + listB[j:]
    return res
    # print("The combined sorted list is : " + str(res))

# turns TimeStamps strings into ints for easier arithmetic 
def turnToInt(timeStamp):
    subStrs = timeStamp.split(":")
    first = subStrs[0]
    second = subStrs[1]
    totalTime = int(first)*60 + int(second)
    return totalTime   
    
# makes list of gaps in free time
def freeTime(listB, timeInt):
    res = []
    size1 = len(listB)
    workTimes.sort()
    finalStart = turnToInt(workTimes[2])
    finalEnd = turnToInt(workTimes[1])
    tempEnd = turnToInt(listB[0][0])
    if tempEnd-finalStart >= int(timeInt):
        res.append([workTimes[2], listB[0][0]])

    i = 1
    while i < size1:
        end = turnToInt(listB[i][0])
        start = turnToInt(listB[i-1][1])
        if end - start >= int(timeInt):
            res.append([listB[i-1][1], listB[i][0]])
        i += 1
    
    tempStart = turnToInt(listB[size1-1][1])
    if finalEnd - tempStart >= int(timeInt):
        res.append([listB[size1-1][1], workTimes[1]])
        
    return res
         
# Takes a sorted list and finds any overlapping intervals of time and commbines them
def combineIntervals(listA):
    intIndex = 0

    for  i in listA:
        if i[0] > listA[intIndex][1]:
            intIndex += 1
            listA[intIndex] = i
        else:
            listA[intIndex] = [listA[intIndex][0], i[1]]
            
    return listA[:intIndex+1]
      
        
# main code
file1 = open("input.txt", 'r')              # opening file input.txt and setting to reading mode
file2 = open("output.txt", 'w')             # creating file output.txt and setting to writing mode

# a while loop that reads lines from the file so long as its not empty
# we use the regex library to sort out our timestamps
while True:
    content = file1.readline()
    if not content:                         # breaks the for loop if content is no longer true
        break
    
    list1 = turnDouble(re.findall(r'(\d+:\d+)',content))    # stores and turns the first line into a double list
    
    content = file1.readline()
    workTimes = re.findall(r'(\d+:\d+)',content)            # stores the first workTimes in a list
    
    content = file1.readline()
    list2 = turnDouble(re.findall(r'(\d+:\d+)',content))    # stores and turns the third line into a double list
    
    content = file1.readline()
    workTimes += re.findall(r'(\d+:\d+)',content)           # adds on the other workTimes onto the existing list

    meetingLength = file1.readline()        # will now store the amount of minutes needed for the meeting
    
    content = file1.readline()              # this line is needed to get rid of the whitespace between entries
    
    busyTimes = combineIntervals(sortLists(list1, list2))
    finalArr = freeTime(busyTimes, meetingLength)
    s = "" + str(finalArr) + "\n"
    file2.write(s)

file1.close()
file2.close()

