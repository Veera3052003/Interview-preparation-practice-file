"""
1. Reverse a list.
Write a function to reverse a given list in-place, 
without using any built-in functions or creating a new list
"""

print("Reverse a given list without using any built-in functions or creating a new list")

#Using two pointer method
 
def reverse_list(original_list):
    print(f"Original list:{original_list}") 
    left=0 #assigning left value as 0
    right=len(original_list)-1 #assigning right value as len(original_list) - 1 i.e. len(original_list)=6, 6-1=5
    while left<right:  # while left value (0) < right value (5)
        original_list[left],original_list[right]=original_list[right],original_list[left] # assigning the left index[0] value to right index[5] value and assigning right index[5] value to left index[0] value
        left+=1 # Incrementing left value by 1 i.e. 0+1= 1
        right-=1 # Decrementing right value by 1 i.e. 5-1=4
    return original_list #Returning the final list after reversing the values in the list
print(f"Reverse list:{reverse_list([1,2,3,4,5,6])}\n") 

"""
2. Find the missing number.
Given a list of integers from 1 to n, with one number missing,
write a function to find the missing number.
"""

print("Find the missing number in a list using formula")

#using formula

"""
Length of the list + 1 = n, 
Actual sum value = the sum of the natural no. formula value, 
To find the missing no. = actual sum value - sum(list)
"""

