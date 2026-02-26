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

#11
def group_by_length(words):
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        if word not in result[length]:
            result[length].append(word)
    return result
words = ["cat", "dog", "apple", "car", "dog", "banana"]
print(group_by_length(words))

#12
filter_strings = lambda s: {
    x for x in s
    if x.isalpha() and len(x) > 4 and len(set(x)) == len(x)
}
data = {"apple", "hello", "world", "abcde", "abcda"}
print(filter_strings(data))

#13
def invert_dict_strict(d):
    result = {}
    value_count = {}
    for key in d:
        value = d[key]
        if value not in value_count:
            value_count[value] = 0
        value_count[value] += 1
    for key in d:
        value = d[key]
        if value_count[value] == 1:
            result[value] = key
    return result
data = {"a": 1, "b": 2, "c": 1}
print(invert_dict_strict(data))

#14
def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    if k > len(items):
        k = len(items)

    result = set()
    for i in range(k):
        result.add(items[i][0])
    return result
nums = [1,1,2,2,2,3,3,4]
print(top_k_frequent(nums, 2))

#15
filter_dict = lambda d: {
    k: v for k, v in d.items()
    if v >= sum(d.values())/len(d) and v % 2 != 0
}
data = {"a": 5, "b": 2, "c": 9, "d": 4}
print(filter_dict(data))

#16
data = {"a": 10, "b": 21, "c": 33, "d": 4, "e": 55}
empty_data = {}
clean_dict = lambda d: {
    k: v for k, v in d.items()
    if len(d) > 0 and v >= (sum(d.values()) / len(d)) and v % 2 != 0
}
print(f"С данными: {clean_dict(data)}")
print(f"Пустой: {clean_dict(empty_data)}")

#17
clean_dict = lambda d: (
    lambda avg: {k: v for k, v in d.items() if v >= avg and v % 2 != 0}
)(sum(d.values()) / len(d) if d else 0)
print(f"С данными: {clean_dict(data)}")

#18
def sort_dict_by_value_sum(d):
    aggregated_list = []
    for key, values in d.items():
        current_sum = 0
        for number in values:
            current_sum += number
        aggregated_list.append((key, current_sum))
    aggregated_list.sort(key=lambda x: (-x[1], x[0]))
    return aggregated_list
if __name__ == "__main__":
    data = {
        "apple": [10, 20, 30],
        "banana": [50, 10],
        "cherry": [5, 5],
        "date": [100]
    }
result = sort_dict_by_value_sum(data)
print(result)

#19
def filter_by_digit_sum(nums):
    items_list = []
    for key in nums:
        values = nums[key]
        total_sum = 0
        for num in values:
            total_sum += num
        items_list.append((key, total_sum))
    n = len(items_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            key1, sum1 = items_list[j]
            key2, sum2 = items_list[j + 1]
            if (sum1 < sum2) or (sum1 == sum2 and key1 > key2):
                items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]
    return items_list
if __name__ == "__main__":
    data = {
        "apple": [10, 20, 30],
        "banana": [50, 10],
        "cherry": [5, 5],
        "date": [100]
    }
result = filter_by_digit_sum(data)
print(result)
#20
top3_keys = lambda d: sorted(
    d.keys(),
    key=lambda k: (d[k], len(k))
)[:3]
data = {
    "apple": 5,
    "kiwi": 2,
    "banana": 2,
    "pear": 4,
    "plum": 1
}
print(top3_keys(data))

#21
def count_leaf_values(d):
    count = 0
    for value in d.values():
        if isinstance(value, dict):
            count += count_leaf_values(value)
        elif isinstance(value, list):
            count += len(value)
        else:
            count += 1
    return count
data = {
    "a": 5,
    "b": [1, 2, 3],
    "c": {
        "d": 10,
        "e": [7, 8],
        "f": {
            "g": 100
        }
    }
}
print(count_leaf_values(data))

#22
result = lambda s1, s2: {
    x for x in s1
    if x > (sum(s2) / len(s2)) and x not in s2
}
a = {1, 5, 10, 20}
b = {2, 4, 6}
print(result(a, b))

#23
def group_by_last_letter(words):
    result = {}
    for word in words:
        if not word:
            continue
        last_letter = word[-1]
        if last_letter not in result:
            result[last_letter] = []
        if word not in result[last_letter]:
            result[last_letter].append(word)
    return result
words = ["apple", "banana", "grape", "avocado", "pineapple", "banana"]
print(group_by_last_letter(words))

#24
def union_of_filtered_sets(sets_list):
    result = set()
    for s in sets_list:
        for num in s:
            if num > 10 and num % 2 != 0:
                result.add(num)
    return result
sets_list = [
    {5, 11, 14, 17},
    {3, 9, 13, 20},
    {21, 8, 10, 15}
]
print(union_of_filtered_sets(sets_list))

#25
from functools import reduce
from operator import mul
result = lambda d: {
    k: reduce(mul, [x for x in v if x > 0], 1)
    for k, v in d.items()
    if any(x > 0 for x in v)
}
data = {
    "a": [1, -2, 3],
    "b": [-5, -10],
    "c": [4, 5],
    "d": [0, -1, 2]
}
print(result(data))

