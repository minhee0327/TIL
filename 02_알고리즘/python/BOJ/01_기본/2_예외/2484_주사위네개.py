max_value = 0

for _ in range(int(input())):
    dice = sorted(map(int, input().split()))
    if len(set(dice)) == 1:
        max_value = max(max_value, dice[0] * 5000 + 50000)
    elif len(set(dice)) == 2:
        if dice[1] == dice[2]:
            max_value = max(max_value, dice[1]*1000 + 10000)
        else:
            max_value = max(max_value, dice[1] * 500 + dice[2] * 500 + 2000)
    elif len(set(dice)) == 3:
        for i in range(3):
            if dice[i] == dice[i+1]:
                max_value = max(max_value, dice[i] * 100 + 1000)
                break
        max_value = max(max_value, dice[0] * 100 + 1000)

    else:
        max_value = max(max_value, dice[-1]*100)

print(max_value)
