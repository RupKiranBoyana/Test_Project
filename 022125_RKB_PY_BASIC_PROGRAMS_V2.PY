## Find the largest element in a list 

def find_largest(lst):
    return max(lst)

print(find_largest([3,5, 7, 2, 8]))

## Count the frequency of elements in a list 

from collections import Counter 

def count_frequency(lst):
    return dict(Counter(lst))

print(count_frequency([1, 2, 2, 3, 3, 3, 3]))

## Find the second largest element in a list 

def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

print(second_largest([10, 20, 4, 45, 99]))

## check if two strings are anagrams 

from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

print(are_anagrams("listen", "silent"))

## Merge two sorted lists

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

## Find the missing number in an array 

def find_missing_number(arr, n):
    expected_sum = n * (n+1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(find_missing_number([1, 3, 4, 5], 5))

## Find the duplicate numbers in an array 

def find_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None

print(find_duplicates([1, 3, 4, 2, 2]))

## Check if a number is a armstrong number 

def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits ) == n

print(is_armstrong(153))
print(is_armstrong(122))