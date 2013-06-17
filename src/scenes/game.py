# -*- coding: utf-8 -*-

import pyglet

from engine import scene
from engine import entity_manager
from engine import system_manager

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager):
        super(Game, self).__init__(manager)
        
        self.batch = pyglet.graphics.Batch()
        
        self.entity_manager = entity_manager.EntityManager()
        self.system_manager = system_manager.SystemManager()
    
    def update(self, dt):
        self.system_manager.update(dt)
            
    def on_draw(self):
        pass

                