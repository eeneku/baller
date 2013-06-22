# -*- coding: utf-8 -*-

from engine import system

from components import Transform
from components import Movement

class MovementSystem(system.System):
    """ Movement system. Moves the entity around. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(MovementSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        move_components, trans_components = self.entity_manager.get_all_components_of_types([Movement, Transform])

        for move, trans in zip(move_components, trans_components):
            trans.x += move.x * dt
            trans.y += move.y * dt
    
    
    