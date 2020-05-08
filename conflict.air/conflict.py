# -*- encoding=utf8 -*-
__author__ = "zjseg"

from airtest.core.api import *

auto_setup(__file__)

def begin():
    touch(Template(r"tpl1586790252977.png", record_pos=(-0.043, -0.057), resolution=(1920, 1080)))

    wait(Template(r"tpl1586789853967.png", record_pos=(0.233, 0.19), resolution=(1280, 720)))
    touch(Template(r"tpl1586789866642.png", record_pos=(0.222, 0.188), resolution=(1280, 720)))
    wait(Template(r"tpl1586790284347.png", record_pos=(-0.403, -0.246), resolution=(1920, 1080)))

    pinch("in")
    
    wait(Template(r"tpl1586790301140.png", record_pos=(0.306, 0.003), resolution=(1920, 1080)))
    touch(Template(r"tpl1586790305527.png", record_pos=(0.297, 0.006), resolution=(1920, 1080)))
    wait(Template(r"tpl1586790325606.png", record_pos=(0.278, 0.001), resolution=(1920, 1080)))
    touch(Template(r"tpl1586790332459.png", record_pos=(0.271, 0.006), resolution=(1920, 1080)))
    touch(Template(r"tpl1586790364112.png", target_pos=9, record_pos=(0.202, 0.043), resolution=(1920, 1080)))
    touch(Template(r"tpl1586790413466.png", record_pos=(0.002, 0.094), resolution=(1920, 1080)))
    wait(Template(r"tpl1586790469743.png", record_pos=(-0.317, 0.021), resolution=(1920, 1080)))
    x,y = touch(Template(r"tpl1586790477643.png", record_pos=(-0.322, 0.02), resolution=(1920, 1080)))
    touch((x,y))
    swipe(Template(r"tpl1586790535123.png", record_pos=(-0.159, -0.089), resolution=(1920, 1080)), vector=[0.2046, 0.0303])




begin()







