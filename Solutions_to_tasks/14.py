

class Blues:

    def __init__(self, *notes):
        self.music = '-'.join(notes)

    def __add__(self, a):
        return Blues(self.music + a.music)

    def __iadd__(self, a):
        self.music += str(a)
        return self
    
    def __str__(self):
        return self.music
    
blu = Blues('до', 'ми_бемоль', 'фа', 'ми_бемоль')
blu += 'ДО'
print(blu)
blu1 = Blues('ля', 'до', 'ре', 'МИ')
blu2 = blu1 + blu
print(blu1, blu2, sep='\n')

