score = input()

length = len(score)//2
front = sum([int(x) for x in score[:length]])
back = sum([int(x) for x in score[length:]])

if front == back:
    print("LUCKY")
else:
    print("READY")