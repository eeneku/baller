# -*- coding: utf-8 -*-

from engine import system

from components import Ball
from components import Collidable
from components import Movement

class BallSystem(system.System):
    """ Ball System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(BallSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        ball_components, col_components, move_components = self.entity_manager.get_all_components_of_types([Ball, 
                                                                                                            Collidable,
                                                                                                            Movement])
        
        for ball, col, move in zip(ball_components, col_components, move_components):
            #print(col.collided)
            if col.collided:
                
                move.moving = False
            else:
                move.moving = True
            
    
    
    