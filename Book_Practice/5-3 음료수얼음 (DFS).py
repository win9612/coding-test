def main() :
    n, m = map(int, input("n, m >>>").split())

    field = [] 
    tmp = [0 for i in range(m)]
    for i in range(n) : 
        tmp = list(map(int, input().split()))
        field.append(tmp)

    icecream = 0
    for i in range(n) : 
        for j in range(m) : 
            icecream += dfs(i, j, field)    
    print("얼음 개수 : {0}".format(icecream))  

def dfs(x, y, field) :
    if x < 0 or x >= len(field) or y < 0 or y >= len(field[0]) :
        return 0

    if field[x][y] == 0 : 
        field[x][y] = 1
        dfs(x+1, y, field)
        dfs(x-1, y, field)
        dfs(x, y+1, field)
        dfs(x, y-1, field) 
        return 1
    elif field[x][y] == 1 :
        return 0

if __name__ == "__main__" : 
    main()