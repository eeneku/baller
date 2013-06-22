# -*- coding: utf-8 -*-

import time
import random
import math

from engine import system

from components import BallSpawner
from components import Ball
from components import Movement
from components import Transform
from components import Player
from components import Render
from components import Collidable

class BallSpawnerSystem(system.System):
    """ Ball Spawner System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(BallSpawnerSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        bspwnr_components = self.entity_manager.get_all_components_of_type(BallSpawner)

        plr, plr_trans = self.entity_manager.get_all_components_of_types([Player, Transform])
        
        for bspwnr in bspwnr_components:
            if time.time() - bspwnr.last_spawn > bspwnr.time_between_spawns:
                    
                new_ball = self.entity_manager.create_entity()
                    
                self.entity_manager.add_components(new_ball, [Ball, Movement, Transform, Render, Collidable])
                    
                trans = self.entity_manager.get_component(new_ball, Transform)
                    
                trans.x = random.choice([-16, 1276])
                trans.y = random.choice([-16, 736])
                    
                move = self.entity_manager.get_component(new_ball, Movement)
                    
                move.speed = 100
                    
                delta_x = plr_trans[0].x - trans.x
                delta_y = plr_trans[0].y - trans.y
                    
                angle = math.atan2(delta_y, delta_x) * 180 / math.pi
                
                ball = self.entity_manager.get_component(new_ball, Ball)
                ball.angle = angle
                    
                move.x = move.speed * math.cos(math.radians(angle))
                move.y = move.speed * math.sin(math.radians(angle))
                    
                rendr = self.entity_manager.get_component(new_ball, Render)
                    
                rendr.image = bspwnr.ball_images["red_ball"]
                    
                col = self.entity_manager.get_component(new_ball, Collidable)
                    
                col.type = "ball"
                col.collision_distance = rendr.image.width / 2
                    
                bspwnr.last_spawn = time.time()
                    
    
    
    