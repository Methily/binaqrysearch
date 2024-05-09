#binary search

def binrysrch(ar,key):
    big=0
    end=len(ar)-1
    mid=0
    while(big<=end):
        mid=(big+end)//2
        if(ar[mid]<key):
            big=mid+1
        elif(ar[mid]>key):
            end=mid-1
        else:
            return mid
    return -1

ar=[9,34,54,1,12,66,19]
key=int(input("Enter the value to be searched :"))
m=binrysrch(ar,key)
if m==-1:
    print("found it")
else:
    print("didnt find it!")