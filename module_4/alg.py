def bubble_sort(ls):
    swap = True
    while swap:
        swap = False
        for i in range(len(ls)-1):
            if ls [i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]
                swap = True


def select_sort(ls):
    for i in range(len(ls)):
        low = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[low]:
                low = j
                ls[i], ls[low] = ls[low], ls[i]