def bubble_sort(l):
    steps = 0
  
    for i in range(len(l)-1):
        print(f"Iterace {i}")

        for j in range(0, len(l)-i-1):
            steps += 1

            if l[j] > l[j+1]:
                print(f"Vyměňuji {l[j]} a {l[j+1]}")
                l[j], l[j+1] = l[j+1], l[j]
        print(l)

    return l, steps


def insertion_sort(l):
    steps = 0

    for i in range(1, len(l)): 
        key = l[i]
  
        j = i-1
        while j >=0 and key < l[j]:
            steps += 1

            print(f"Vyměňuji {l[j]} a {l[j+1]}")
            l[j+1] = l[j]
            j -= 1

        l[j+1] = key
        print(l)

    return l, steps


def selection_sort(l):
    steps = 0

    for i in range(len(l)): 
        min_idx = i

        for j in range(i+1, len(l)): 
            steps += 1

            if l[min_idx] > l[j]: 
                min_idx = j
        
        l[i], l[min_idx] = l[min_idx], l[i]
        print(f"Vyměňuji {l[min_idx]} a {l[i]}")
        print(l)

    return l, steps


l = [6, 4, 1, 3, 2, 5]
print(l)
print("==================")

sort = insertion_sort

print("==================")
l_sorted, steps = sort(l)
