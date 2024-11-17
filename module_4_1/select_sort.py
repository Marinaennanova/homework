nums = [4,7,5,2,3,9,12]
def select_sort(ls):
    for i in range(len(ls)):
        low = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[low]:
                low = j
                ls[i],ls[low] = ls[low],ls[i]

select_sort(nums)
print(nums)
