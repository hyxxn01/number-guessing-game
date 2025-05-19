import random 

answer = random.randint(1, 100) 
print("업다운 게임을 시작합니다! (1~100 사이 숫자를 맞혀보세요)") 

while True:
    guess = input("숫자를 입력하세요: ")

    if not guess.isdigit():   
        continue

    guess = int(guess) #

    if guess < answer:
        print("UP!")
    elif guess > answer:
        print("DOWN!")
    else:
        print("정답입니다!")
        break
    
    