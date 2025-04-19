import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use("TkAgg")
import math
def linear_search(list1,n,key):
    #searching list1 sequentially
    for i in range(0,n+1):
        if(list1[i]==key):
            return i
    return -1
thevalues=[10,20,30,40,50,60,70]
target=int(input("enter key to search:"))
tmp=linear_search(thevalues,len(thevalues)-1,target)
if tmp==1:
    print("target value not found in list")
else:
    print("target value found in list at location",tmp)


plt.title("linear-time complexity is O(log n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()