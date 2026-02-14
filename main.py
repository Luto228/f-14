import random
import time

LON = ['любит', 'не любит']
a = int(input(('Введите число от 1-3:')))
if 0 < a < 3:
    if a == 1:
        YN = str(input('Введи свое имя '))
        LN = str(input('Введи имя половинки '))
        RL = random.choice(LON)
        N = random.randint(10, 50)
        Ro = '🌼'
        ROT = Ro * N
        print(ROT)
        for i in range(N):
            time.sleep(0.25)
            N = N-1
            print(Ro * (N - 1))
            if N%2 == 0:
                print('Любит')
            else:
                print('не любит')
        if N % 2 == 0:
            print(f'{LN} {RL} {YN}! Мои поздравление!')
        else:
            print(f'{LN} {RL} {YN}! Еще более большие поздравления!!')
elif a == 2 or a == 3:
    print('братан, эти кнопки еще в разработке')
else:
    print('Введите число от 1 до 3!')
    