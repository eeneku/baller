# -*- coding: utf-8 -*-

import time
import random
import math

from engine import system

from components import ball_spawner
from components import ball
from components import movement
from components import transform
from components import player
from components import render

class BallSpawnerSystem(system.System):
    """ Ball Spawner System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(BallSpawnerSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(ball_spawner.BallSpawner)
        # The row below assumes that there will be only a one player component. 
        plr = self.entity_manager.get_all_components_of_type(player.Player)
        plr_ent = plr.keys()
        #print(plr_ent[0])
        plr_trans = self.entity_manager.get_component(plr_ent[0], transform.Transform)

        if plr_trans and store:
            for entity, component in store.iteritems():

                if time.time() - component.last_spawn > component.time_between_spawns:
                    
                    new_ball = self.entity_manager.create_entity()
                    
                    self.entity_manager.add_components(new_ball, [ball.Ball, movement.Movement, 
                                                                  transform.Transform, render.Render])
                    
                    trans = self.entity_manager.get_component(new_ball, transform.Transform)
                    
                    trans.x = random.choice([-32, 1292])
                    trans.y = random.choice([-32, 758])
                    #trans.x = 230
                    #trans.y = 342
                    
                    move = self.entity_manager.get_component(new_ball, movement.Movement)
                    
                    move.speed = 100
                    
                    delta_x = plr_trans.x - trans.x
                    delta_y = plr_trans.y - trans.y
                    
                    angle = math.atan2(delta_y, delta_x) * 180 / math.pi
                    
                    move.x = move.speed * math.cos(math.radians(angle))
                    move.y = move.speed * math.sin(math.radians(angle))
                    
                    rendr = self.entity_manager.get_component(new_ball, render.Render)
                    
                    rendr.image = component.ball_image
                    
                    component.last_spawn = time.time()
                    
    
    
    