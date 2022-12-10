class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_str(self):
        return f'{self.name}/{self.category}'


class Pokemon(BasePokemon):
    def __init__(self, name, category, weaknesses):
        super().__init__(name, category)
        self.weaknesses = weaknesses


class EmojiMixin:
    emojis = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡'
    }

    def __str__(self):
        


if __name__ == '__main__':
    pokemon = Pokemon('fdf', 'fad', 'sssss')
    print(pokemon.to_str())
