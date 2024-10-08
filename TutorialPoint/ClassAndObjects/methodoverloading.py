class Bird:
    def fly(self):
        print('Bird is flying')


class Airplane:
    def fly(self):
        print('Airplane is flying')


class Fish:
    def swim(self):
        print('Fish is swimming')


def perform_action(entity):
    entity.fly()


sparrow = Bird()
boeing = Airplane()

perform_action(sparrow)
perform_action(boeing)
