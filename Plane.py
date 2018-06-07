# retornar o maior numero de possibilidades
# N seria o numero possivel de fileiras
# S e um array de locais marcados
def solution(N, S):
    if not S:
        return N*3

    markedPlaces = S.split()
    
    a = [ [True] * 3 for _ in range(N)]
    for row, col in markedPlaces:
        row = int(row) - 1
        if col in 'ABC':
            a[row][0] = False
        elif col in 'DEFG':
            a[row][1] = False
        elif col in 'HJK':
            a[row][2] = False

    return sum(map(sum, a)) 

if __name__ == '__main__':
    assert 6 == solution(2, "")
    assert 4 == solution(2, "1A 2F 1C")
    #solution(30, "1A 2F 1C 29B 17K 12C 12D") # ValueError: too many values to unpack