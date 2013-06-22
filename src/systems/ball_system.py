# -*- coding: utf-8 -*-

import math

from engine import system

from components import Ball
from components import Collidable
from components import Movement
from components import Transform
from components import Player

class BallSystem(system.System):
    """ Ball System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(BallSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        ball_components, col_components, move_components, trans_components = self.entity_manager.get_all_components_of_types([Ball, Collidable, Movement, Transform])
        plr, plr_trans = self.entity_manager.get_all_components_of_types([Player, Transform])
        
        for ball, col, move, trans in zip(ball_components, col_components, move_components, trans_components):
            if col.collided and not ball.attached:
                move.moving = False
                ball.attached = True
                ball.distance_to_player = self.distance((trans.x, trans.y),(plr_trans[0].x, plr_trans[0].y))
                
                delta_x = trans.x - plr_trans[0].x
                delta_y = trans.y - plr_trans[0].y 

                ball.angle = ((math.atan2(delta_y, delta_x) * 180 / math.pi) - plr_trans[0].rotation + 360) % 360
                col.collided = False
                
            if ball.attached:
                trans.x = (math.cos(math.radians((ball.angle + plr_trans[0].rotation + 360) % 360)) * ball.distance_to_player) + plr_trans[0].x
                trans.y = (math.sin(math.radians((ball.angle + plr_trans[0].rotation + 360) % 360)) * ball.distance_to_player) + plr_trans[0].y
            
    def distance(self, point_1=(0, 0), point_2=(0, 0)):
        return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)
    
    
    