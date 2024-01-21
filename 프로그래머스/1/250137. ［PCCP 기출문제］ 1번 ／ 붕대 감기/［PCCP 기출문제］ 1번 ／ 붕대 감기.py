def solution(bandage, health, attacks):
    max_health = health
    answer = health
    cnt = 0
    for i in range(1, attacks[-1][0]+1):
        if i == attacks[0][0]:
            health -= attacks[0][1]
            cnt = 0
            if health <= 0:
                answer = -1
                break
            attacks.pop(0)
            continue
        if cnt != bandage[0]:
            health += bandage[1]
            cnt += 1
        if cnt == bandage[0]:
            health += bandage[2]
            cnt = 0
        if health >= max_health:
            health = max_health
    if answer != -1:
        answer = health
    return answer