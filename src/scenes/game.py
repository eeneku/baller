# -*- coding: utf-8 -*-

import pyglet

from engine import scene
from engine import entity_manager
from engine import system_manager

from systems import render_system
from systems import player_system
from systems import movement_system
from systems import ball_spawner_system
from systems import ball_system
from systems import collision_system

from components import transform
from components import render
from components import player
from components import collidable
from components import ball_spawner

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
        
        self.entity_manager.add_components(self.entity_player, [transform.Transform, render.Render, player.Player, collidable.Collidable])
        self.entity_manager.add_component(self.entity_ball_spawner, ball_spawner.BallSpawner)
        
        self.entity_manager.get_component(self.entity_player, transform.Transform).x = 1280/2
        self.entity_manager.get_component(self.entity_player, transform.Transform).y = 720/2
        self.entity_manager.get_component(self.entity_player, player.Player).keys["turn_right"] = 65363
        self.entity_manager.get_component(self.entity_player, player.Player).keys["turn_left"] = 65361
        self.entity_manager.get_component(self.entity_player, render.Render).image = self.gfx_player
        
        b_spawner = self.entity_manager.get_component(self.entity_ball_spawner, ball_spawner.BallSpawner)
        b_spawner.time_between_spawns = 1
        b_spawner.ball_images = {"green_ball" : self.gfx_green_ball,
                                 "red_ball" : self.gfx_red_ball,
                                 "yellow_ball" : self.gfx_yellow_ball,
                                 "blue_ball" : self.gfx_blue_ball}
        
        

    def init_systems(self):
        self.render_system = render_system.RenderSystem(self.entity_manager)
        self.player_system = player_system.PlayerSystem(self.entity_manager, self.manager.engine.key_state)
        self.movement_system = movement_system.MovementSystem(self.entity_manager)
        self.ball_spawner_system = ball_spawner_system.BallSpawnerSystem(self.entity_manager)
        self.ball_system = ball_system.BallSystem(self.entity_manager)
        self.collision_system = collision_system.CollisionSystem(self.entity_manager)
        
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

                