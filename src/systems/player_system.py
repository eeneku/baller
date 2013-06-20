# -*- coding: utf-8 -*-

from engine import system

from components import player
from components import transform

class PlayerSystem(system.System):
    """ Player system. """
    
    def __init__(self, entity_manager=None, keys=None, *args, **kwargs):
        super(PlayerSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
        self.keys = keys
    
    def update(self, dt):
        if self.keys:
            store = self.entity_manager.get_all_components_of_type(player.Player)
    
            if store:
                for entity, component in store.iteritems():
                    transform_component = self.entity_manager.get_component(entity, transform.Transform)

                    if transform_component:
                        if self.keys[component.keys["turn_left"]]:
                            print("left!")
                            transform_component.rotation += component.rotation_speed * dt
                        elif self.keys[component.keys["turn_right"]]:
                            print("right!")
                            transform_component.rotation -= component.rotation_speed * dt
                            
    
    
    