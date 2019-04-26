
import math

class Collider(object):

    tanks = []
    walls = []

    def __init__(self, type ,entity, rad):

        if type == 0:
            self.tanks.append(entity)
            self.rad = rad
            self.entity = entity

        if type == 1:

            self.rad = rad
            self.entity = entity

        if type == 2:
            self.entity = entity
            self.walls.append(entity)

        #else:
            #raise TypeError("Type " + str(type) + " is not defined!")

    def dist(self, other):

        x1 = self.entity.true_pos[0]
        y1 = self.entity.true_pos[1]

        x2 = other.true_pos[0]
        y2 = other.true_pos[1]

        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def is_collided(self):

        for tank in self.tanks:


            if tank != self.entity:
                dist = self.dist(tank)
                if dist < self.rad + tank.collider.rad:
                    tank.speed = 0
                    return True
                else:
                    return False

    def bullet_collided_tank(self):

        for tank in self.tanks:
            dist = self.dist(tank)

            if tank.p != self.entity.p:

                if dist < self.rad + tank.collider.rad:

                    tank.healt -= 1

                    print("collide to tank")
                    return tank
                else:
                    return 0

    def is_collided_to_wall(self):

         for wall in self.walls:

            self.dis_to_start = math.sqrt((self.entity.true_pos[0]-wall.point1[0])**2 + (self.entity.true_pos[1]-wall.point1[1])**2)
            self.dis_to_end = math.sqrt((self.entity.true_pos[0]-wall.point2[0])**2 + (self.entity.true_pos[1]-wall.point2[1])**2)


            if round(self.dis_to_end + self.dis_to_start) == round(wall.lenght):

                return abs(wall.wall_angle)

    def tank_collided_to_wall(self):

         for wall in self.walls:

            self.dis_to_start = math.sqrt((self.entity.true_pos[0]-wall.point1[0])**2 + (self.entity.true_pos[1]-wall.point1[1])**2)
            self.dis_to_end = math.sqrt((self.entity.true_pos[0]-wall.point2[0])**2 + (self.entity.true_pos[1]-wall.point2[1])**2)


            if round(self.dis_to_end + self.dis_to_start) - 3 == round(wall.lenght):

                return True




