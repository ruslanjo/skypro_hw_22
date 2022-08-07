

class Unit:
    def move(self, field, x_coord, y_coord, direction, is_fly, is_crawl, speed = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита,
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с
        которым двигается юнит
        """
        if is_fly and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGHT':
                new_y = y_coord
                new_x = x_coord + speed
        if is_crawl:
            speed *= 0.5
            if direction == 'UP': 
                new_y = y_coord + speed  
                new_x = x_coord  
            elif direction == 'DOWN':  
                new_y = y_coord - speed  
                new_x = x_coord  
            elif direction == 'LEFT':  
                new_y = y_coord  
                new_x = x_coord - speed 
            elif direction == 'RIGHT':  
                new_y = y_coord  
                new_x = x_coord + speed  

            field.set_unit(x=new_x, y=new_y, unit=self)
