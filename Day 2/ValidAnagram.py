# Given two strings, s and t, return True
# if t is an anagram of s, and False otherwise

def isAnagram(s, t):
    s_freq = {}
    t_freq = {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1
    
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
        
    return s_freq == t_freq