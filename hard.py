def find_smallest_num(arr):
  low = arr[0]
  for num in arr[1:]:
    if num < low:
      low = num
  return low

def find_largest_num(arr):
  high = arr[0]
  for num in arr[1:]:
    if num > high:
      high = num
  return high


def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
       if num > largest:
          second_largest = largest
          largest = num
       elif largest > num > second_largest:
          second_largest = num
    return second_largest
def second_smallest(arr):
   smallest = float('inf')
   second_small = float('inf')
   for num in arr:
      if num < smallest:
         second_small = smallest
         smallest = num
      elif smallest < num < second_small:
         second_small = num
   return second_small

def reverse_arr(arr):
   start = 0
   end = len(arr)-1
   while start <= end:
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

def count_freq(arr):
  dic = {}
  for key in arr:
      if key in dic:
         dic[key] += 1
      else:
        dic[key] = 1

  
  print(dic)
   
  # Rotate array by K elements - Block Swap Algorithm
def k_swap(arr, pos):
   
   
  #  pos %= len(arr)
  #  ar1=arr[:pos]
  #  ar2 = arr[pos:]
   
  #  return ar2 + ar1
  # reverse_alogrithm
    ar1 = arr[:pos][::-1]
    ar2 = arr[pos:][::-1]
    ans = ar1+ar2
    return ans[::-1]





def remove_dup(arr):

  return list(set(arr))

def find_symmetric(arr2):
   for i in range(len(arr2)):
      for j in range(i+1):
        #  print(arr2[i][0], arr2[j][1])
         if arr2[i][0] == arr2[j][1] and arr2[i][1] == arr2[j][0]:
            print(arr2[i], arr2[j])
   

arr = [1,2,3,4,5]
arr2 = [(1,2), (2,1), (3,4), (4,3), (5,1), (6,1), (1,6)]


# Maximum Product Subarray in an Array

print(k_swap(arr,2))