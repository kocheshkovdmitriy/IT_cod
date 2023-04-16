import random
class Card:
    def __init__(self, suit, value):
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

if __name__ == "__main__":
    deck = Deck()
    print('Карт в колоде', len(deck))
    for  _ in range(5):
        print(deck.issue_card())
    print('Карт в колоде', len(deck))