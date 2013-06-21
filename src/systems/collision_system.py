# -*- coding: utf-8 -*-

import math

from engine import system

from components import collidable
from components import transform

class CollisionSystem(system.System):
    """ Collision System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(CollisionSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(collidable.Collidable)

        if store:
            for entity, component in store.iteritems():
                pass
            
    def distance(self, point_1=(0, 0), point_2=(0, 0)):
        return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    
    
    