day = 5
month = 'апреля'
temperature = 20


def weather(day: int, month: str, temperature: int):
    print(f'Сугодня {day} {month}. На улице {temperature} градусов.')
    if temperature < 0:
        print('Холодно, лучше отстаться дома.')

if __name__ == "__main__":
    data = [
        (17, 'марта', 10),
        (15, 'октября', 0),
        (1, 'января', -10)
    ]
    for el in data:
        print('*' * 40)
        weather(*el)