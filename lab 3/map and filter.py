#1
nums = [4, 5, 6, 7, 8]
result=list(map(lambda x: x*2, nums))
print(result)

#2
word=["anel", "car", "safe", "apple"]
result=list(map(lambda x:x.upper() + "!" if len(x)>3 else x.upper(), word ))
print(result)