#26
def remove_elements_with_common_digits(s):
    digit_count = {}
    for num in s:
        digits = set(str(abs(num)))
        for d in digits:
            if d not in digit_count:
                digit_count[d] = 0
            digit_count[d] += 1
    result = set()
    for num in s:
        digits = set(str(abs(num)))
        has_common = False
        for d in digits:
            if digit_count[d] > 1:
                has_common = True
                break
        if not has_common:
            result.add(num)
    return result
s = {123, 456, 178, 890, 345}
print(remove_elements_with_common_digits(s))

#27
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
result = lambda d: {
    k: v
    for k, v in d.items()
    if is_prime(v) and len(k) % 2 == 1
}
data = {
    "one": 2,
    "two": 4,
    "three": 5,
    "four": 7,
    "six": 11
}
print(result(data))

#28
def sorted_unique_chars(strings):
    unique_chars = set()
    for s in strings:
        for ch in s:
            if not ch.isdigit() and ch != ' ':
                unique_chars.add(ch)
    result = list(unique_chars)
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result
strings = ["Hello 123", "World 456", "Hi!"]
print(sorted_unique_chars(strings))


#29
result = lambda d: sorted(
    d.keys(),
    key=lambda k: (abs(d[k]) % 10, k)
)
data = {
    "apple": 23,
    "banana": 17,
    "cherry": 34,
    "date": 27,
    "fig": 14
}
print(result(data))

#30
def partition_by_sum_parity(s):
    even_sum_set = set()
    odd_sum_set = set()
    for num in s:
        digit_sum = 0
        n = abs(num)
        while n > 0:
            digit_sum += n % 10
            n //= 10
        if num == 0:
            digit_sum = 0

        if digit_sum % 2 == 0:
            even_sum_set.add(num)
        else:
            odd_sum_set.add(num)
    return (even_sum_set, odd_sum_set)
s = {12, 33, 41, 7, 20}
print(partition_by_sum_parity(s))

#31
result = lambda d: {
    k: v
    for k, v in d.items()
    if len(v) == len(set(v)) and all(len(s) > 3 for s in v)
}
data = {
    "a": ["apple", "pear", "melon"],
    "b": ["cat", "lion", "tiger"],
    "c": ["blue", "blue", "green"],
    "d": ["tree", "rock"]
}
print(result(data))

#32
def pairwise_intersections(sets_list):
    result = []

    if len(sets_list) < 2:
        return result
    for i in range(len(sets_list) - 1):
        set1 = sets_list[i]
        set2 = sets_list[i + 1]
        intersection = set()
        for elem in set1:
            if elem in set2:
                intersection.add(elem)
        result.append(intersection)
    return result
sets_list = [
    {1, 2, 3},
    {2, 3, 4},
    {3, 4, 5},
    {10}
]
print(pairwise_intersections(sets_list))

#33
result = lambda d: (
    lambda overall_avg: {
        k: v
        for k, v in d.items()
        if len(v) > 0 and (sum(v) / len(v)) > overall_avg
    }
)(
    sum(sum(v) for v in d.values()) /
    sum(len(v) for v in d.values())
)
data = {
    "a": [1, 2, 3],
    "b": [10, 20],
    "c": [4, 5, 6]
}
print(result(data))

#34
def top_k_smallest_unique(nums, k):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    n = len(unique_nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unique_nums[j] > unique_nums[j + 1]:
                unique_nums[j], unique_nums[j + 1] = unique_nums[j + 1], unique_nums[j]
    result = set()
    count = 0
    for num in unique_nums:
        if count >= k:
            break
        result.add(num)
        count += 1
    return result

#35
result = lambda d: {
    k: v
    for k, v in d.items()
    if v % 3 != 0 and len(k) % 2 != 0
}
data = {
    "one": 4,
    "two": 9,
    "four": 5,
    "six": 7,
    "ten": 12
}
print(result(data))

#36
def all_subsets_of_size_k(s, k):
    elements = list(s)
    result = []

    def backtrack(start, current_subset):
        if len(current_subset) == k:
            result.append(set(current_subset))
            return
        for i in range(start, len(elements)):
            current_subset.append(elements[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
    if k > len(s) or k < 0:
        return []
    backtrack(0, [])
    return result
s = {1, 2, 3}
k = 2
print(all_subsets_of_size_k(s, k))

#37
from math import factorial
result = lambda d: {
    k: factorial(v) if v < 6 else v
    for k, v in d.items()
}
data = {
    "a": 3,
    "b": 5,
    "c": 6,
    "d": 2
}
print(result(data))

#38
def multi_symmetric_difference(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for i in range(1, len(sets_list)):
        current_set = sets_list[i]
        new_result = set()
        for elem in result:
            if elem not in current_set:
                new_result.add(elem)
        for elem in current_set:
            if elem not in result:
                new_result.add(elem)
        result = new_result
    return result
sets_list = [
    {1, 2, 3},
    {3, 4},
    {4, 5}
]
print(multi_symmetric_difference(sets_list))