import random

def get_name(weather):
    nickname = input('What is your nickname? ')
    print(f'That is funny, hello {nickname}')
    print(f'It is {weather} outside!')
    return nickname

for i in range(1,5):
    print(f'You rolled a: {random.randint(1,20)}')
print('argh!')
name = input('What is your name? ')
print(f'Hello, {name}!')
nick = get_name('sunny')
print(nick)

