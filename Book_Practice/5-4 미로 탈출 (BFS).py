def main() :
    n, m = map(int, input("n, m >>>").split())

    field = [] 
    for i in range(n) : 
        field.append(list(map(int, input())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    x = 0
    y = 0

    result = bfs(x,y, field)
    print(result)


def bfs(x, y, field) :
    if x < 0 or x >= 5 or y < 0 or y >= 6 or field[x][y] == 0 :
        print("문제!")
        return 0
    
    if x == len(field)-1 and y == len(field[0])-1 :
        print("완료: {0}".format(field[x][y] + 1))
        return field[x][y] + 1
    else : 
        print("진행중: {0}".format(field[x][y] + 1))
        field[x][y] += 1
        bfs(x+1, y, field)
        bfs(x-1, y, field)
        bfs(x, y+1, field)
        bfs(x, y-1, field)
    



if __name__ == "__main__" : 
    main()