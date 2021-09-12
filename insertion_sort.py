# VERSION 1

a=[6,5,3,1,8,7,2,4]
b=[4,9,3,8,2,7,1,6]

def insertionSort(arr):
    for j in range(1,len(arr)):
        x=arr[j]
        i=j-1
        print(i,j)
        while i>=0 and arr[i]>x:
            print(arr)
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=x
        print(arr)

insertionSort(a)

# VERSION 2

a=[6,5,3,1,8,7,2,4]
b=[4,9,3,8,2,7,1,6]
c=[9,8,7,6,5,4,3,2,1]

def insertionSort(arr):
    for j in range(1,len(arr)):
        x=arr[j]
        i=j-1
        print(i,j)
        while i>=0 and arr[i]>x:
            print(arr)
            arr[i+1]=arr[i]
            arr[i]=x  #ISN'T THIS THE SAME AS BUBBLE SORT?
            i-=1
        print(arr)

insertionSort(c)

#REWRITE IT AGAIN FOR EXTRA PRACTICE

a=[6,5,3,1,8,7,2,4,9]

def insert_sort(arr):
    for j in range(len(arr)):
        x=arr[j]
        i=j-1
        while i>=0 and arr[i]>x:
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=x
        print(arr)

insert_sort(a)
