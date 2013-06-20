# -*- coding: utf-8 -*-

from engine import system

from components import collidable

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
    
    
    