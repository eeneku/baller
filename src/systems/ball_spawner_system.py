# -*- coding: utf-8 -*-

from engine import system

from components import ball_spawner
from components import ball

class BallSpawnerSystem(system.System):
    """ Ball Spawner System. """
    
    def __init__(self, entity_manager=None, *args, **kwargs):
        super(BallSpawnerSystem, self).__init__(*args, **kwargs)
        
        self.entity_manager = entity_manager
    
    def update(self, dt):
        store = self.entity_manager.get_all_components_of_type(ball_spawner.BallSpawner)

        if store:
            for entity, component in store.iteritems():
                pass
    
    
    