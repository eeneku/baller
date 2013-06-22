# -*- coding: utf-8 -*-

import pyglet

from engine import scene
from engine import entity_manager
from engine import system_manager

import systems
import components

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
        self.gfx_bg = pyglet.image.load("gfx/bg.png")
        
        self.gfx_player = pyglet.image.load("gfx/player.png")
        self.gfx_player.anchor_x = self.gfx_player.width / 2
        self.gfx_player.anchor_y = self.gfx_player.height / 2
        
        self.gfx_blue_ball = pyglet.image.load("gfx/blue_ball.png")
        self.gfx_blue_ball.anchor_x = self.gfx_blue_ball.width / 2
        self.gfx_blue_ball.anchor_y = self.gfx_blue_ball.height / 2
        
        self.gfx_red_ball = pyglet.image.load("gfx/red_ball.png")
        self.gfx_red_ball.anchor_x = self.gfx_red_ball.width / 2
        self.gfx_red_ball.anchor_y = self.gfx_red_ball.height / 2
        
        self.gfx_yellow_ball = pyglet.image.load("gfx/yellow_ball.png")
        self.gfx_yellow_ball.anchor_x = self.gfx_yellow_ball.width / 2
        self.gfx_yellow_ball.anchor_y = self.gfx_yellow_ball.height / 2
        
        self.gfx_green_ball = pyglet.image.load("gfx/green_ball.png")
        self.gfx_green_ball.anchor_x = self.gfx_green_ball.width / 2
        self.gfx_green_ball.anchor_y = self.gfx_green_ball.height / 2
        
    def init_entities(self):
        self.entity_player = self.entity_manager.create_entity()
        self.entity_ball_spawner = self.entity_manager.create_entity()
        
        self.entity_manager.add_components(self.entity_player, [components.Transform, components.Render, 
                                                                components.Player, components.Collidable])
        self.entity_manager.add_component(self.entity_ball_spawner, components.BallSpawner)
        
        self.entity_manager.get_component(self.entity_player, components.Transform).x = 1280/2
        self.entity_manager.get_component(self.entity_player, components.Transform).y = 720/2
        self.entity_manager.get_component(self.entity_player, components.Player).keys["turn_right"] = 65363
        self.entity_manager.get_component(self.entity_player, components.Player).keys["turn_left"] = 65361
        self.entity_manager.get_component(self.entity_player, components.Render).image = self.gfx_player
        self.entity_manager.get_component(self.entity_player, components.Collidable).type = "player"
        self.entity_manager.get_component(self.entity_player, components.Collidable).collision_distance = self.gfx_player.width / 2
        
        b_spawner = self.entity_manager.get_component(self.entity_ball_spawner, components.BallSpawner)
        b_spawner.time_between_spawns = 1
        b_spawner.ball_images = {"green_ball" : self.gfx_green_ball,
                                 "red_ball" : self.gfx_red_ball,
                                 "yellow_ball" : self.gfx_yellow_ball,
                                 "blue_ball" : self.gfx_blue_ball}
        
        

    def init_systems(self):
        self.render_system = systems.RenderSystem(self.entity_manager)
        self.player_system = systems.PlayerSystem(self.entity_manager, self.manager.engine.key_state)
        self.movement_system = systems.MovementSystem(self.entity_manager)
        self.ball_spawner_system = systems.BallSpawnerSystem(self.entity_manager)
        self.ball_system = systems.BallSystem(self.entity_manager)
        self.collision_system = systems.CollisionSystem(self.entity_manager)
        
        self.system_manager.add_system(self.player_system)
        self.system_manager.add_system(self.collision_system)
        self.system_manager.add_system(self.movement_system)
        self.system_manager.add_system(self.ball_system)
        self.system_manager.add_system(self.ball_spawner_system)
    
    def update(self, dt):
        self.system_manager.update(dt)
            
    def on_draw(self):
        self.gfx_bg.blit(0, 0)
        self.render_system.on_draw()

                