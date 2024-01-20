def solution(land):
    dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    answer = [0] * len(land[0])
    visited = [[0] * len(land[0]) for _ in range(len(land))]
    for i in range(len(land[0])):
        for j in range(len(land)):
            k = set()
            if land[j][i] and not visited[j][i]:
                cnt = 1
                visited[j][i] = 1
                stack = [(j, i)]
                k.add(i)
                while stack:
                    y, x = stack.pop()
                    for dy, dx in dydx:
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < len(land) and 0 <= nx < len(land[0]) and land[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            stack.append((ny, nx))
                            k.add(nx)
                            cnt += 1
                for u in k:
                    answer[u] += cnt
    answer = max(answer)
    return answer