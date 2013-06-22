# -*- coding: utf-8 -*-

import math

from engine import system

from components import Collidable
from components import Transform

class CollisionSystem(system.System):
    """ Collision System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(CollisionSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager

    
    def update(self, dt):
        col_components, trans_components = self.entity_manager.get_all_components_of_types([Collidable, Transform])
        
        for i in xrange(len(col_components)):
            for j in xrange(i+1, len(col_components)):
                collided = self.check_collision((col_components[i], trans_components[i]),
                                                (col_components[j], trans_components[j]))

                if collided:
                    col_components[i].collided = True
                    col_components[j].collided = True
       
    def check_collision(self, i, j):
        collision_distance = i[0].collision_distance + j[0].collision_distance
        actual_distance = self.distance((i[1].x, i[1].y), (j[1].x, j[1].y))
        
        return (actual_distance <= collision_distance) 
            
    def distance(self, point_1=(0, 0), point_2=(0, 0)):
        return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    
    
    