def rotate_left(lst, k):
    n = len(lst)
    
    if n == 0:
        return lst
    
    k = k % n
    return lst[k:] + lst[:k]


# Input lena
lst = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter k value: "))

# Function call
result = rotate_left(lst, k)

print("Rotated list:", result)
