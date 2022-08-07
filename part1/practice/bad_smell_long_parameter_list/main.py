# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Field:
    def set_unit(self, x, y, unit):
        pass


class Unit:
    def __init__(self, movement_type: str, field, x=0, y=0):

        if movement_type not in ['fly', 'crawl']:
            raise ValueError('Тип движения может быть только fly или crawl')

        self.movement_type = movement_type
        self.x = x
        self.y = y
        self.field = Field()

    def _get_speed(self):
        if self.movement_type == 'fly':
            return 1.2

        elif self.movement_type == 'crawl':
            return 0.5

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)
