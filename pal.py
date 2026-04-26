def is_palindrome(input_string):
    left=0
    right=len(input_string)-1
    while left<=right:
        middle=(left+right)//2
        if input_string[left]==input_string[right]:
            left+=1
            right-=1
        else:
            return false
    return True
input_string="ABCDCBA"
print(is_palindrome(input_string))


#given string make it return lexicographically smallest palindrome string

from collections import Counter

def make_palindrome(input_string: str) -> str:
    count = Counter(input_string)
    # Characters with odd counts
    odd_chars = [ch for ch, c in count.items() if c % 2 == 1]
    if len(odd_chars) > 1:
        return "can't be palindrome"

    # sorted list of (char, freq) by character -> ensures lexicographically smallest left half
    sorted_char_items = sorted(count.items(), key=lambda x: x[0])

    # build left part
    left_parts = []
    for ch, freq in sorted_char_items:
        left_parts.append(ch * (freq // 2))
    left = "".join(left_parts)

    # middle (if any)
    middle = ""
    if odd_chars:
        middle_char = odd_chars[0]
        middle = middle_char * (count[middle_char] % 2)

    # right is reverse of left
    right = left[::-1]
    print(right)

    return left + middle + right

# Example
input_string = "abcdddabc"
print(make_palindrome(input_string))  # prints "abcacba"

def medians(values, k):
    n = len(values)
    vals_sorted = sorted(values)
    mpos = (k - 1) // 2
    min_median = vals_sorted[mpos]
    max_median = vals_sorted[n - k + mpos]
    return [max_median, min_median]
arr=[1,2,3]
k=2
print(medians(arr,k))


def minTime(key):
    S = 10**12         # cost of one adjacent swap
    D = S + 1          # cost to delete one character
    # dp_keep = min cost up to now if we keep the characters chosen so far (and maintain sorted prefix)
    # dp_delete = min cost up to now if we deleted some suffix to avoid swaps (not strictly needed separately)
    # We'll use a single variable best = minimal cost so far.
    best = 0
    ones_kept = 0  # count of '1's kept so far
    for c in key:
        if c == '1':
            # Option1: keep this '1' (no immediate cost, increases ones_kept)
            # Option2: delete this '1' at cost D (best + D)
            # choose min: keeping delays cost until encountering 0s (swaps), deleting pays now
            # so update best = min(best (keep), best + D (delete)) but keeping increases ones_kept
            # If delete is chosen we do not increment ones_kept.
            # We should set best = min(best, best + D) -> obviously best <= best + D, so deletion never helps immediately.
            # But deletion may be chosen later when zeros arrive. So we just keep the 1 for now.
            ones_kept += 1
        else:  # c == '0'
            # When a 0 arrives, every previously kept 1 would need one swap to move past this 0.
            # Two choices for this 0:
            #  - keep the 0: pay ones_kept * S to swap those ones past it
            #  - delete the 0: pay D
            cost_keep0 = best + ones_kept * S
            cost_delete0 = best + D
            # choose cheaper and if we keep the 0, ones_kept stays same; if we delete it, ones_kept unchanged as well
            best = min(cost_keep0, cost_delete0)
            # If we kept the 0, it stays in sequence (zeros don't need to be counted further).
            # Note: ones_kept remains unchanged in either branch.
    return best







# Welcome to your Python project!
def max_diff(intervals):
    intervals.sort()
    first=intervals[0]
    sum_diff=first[1]-first[0]
    for start,end in intervals[1:]:
        if first[1]<=start:
            sum_diff+=end-start
        first[1]=end
    return sum_diff

intervals=[[9,12],[10,13],[13,15],[14,17]]
print(max_diff(intervals))



def is_strictly_increasing(arr, left, right):
    for i in range(left, right):
        if arr[i] >= arr[i + 1]:
            return False
    return True

def is_strictly_decreasing(arr, left, right):
    for i in range(left, right):
        if arr[i] <= arr[i + 1]:
            return False
    return True

def find_peak_max_value(arr, left, right):
    # returns the maximum peak value in arr[left..right]
    if left > right:
        return float("-inf")
    mid = (left + right) // 2
    n = len(arr)

    left_neighbor = arr[mid - 1] if mid - 1 >= 0 else float("-inf")
    right_neighbor = arr[mid + 1] if mid + 1 < n else float("-inf")

    # If mid is a peak (plateau peak allowed)
    if arr[mid]>=left_neighbor and arr[mid]>=right_neighbor:
        # Your requirement: still search both sides when ambiguous due to duplicates.
        # We'll search both directions to ensure we get the maximum peak value.
        left_max = find_peak_max_value(arr, left, mid - 1)
        right_max = find_peak_max_value(arr, mid + 1, right)
        return max(arr[mid],left_max, right_max)

    # Ambiguous duplicates: search both directions if both sides equal mid
    if (mid - 1 >= 0 and mid + 1 < n and
        arr[mid - 1] == arr[mid] and arr[mid + 1] == arr[mid]):
        left_max = find_peak_max_value(arr, left, mid - 1)
        right_max = find_peak_max_value(arr, mid + 1, right)
        return max(left_max, right_max)

    # Otherwise follow the higher side
    if right_neighbor > arr[mid]:
        return find_peak_max_value(arr, mid + 1, right)
    else:
        return find_peak_max_value(arr, left, mid - 1)

def find_peak_element_index(arr, left, right):
    if not arr or left > right:
        return None

    # If strictly increasing: return last element index
    if is_strictly_increasing(arr, left, right):
        return right

    # If strictly decreasing: return first element index
    if is_strictly_decreasing(arr, left, right):
        return left

    max_peak_val = find_peak_max_value(arr, left, right)
    n = len(arr)

    # Return an index whose value equals max_peak_val and is a peak
    for i in range(left, right + 1):
        ln = arr[i - 1] if i - 1 >= 0 else float("-inf")
        rn = arr[i + 1] if i + 1 < n else float("-inf")
        if arr[i] == max_peak_val and arr[i] >= ln and arr[i] >= rn:
            return i

    return None  # fallback (shouldn't happen)

# Example
arr = [1, 2, 3, 4, 6, 6, 6, 6, 8, 3, 2, 1]
arr1=[1,2,3,4,9,8,8,8,8,3,2,1]
print(find_peak_element_index(arr1, 0, len(arr) - 1))


'''def mintrucks(n, arr, maxweight):
    if sum(arr) <= maxweight:
        return 1

    if sum(arr) == maxweight * len(arr):
        return maxweight

    arr.sort()
    left = 0
    right = len(arr) - 1
    min_trucks_needed = 0

    while left <= right:
        if left==right:
            min_trucks_needed+=1
            break
            
        if arr[left] + arr[right] == maxweight:
            min_trucks_needed += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] < maxweight:
            left += 1
        else:
            right -= 1

    return min_trucks_needed


n=int(input("please enter the number of test cuses:"))
results = []

for i in range(n):
    input1 = input("please enter two space separated integers: ")
    input2 = input("please enter the array elements separated by space: ")
    a, b = map(int, input1.split())
    arr = list(map(int, input2.split()))    # array
    results.append(mintrucks(a, arr, b))

# Print outputs after all inputs
for ans in results:
    print(ans)'''


#given an array return the maximum of every sub array length k
from collections import deque

def max_subarray(array,k):
    n=len(array)
    if k<=0 or k>n:
        return []
    dp=deque()
    result=[]
    for i in range(n):
        while dp and dp[0]<i-k+1:
            dp.popleft()
        while dp and arr[dp[-1]]<=arr[i]:
            dp.pop()
        dp.append(i)
        
        if i>=k-1:
            result.append(arr[dp[0]])
        
    return result
arr=[2,3,4,5,7,8]
k=3
print(max_subarray(arr,k))
                          
#given an array return the minimum of every sub array length k
from collections import deque

def min_subarray(array,k):
    n=len(array)
    if k<=0 or k>n:
        return []
    dp=deque()
    result=[]
    for i in range(n):
        while dp and dp[0]<i-k+1:
            dp.popleft()
        while dp and arr[dp[-1]]>=arr[i]:
            dp.pop()
        dp.append(i)
        
        if i>=k-1:
            result.append(arr[dp[0]])

    return result
arr=[2,3,4,5,7,8]
k=3
print(min_subarray(arr,k))

def leaders_array(arr):
    result=[arr[-1]]
    last_max=arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i]>last_max:
            last_max=arr[i]
            result.append(last_max)
    result.reverse()
    return result
arr=[16,17,4,3,5,2]
print(leaders_array(arr))


def sort_012(arr):
    low=0
    mid=0
    end=len(arr)-1
    while mid<=end:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[end]=arr[end],arr[mid]
            end-=1
    return arr
arr=[1,2,0,1,2,0,0]
print(sort_012(arr))







                          





















        
        
