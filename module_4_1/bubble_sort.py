 nums = [4,7,5,2,3,9]
def bubble_sort(ls):
    swap = True
    while swap:
        swap = False
        for i in range(len(ls)-1):
            if ls [i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                swap = True
print(bubble_sort(nums))
print(nums)
