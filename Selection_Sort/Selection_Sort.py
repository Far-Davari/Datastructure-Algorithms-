# selection sorting
def find_smallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index;
  
  
my_list = [1, 6, -5, 45, -56, 3, 1, -8, -89, -6, -3, 15]

print(find_smallest(my_list))

def selection_sort(arr):
  newArr = []
  for i in range(len(arr)): 
    smallest = find_smallest(arr)
    newArr.append(arr.pop(smallest))
  return newArr
  
print(selection_sort(my_list))