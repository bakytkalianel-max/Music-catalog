#1
nums = [4, 5, 6, 7, 8]
result=list(map(lambda x: x*2, nums))
print(result)

#2
word=["anel", "car", "safe", "apple"]
result=list(map(lambda x:x.upper() + "!" if len(x)>3 else x.upper(), word ))
print(result)

#3
nums=[11,12,5,7,8,10,26]
result=list(filter(lambda x: x%2==0, nums))
print(result)

#4
nums=[1,5,-6,7,-2,4,12,24]
result=list(map(lambda x: x/2 if x%2==0 else x*3,
                filter(lambda x:x>5,nums)))
print(result)