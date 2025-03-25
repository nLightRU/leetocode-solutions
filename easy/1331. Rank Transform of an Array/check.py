from typing import List, Dict

target_arr = [37,12,28,9,100,56,80,5,12]

def create_sorted(arr: List[int]) -> List[Dict]:
    res = []
    for i, value in enumerate(arr):
        res.append({'value':  value, 'index': i})
    
    return sorted(res, key=lambda x: x['value'])

arr_sorted = list(create_sorted(target_arr))
cur_top = arr_sorted[0]['value'] # current_top
cur_rank = 1 # current_rank

for elem in arr_sorted:
    print(elem)
    value = elem['value']
    index = elem['index']
    if value == cur_top:
        target_arr[index] = cur_rank
    else:
        cur_top = value
        cur_rank += 1
        target_arr[index] = cur_rank


# assert target_arr == [5,3,4,2,8,6,7,1,3]
print(target_arr)
