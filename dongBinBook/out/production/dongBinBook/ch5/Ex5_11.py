from collections import deque

def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        x, y = que.popleft()
        print(x,y)
    print("종료되었습니다")

bfs(0,0)