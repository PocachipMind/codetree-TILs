n, m = map(int,input().split())

edge = []
for _ in range(n):
    edge.append([])

for _ in range(m):
    k, m = map(int,input().split())
    edge[k-1].append(m-1)

visited = []

def dfs(x):
    if x in visited:
        return
    visited.append(x)
    for i in edge[x]:
        dfs(i)

dfs(0)

print(len(visited)-1)