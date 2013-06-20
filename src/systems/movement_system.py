# -*- coding: utf-8 -*-

from engine import system

from components import transform
from components import movement

class MovementSystem(system.System):
    """ Movement system. Moves the entity around. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(MovementSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(movement.Movement)

        if store:
            for entity, component in store.iteritems():
                transform_component = self.entity_manager.get_component(entity, transform.Transform)
                
                if transform_component:
                    transform_component.x += component.x * dt
                    transform_component.y += component.y * dt
    
    
    