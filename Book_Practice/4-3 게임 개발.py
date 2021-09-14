import os
import time

def turn_left() :
    global direction
    direction -= 1
    if direction == -1 :
        direction = 3

def show_map(arr) :
    time.sleep(0.5)
    os.system('cls')
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if i == x and j == y : 
                print('*', end=" ")
            else : 
                print(arr[i][j], end=" ")
        print()


n, m = map(int, input("n, m >>>").split()) # n x n 맵 생성

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
x, y, direction = map(int, input("x, y, direction >>>").split()) # (x,y)에 direction방향을 바라보고 서 있는 캐릭터
print()

field = [] 
tmp = [0 for i in range(m)]
for i in range(n) : 
    tmp = list(map(int, input().split()))
    field.append(tmp)


turn_count = 0
visit_count = 0
while True : 
    show_map(field)
    turn_left()
    if x + dx[direction] >= 0 and x + dx[direction] <= 3 and y + dy[direction] >= 0 and dy[direction] <= 3 :
        if field[x + dx[direction]][y + dy[direction]] == 0 : # 방문할 수 있는 칸의 경우
            x += dx[direction]
            y += dy[direction]
            field[x][y] = 1
            visit_count += 1
            turn_count = 0
        else : 
            if turn_count == 4 :
                break
            else : 
                turn_count += 1
                continue
    
show_map(field)
print("\n방문한 칸의 수 : {0}".format(visit_count))