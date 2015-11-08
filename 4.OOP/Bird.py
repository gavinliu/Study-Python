class Bird():
    name = 'egg'
    have_fetcher = True
    def move(self, dx, dy):
        position = [0, 0]
        position[0] += dx
        position[1] += dy
        return position

summer = Bird()

print(summer.name)
print(summer.move(10, 2))


class Chicken(Bird):
    name = 'Chicken'
    position = [0, 0]
    def move(self, dx, dy):
        self.position[0] += dx + 2
        self.position[1] += dy + 2
        return self.position

chicken = Chicken()

print(chicken.name)
print(chicken.move(10, 2))


class Duck(Bird):
    def __init__(self, have_fetcher):
        self.name = 'Duck'
        self.have_fetcher = have_fetcher


duck = Duck(False)

print(duck.name)
print(duck.have_fetcher)
print(duck.move(2, 2))
