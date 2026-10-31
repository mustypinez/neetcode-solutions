class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        items = collections.defaultdict(int)
        for character in s:
            items[character] += 1
        for character in t:
            items[character] -= 1
        
        for key in items:
            if items[key] != 0:
                return False
        return True
