def Count_of_Array_Element(A):
    count = 0
    n = len(A)

    for i in range(n):
        has_greater = False
        for j in range(n):
            if i != j and A[j] > A[i]:
                has_greater = True
                break
        if has_greater:
            count += 1

    return count


A = list(map(int,input().split()))
result = Count_of_Array_Element(A)
print(result)  
