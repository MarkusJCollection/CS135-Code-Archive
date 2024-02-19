
def anagrams(s):
    # returns a list of all anagrams of string s
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            
            for pos in range(len(w)+1):
                word = w[:pos]+s[0]+w[pos:]
                if word not in ans:
                    ans.append(word)
                
                
        return ans



#Recursive Binary Search

def recBinSearch(x, nums, low, high):
    if low > high:                        # No place left to look, return -1
        return -1
    mid = (low + high) // 2
    item = nums[mid]
    if item == x:                         # Found it! Return the index
        return mid
    elif x < item:                        # Look in lower half
        return recBinSearch(x, nums, low, mid-1)
    else:                                 # Look in upper half
        return recBinSearch(x, nums, mid+1, high)

def rbinSearch(x, nums):
    return recBinSearch(x, nums, 0, len(nums)-1)


#Sample list for testing
import random
random.seed(42)
nums=[]
for i in range(3000):
    n =int(random.random()*10000)
    if n not in nums:
        nums.append(n)
nums.sort()
