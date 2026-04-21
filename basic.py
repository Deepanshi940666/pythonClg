# to print 1st and last element of each list of l1
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[]
for i in l1:
    l2.append(i[0])
    l2.append(i[-1])
print (l2)

# to print sum of max element of each element of l3 list
l3=[[1,2,3],[4,5,6],[7,8,9]]
ans=0
for j in l3:
    ans=ans+max(j)
print(ans)


# to print sum of each element of each element of l3 list
l3=[[1,2,3],[4,5,6],[7,8,9]]
ans=0
for j in l3:
    ans=ans+sum(j)
print(ans)

# to print sum of halfs of list in 2 parts
l4=[2,3,4,5,6,7]
length=len(l4)
sumL=0
sumR=0
mid=length//2
for i in range(0, mid):
    sumL+=l4[i]
print(sumL)
for i in range(mid+1, length):
    sumR+=l4[i]
print(sumR)


# print (sum(l4[:len(l4//2)]),
#     sum(l4[len(l4)//2;]))

# wap which will crete a list with all the element divisible by 3 in btw 4 to 25

l5=[]
for i in range(4, 26):
    if i%3==0:
       l5.append(i)
print(l5)

# or 

l6= [i for i in range(4,26) if i%3==0]
print(l6)

