#Python Game Application Project

'''컴퓨터가 숫자 3개를 뽑아 3자리 수를 만든 후, 플레이어가 해당 숫자를 맞추는 게임'''

#임의수 3개 뽑아 3자리수 만들기
name = input('당신의 이름을 알려주세요. :')
print('안녕하세요! 야구 게임 세상에 오신걸 환영합니다.', name,'씨!')
print()
print('이 야구 게임은 서로 다른 3개의 숫자로 이루어진 3자리 수를 맞추는 게임입니다.', sep = '\n')
print('입력한 숫자의 자리와 숫자가 맞다 ---> Strike!', sep = '\n')
print('입력한 숫자가 존재하나 자리가 맞지 않다 ---> Ball!', sep = '\n')
print('입력한 숫자 자체가 존재하지 않는다 ---> Out!', sep= '\n')
print('이렇게 3자리 숫자와 숫자의 자리 모두 맞힐 시 게임은 당신의 승리로 끝나게 됩니다!')
print('게임을 시작하도록 하겠습니다!')
print()
import random

#0~9 사이의 수로 3개의 수를 추출하되, 첫자리가 0이면 3자리 수가 안되므로, 해당 경우는 배제
def baseball_game():


    ran_num = []
    while True:
        number = random.randint(0, 9)
        if not number in ran_num:
            ran_num.append(number)      #컴퓨터가 뽑은 3개의 수를 ran_num 변수에 저장
            if ran_num[0] == 0:
                continue
            if len(ran_num) == 3:       #숫자 3개가 선택 되면 끝
                break
    #print(ran_num)

    print('☆★☆★☆★☆★숫자 야구☆★☆★☆★☆★')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


    player_count = 0        #도전횟수

    while player_count < 10:#도전횟수 10회 제한
        strike_count = 0  # 스트라이크 횟수
        ball_count = 0  # 볼 횟수
        out_count = 0  # 아웃 횟수
        player_answer = []  # 플레이어 입력값
        player_count = player_count + 1

        answer = input('숫자 3자리를 입력해 주세요.: ')
        if len(answer) < 3:
            print("잘못 입력하셨습니다.", "재입력 해주세요.")
            continue
        elif answer[0] == answer[1] or answer[0] == answer[2] or answer[1] == answer[2]:
            print("잘못 입력하셨습니다.", "재입력 해주세요.")
            continue
        else:
            for i in range(0,3):
                player_answer.append(int(answer[i:i+1]))

        #print(player_answer)

        for i in range(0,3):
            if player_answer[i] == ran_num[i]:
                strike_count = strike_count + 1
            else:
                j = 0
                for j in range(0,3):
                    if player_answer[i] == ran_num[j]:
                        ball_count = ball_count + 1
            out_count = 3 - (strike_count + ball_count)


        print('%dStrike!!'%strike_count, '%dBall!!'%ball_count, '%dOut!!'%out_count)
        print('남은 기회는', 10-player_count, '번!!')


        if strike_count == 3:
            print('☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★')
            print('%d번 만에 맞추셨습니다!!'%player_count)
            print('☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★')
            break

        if player_count == 10:
            ran_num_answer = ran_num[0]*100 + ran_num[1]*10 + ran_num[2]
            print('☆★☆★☆★☆★Game Over☆★☆★☆★☆★', sep='\n')
            print('정답은 %d입니다.'%ran_num_answer)
            break

baseball_game()
print('재도전 --> Y // 게임 종료 --> N')
replay_game = input('입력해주세요.: ')

if replay_game == 'Y':
   while replay_game =='Y':
    baseball_game()

elif replay_game == 'N':
   print('감사합니다')
   exit()

elif replay_game !='Y' and replay_game !='N':
   print('잘못입력하셨습니다.')
   exit()






















