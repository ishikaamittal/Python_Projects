import random
from logo import logo, vs
from data import data

game_over = True
print(logo)
data1 = random.choice(data)
data2 = random.choice(data)
score = 0

while game_over:

    print(f"Compare: {data1['name']} who is {data1[ 'description']}, {data1['country']}")
    print(vs)
    print(f"Against: {data2['name']}  who is {data2[ 'description']}, {data2['country']}")

    ask = input("\nChoose 'A' or 'B: ")
    if ask == 'A':
        if data1['follower_count'] > data2['follower_count']:
            data1 = data2
            data2 = random.choice(data)
            score = score+1
            print(f"Yea! you won{score}")
        elif data1['follower_count'] < data2['follower_count']:
            game_over = False
            print(f"Game over! your score is {score}")
    else:
        if data1['follower_count'] < data2['follower_count']:
            data1 = data2
            data2 = random.choice(data)
            score = score+1
            print(f"Yea! you won{score}")
        elif data1['follower_count'] > data2['follower_count']:
            game_over = False
            print(f"Game over! your score is {score}")
