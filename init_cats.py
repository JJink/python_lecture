class Cat :
    def __init__(self, name, color='white'):
        self.name = name
        self.color = color

    def meow(self, name):
        print("my name is {}, color is {}, meow meow".format(self.name, self.color))
        print("speed is ",name)


nabi = Cat("nabi")
nabi.meow(100)

nero = Cat("nero", "black")
nero.meow(200)

mimi = Cat("mimi", "brown")
mimi.meow(300)