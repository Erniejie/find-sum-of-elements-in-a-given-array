#program to find sum of elements in given array
#Computer Programming Tutor_yt_April 28,2021

"FUNCTION TO ADD THE SUM OF THE ELEMENT"

def sumarray(arr):
    # initialise a variable sum
    sum =0
    #iterate the array and each element
    for k in arr:
        sum = sum + k

    return (sum)
arr=[]

# input value to list
arr = [12,3,4,15,17,23,67]

#Calling Function to Sum Array

result = sumarray(arr)

# display sum
print("Sum of the array is: ",result)
