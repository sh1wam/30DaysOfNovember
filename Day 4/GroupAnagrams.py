# Given an array of strings strs, 
# group the anagrams together. 
# You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap, itterate through strs and create a new variable
        #for each word in strs but sorted. Check if that word is in the hashmap
        #if it is, append the current word in strs to the key value array.
        #if it is not, add the sorted word as the key and the current value as the array value
        myMap = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in myMap:
                myMap[temp].append(word)
            else:
                myMap[temp] = [word]
        return myMap.values()