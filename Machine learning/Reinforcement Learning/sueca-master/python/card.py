class Card:
    def __init__(self,id,name,naipe,value):
        self.naipe = naipe
        self.name = name
        self.value = value
        self.id = id

    def getId(self):
        return self.id

    def getNaipe(self):
        return self.naipe

    def getValue(self):
        return self.value

    def getName(self):
        return self.name
