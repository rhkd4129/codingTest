import random

def number_create():
    number_list= []
    while len(number_list)<=2:
        new_number = random.randint(0,9)
        if new_number not in number_list:
            number_list.append(new_number)
    print("랜덤한 3개의 숫자를 입력했습니다")
    print(number_list)
    return number_list


def number_input():
    guess_number =[]
    while len(guess_number)<=2:
        new_num = int(input(f"{len(guess_number)+1}번째 숫자를 입력하세요"))
        if 0<=new_num<10:
            guess_number.append(new_num)
        else:
            print("다시입력")
    print('입력완료')
    return guess_number

def number_exam(number_list,guess_number):
    strike = 0
    ball = 0
    for x in range(len(number_list)):
        if number_list[x] == guess_number[x]:
            strike+=1
        elif guess_number[x] in number_list:
            ball+=1
    
    return strike,ball

tries = 0
number_list = number_create()
while True:
    number_guess = number_input()
    tries+=1
    
    strike , ball = number_exam(number_list,number_guess)

    if strike ==3:
        print(f"정답 시도횟수:{tries}")
        break
    else:
        print(strike,ball)
        print("다시시도")

