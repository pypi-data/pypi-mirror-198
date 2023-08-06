import random

class b:
    def __init__(self):
        data = {
            '1': [1, ['+', '-']],
            '2': [1, ['+', '-', '*']],
            '3': [2, ['+', '-', '*']]
        }
        while True:
            option = ''
            while option not in data:
                option = input('What difficulty do you want?\n1. Easy\n2. Medium\n3. Hard\n> ')
            correct = 0
            for i in range(10):
                if option != '3':
                    question = f'{random.randint(0, 9)}{random.choice(data[option][1])}{random.randint(0, 9)}'
                else:
                    question = f'{random.randint(0, 9)}{random.randint(0, 9)}{random.choice(data[option][1])}{random.randint(0, 9)}{random.randint(0, 9)}'
                answer = input(f'{question}: ')
                if int(answer) == eval(question):
                    correct += 1
                    print('Correct!')
                else:
                    print(f'Incorrect, the answer was {eval(question)}')
            print(f'Your final score was {correct}/10')
            if input('Do you want to go again?\n1. Yes\n2. No\n> ') == '2':
                break