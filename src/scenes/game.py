# -*- coding: utf-8 -*-

import pyglet

from engine import scene
from engine import entity_manager
from engine import system_manager

from systems import render_system
from systems import player_input_system

from components import transform
from components import render
from components import player_input

class Game(scene.Scene):
    """ The main scene where most of the game is happening. """

    def __init__(self, manager):
        super(Game, self).__init__(manager)
        
        self.batch = pyglet.graphics.Batch()
        
        self.entity_manager = entity_manager.EntityManager()
        self.system_manager = system_manager.SystemManager()
        
        self.init_graphics()
        self.init_entities()
        self.init_systems()
        
    def init_graphics(self):
        self.gfx_player = pyglet.image.load("gfx/player.png")
        self.gfx_blue_ball = pyglet.image.load("gfx/blue_ball.png")
        self.gfx_red_ball = pyglet.image.load("gfx/red_ball.png")
        self.gfx_yellow_ball = pyglet.image.load("gfx/yellow_ball.png")
        self.gfx_green_ball = pyglet.image.load("gfx/green_ball.png")
        
    def init_entities(self):
        self.entity_player = self.entity_manager.create_entity()
        
        self.entity_manager.add_components(self.entity_player, [transform.Transform, render.Render, player_input.PlayerInput])
        
        self.entity_manager.get_component(self.entity_player, transform.Transform).x = 399
        self.entity_manager.get_component(self.entity_player, transform.Transform).y = 150
        self.entity_manager.get_component(self.entity_player, player_input.PlayerInput).turn_right = 65363
        self.entity_manager.get_component(self.entity_player, player_input.PlayerInput).turn_left = 65361
        self.entity_manager.get_component(self.entity_player, render.Render).image = self.gfx_player.get_texture()
        

    def init_systems(self):
        self.render_system = render_system.RenderSystem(self.entity_manager)
        self.player_input_system = player_input_system.PlayerInputSystem(self.entity_manager, self.manager.engine.key_state)
        
        self.system_manager.add_system(self.player_input_system)
    
    def update(self, dt):
        self.system_manager.update(dt)
            
    def on_draw(self):
        self.render_system.on_draw()

                