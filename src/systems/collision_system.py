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
            
        for col, trans in zip(col_components, trans_components):
            pass
            
    def distance(self, point_1=(0, 0), point_2=(0, 0)):
        return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    
    
    