def find_missing_number(list):
    print(list)
    n=len(list)+1 
    return ((n*(n+1))//2)-(sum(list)) 
print(f"Missing number:{find_missing_number([1,2,3,5])}\n")

print("Find the missing number in the list using two pointer method")

#using two pointer method
def find_missing_number(list):
    print(list)
    left=list[0] #Assigning left value as list[0] (list --> first value as left value) i.e. left=1
    right=list[-1] #Assigning right value as list[-1] (list --> last value as right value) i.e. right=5
    while left<right: # 1<5, 2<5, 3<5, 4<5
        if left not in list: # if 1 not in list then return 1, 
            return left
        left+=1 #else increase the left value by 1 and again the while loop continues
print(f"Missing number:{find_missing_number([1,2,4,5])}\n")

"""
3. Merge Sorted lists.  
Given 2 sorted lists.   
Write a function to merge them into a single sorted list.
"""

print("Merge two sorted list into a Single sorted list using extend() and sort()")

#Using extend() and sort() functions
 
def merge_sorted_list(list1,list2):
    print(f"List 1:{list1}\nList 2:{list2}")
    list1.extend(list2) # Merging list 1 and list 2 using extend function into a single list --> list1
    list1.sort() # Sorting the merged list, list1 
    return list1 # Returning the sorted list, list1
list1=[1,5,6,9,11]
list2=[3,4,7,8,10]
print(f"Single sorted list:{merge_sorted_list(list1,list2)}\n")

#Creating an empty list

print("Merge two sorted list into a Single sorted list by creating an empty list")

def merge_sorted_lists(list1,list2):
    print(f"List 1:{list1}\nList 2:{list2}")
    final_list=[] # creating an empty list, final_list
    i=j=0 # initialising i and j value as 0 Note:Here, i value is used for accessing list1 index and j value is used for accessing list2 index
    while i<len(list1) and j<len(list2): # This works until both the list list1 and list2 lesser than their respective lengths
        if list1[i]<list2[j]: # if list1[i] value < list2[j] value, 
            final_list.append(list1[i]) # append list1 value into final_list
            i+=1 # This increases only i value
        else: # if list2[j] value < list1[j] value,
            final_list.append(list2[j]) # append list2 value into final_list
            j+=1 # This increases only j value
    final_list.extend(list1[i:]) #Adds the remaining value in list1, if present
    final_list.extend(list2[j:]) #Adds the remaining value in list2, if present
    return final_list #Returns the final sorted list
list1=[1,5,6]
list2=[2,4,7]
print(f"Merge sorted lists into a single list:{merge_sorted_lists(list1,list2)}\n")


"""
4.Remove Duplicates.
Write a function to remove duplicates from a list
while preserving the original order of elements.
"""

#Creating an empty list

print("Remove duplicates from the list while preserving the original order of elements by creating an empty list")

def remove_duplicate(list):
    print(f"The original list:{list}")
    emptylist=[] # Creating an empty list
    i=0 # Initializing i value as 0
    while i<len(list): #This works until i value less than length of the list
        if list[i] not in emptylist: # if list[i] value not in empty list,
            emptylist.append(list[i]) # append the list[i] value, 
            #if list[i] value already present in empty list it does not append the value to the list
        i+=1 # Incrementing the i value by 1
    return emptylist # Returning the final list after removing the duplicate values
print(f"The list after removing the duplicate values:{remove_duplicate([4,7,8,4,7,1,2])}\n")

"""
5. Find the Second Largest Number
Write a function to find the second largest number in a list of integers.
"""

#Using sort function

print("To find the second largest number in a list of integers using sort function")

def second_largest_number(list):
    print(f"The list to find second largest number:{list}")
    list.sort(reverse=True) # Sorting the list in descending order
    return list[1] # Returns the list's 2nd value i.e. Second largest number in the list
print(f"The second largest number:{second_largest_number([30,10,20,4])}\n")

"""
6. Rotate List
Given a list and an integer k
write a function to rotate the list k times to the right.
"""

# Using insert() and pop()

print("To rotate the list k times to the right using insert() and pop()")

def rotate_list_by_k_times(list,k):
    print(f"The Original list:{list}\nRotate {k} times")
    i=0 
    while i<k: # Here: k=2 and i=0, i<k , so this works for 2 times
        list.insert(0,list[-1]) # inserts the copy of the last element at the first and also present in the last position
        list.pop() # pops out the last element so that, the copy of the last element only present in the first position
        i+=1 # Incrementing the i value
    return list # Returning the final list after rotating 2 times
print(f"The list after rotating:{rotate_list_by_k_times([1,2,3,4,5,6],2)}\n")


"""
7. Find Common Elements.
Given two lists, 
write a function to find the common elements between them.
"""

#Using append()
#Creating an empty list

print("To find the common elements in two lists using append() and creating empty list")

def find_common_element(list1,list2):
    print(f"List 1:{list1}\nList 2:{list2}")
    i=0 # initializing i value as 0
    list=[] # creating an empty list
    while i<len(list1): #  This works until i value less than length of the list1
        if list1[i] in list2: # it checks list1 value present in list2 one by one
            list.append(list1[i]) # if list1 value present in list2 then it appends to list
        i+=1 # Increments the value by 1
    return list # Returns the final list, i.e. whichever value repeats returns in a final list.
print(f"The common element in list 1 and list 2:{find_common_element([1,2,3,4,5],[2,3,4,5,6,7])}\n")

"""
8. Largest Continuous Sum
Write a function to find the largest sum of contiguous subarray within a list of integers.
"""

"""
9. Find the Majority Element.
Given a list of integers
write a function to find the majority element 
(an element that appears more than n/2 times).
"""

#Using statistics - mode

import statistics
from statistics import mode
def majority_element(list):
    return(mode(list))
list=[1,2,1,2,2,3]
print(f"The list to find the majority element:{list}")
print(f"The majority element:{majority_element(list)}\n")

"""
10. Sort List of 0s, 1s, and 2s
Given a list containing only 0s, 1s, and 2s
write a function to sort the list in linear time.
"""

#Using sort()

print("Write a function to sort the list of 0s, 1s and 2s in linear time")

def sort_list(list):
    print(f"Original list:{list}")
    list.sort()
    return list
print(f"Sorted list of 0s, 1s and 2s:{sort_list([0,1,2,0,2,1,1,0])}\n")

#Using for and while loop

print("Write a function to sort the list of 0s, 1s and 2s in linear time")

def sortlist(list,n): #Function to sort the 0s, 1s and 2s in the list
    count0=0 # Initializing the count0=0
    count1=0 # Initializing the count1=0
    count2=0 # Initializing the count2=0
    
    for i in range(n): #To count the no. of 0s, 1s and 2s
        if list[i]==0: # If the list[i] value is 0 
            count0+=1  # count0 value is increased by 1
        elif list[i]==1:  # If the list[i] value is 1 
            count1+=1     # count1 value is increased by 1
        else:
            count2+=1     # count2 value is increased by 1
    
    i=0
    while(count0>0): #To update the list
        list[i]=0    #Store all 0's in the beginning
        i+=1
        count0-=1
    while(count1>0): #Then all 1's 
        list[i]=1
        i+=1
        count1-=1
    while(count2>0): #Finally all 2's
        list[i]=2
        i+=1
        count2-=1

    return list
    
list=[0,1,1,2,0,1,2,1,2,0,0,0,1]
print(f"The Original list:{list}")
n=len(list)
print(f"The Sorted list:{sortlist(list,n)}")