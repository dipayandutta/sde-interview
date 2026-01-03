'''
Find the length of the longest substring without repeating characters.
Input
"abcabcbb"
Output
3   # "abc"
'''

'''
Approach
Sliding window technique
Two pointers + hash set/map
'''
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


string = "abcabcbb"
print(longest_unique_substring(string))
