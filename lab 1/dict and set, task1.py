#1
def invert_unique(d:dict) -> dict:
    result = {}
    for k,v in d.items():
        if v not in result:
            result[v] = []
        if k not in result:
            result[v].append(k)
    return result
d={"a":1,"b":2,"c":3,"d":4,"e":5}
print(invert_unique(d))

#2
filter_numbers = lambda s: {
    x for x in s
    if x > sum(s)/len(s) and x % 2 != 0 and x % 5 != 0
}
nums = {1, 3, 5, 7, 9, 11, 20, 25}
print(filter_numbers(nums))

#3
def merge_dicts_sum(d1, d2):
    result = {}
    for key in d1:
        result[key] = d1[key]
    for key in d2:
        if key in result:
            result[key] += d2[key]
        else:
            result[key] = d2[key]
    return result
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
print(merge_dicts_sum(a, b))