def solution(A):
    #aa = sorted(A)
    swaps = 0

    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            swaps += 1
            aaa = A[i]
            A[i] = A[i+1]
            A[i+1] = aaa

            '''if i+2 <= len(A)-1 and aaa > A[i+2]:
                A[i+1] = A[i+2]
                A[i+2] = aaa'''

    if swaps <= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    assert True == solution([1, 5, 3, 3, 7])
    assert False == solution([1, 5, 9, 3, 3, 7])