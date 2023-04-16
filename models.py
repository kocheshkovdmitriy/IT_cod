import random
class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.suit} {self.value}'


class Deck:
    SUIT = ["Черви", "Бубны", "Крести", "Пики"]
    VALUE = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    def __init__(self):
        self.deck = [Card(suit, value) for suit in Deck.SUIT for value in Deck.VALUE]

    def issue_card(self):
        temp = self.deck.pop(self.deck.index(random.choice(self.deck)))
        return temp

    def __len__(self):
        return len(self.deck)

class Player:
    DATA = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10,'Валет': 2, 'Дама': 3, 'Король': 4 , 'Туз': 11}
    def __init__(self, name: str):
        self.name = name
        self.list_crads = list()
        self.score = 0

    def get_card(self,deck: Deck):
        card = deck.issue_card()
        self.list_crads.append(card)
        self.score += Player.DATA.get(card.value)


    def info(self):
        temp = '\n\t'.join([card.__str__() for card in self.list_crads])
        return f'ваш счет: {self.score}\nкарты на руках:\n\t{temp}'

if __name__ == "__main__":
    deck = Deck()
    player = Player('Дима')
    print('Карт в колоде', len(deck))
    for  _ in range(5):
        player.get_card(deck)
    print('Карт в колоде', len(deck))
    print(player.info())
