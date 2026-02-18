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

#4
def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) > 3:
            has_negative = False
            has_even = False

            for num in s:
                if num < 0:
                    has_negative = True
                if num % 2 == 0:
                    has_even = True

            if not has_negative and has_even:
                result.append(s)
    return result
sets = [{1,2,3,4}, {1,-2,3,4}, {1,3,5,7}, {2,4,6,8}]
print(filter_sets(sets))

#5
top_keys = lambda d: [
    k for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0]))
][:5]
data = {
    "apple": 5,
    "banana": 8,
    "cherry": 8,
    "date": 3,
    "fig": 10,
    "grape": 7
}
print(top_keys(data))

#6
def deep_sum(d):
    total = 0
    for value in d.values():
        if isinstance(value, int):
            total += value

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, int):
                    total += item

        elif isinstance(value, dict):
            total += deep_sum(value)
    return total
data = {
    "a": 5,
    "b": [1, 2, 3],
    "c": {"x": 10, "y": [4, 5]}
}
print(deep_sum(data))

#7
unique_even = lambda s1, s2: {
    x for x in s1.symmetric_difference(s2) if x % 2 == 0
}
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(unique_even(a, b))

#8
def sort_dict_by_value_length(d):
    items = []
    for key in d:
        items.append((key, d[key]))
    items.sort(key=lambda x: (len(x[1]), x[0]))
    return items
data = {
    "a": "apple",
    "b": "kiwi",
    "c": "banana"
}
print(sort_dict_by_value_length(data))

#9
def common_elements_all(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for s in sets_list[1:]:
        result = result.intersection(s)
    return result
sets = [{1,2,3}, {2,3,4}, {2,3,5}]
print(common_elements_all(sets))

#10
filter_dict = lambda d: {
    k: sorted([x for x in v if x % 2 != 0])
    for k, v in d.items()
    if [x for x in v if x % 2 != 0]
}
data = {
    "a": [1, 2, 3, 4],
    "b": [2, 4, 6],
    "c": [5, 7, 8]
}
print(filter_dict(data))