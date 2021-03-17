class Entity:
    def __init__(self, x, y ,field):
        self.x = x
        self.y = y
        self.field = field
        self.field.entities.append(self)
    def move(self, direction):
        if direction == "su"  and self.y > 0:
            self.y -= 1
        elif direction == "giù"  and self.y < field.h - 1:
            self.y += 1
        elif direction == "sinistra"  and self.x > 0:
            self.x -= 1
        elif direction == "destra"  and self.x < field.w - 1:
            self.x += 1


class Monster(Entity):
    def __init__(self, x, y, name, damage, field):
        super().__init__(x, y, field)
        self.name = name
        self.hp = 10
        self.damage = damage

    def info(self):
        print("nome:", self.name, "hp:", self.hp, "/10", "posizione:", self.x, ",", self.y)


class Field:
    def __init__(self):
        self.w = 5
        self.h = 5
        self.entities = []

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if y == e.y and x == e.x:
                        print('[X]', end = '')
                        break

                else:
                    print('[ ]', end = '')
            print()

field = Field()
m = Monster(2, 2, "Zeke", 10, field)

while True:
    field.draw()
    move=input("Inserisci un comando direzionale come: su, giù, destra, sinistra per muovere il mostro (per interrompere il movimento digita ""STOP""):")
    if move == "STOP":
        quit()
    m.move(move)