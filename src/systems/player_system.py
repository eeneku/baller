# -*- coding: utf-8 -*-

from engine import system

from components import Player
from components import Transform

class PlayerSystem(system.System):
    """ Player system. """
    
    def __init__(self, entity_manager=None, keys=None, *args, **kwargs):
        super(PlayerSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
        self.keys = keys
    
    def update(self, dt):
        plr_components, trans_components = self.entity_manager.get_all_components_of_types([Player, Transform])
    
        for plr, trans in zip(plr_components, trans_components):
            if self.keys:
                if self.keys[plr.keys["turn_left"]]:
                    trans.rotation += plr.rotation_speed * dt
                elif self.keys[plr.keys["turn_right"]]:
                    trans.rotation -= plr.rotation_speed * dt
                            
    
    
    