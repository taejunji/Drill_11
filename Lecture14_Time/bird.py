import random
import game_framework
from pico2d import *
import game_world
import boy

PIXEL_PER_METER = (10.0/0.3)
BIRDFLY_SPEED_KMPH = 50.0
BIRDFLY_SPEED_MPM = (BIRDFLY_SPEED_KMPH * 1000.0/60.0)
BIRDFLY_SPEED_MPS = (BIRDFLY_SPEED_MPM / 60.0)
BIRDFLY_SPEED_PPS = (BIRDFLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PRE_ACTION  = 0.5
ACTION_PER_TIME = 1.0 / TIME_PRE_ACTION
BIRD_FRAMES_PER_ACTION = 14
class Bird:
    image = None

    def __init__(self):
        self.frame = 0
        self.x = random.randint(100,600)
        self.y = 500
        self.dir = 1
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')


    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.frame % 14) * 183 , int(165 * (1+self.frame//5)) , 184, 165,
                                          0, 'h', self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(int(self.frame % 14) * 183 , int(165 * (1+self.frame//5)) , 184, 165,
                                          0, '', self.x, self.y, 50, 50)

    def update(self):
        self.x += self.dir * BIRDFLY_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + BIRD_FRAMES_PER_ACTION * ACTION_PER_TIME *game_framework.frame_time) % BIRD_FRAMES_PER_ACTION

        if self.x < 25 or self.x > 1600 - 25:
            if self.dir == 1: self.dir = - 1
            else: self.dir = 1