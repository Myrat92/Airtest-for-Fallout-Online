# -*- encoding=utf8 -*-
__author__ = "zjseg"

from airtest.core.api import *

auto_setup(__file__)


def HasSSR():
    if exists(Template(r"tpl1584536754992.png", record_pos=(-0.239, -0.063), resolution=(1920, 1080))):
        return 1
    if exists(Template(r"tpl1585664905325.png", record_pos=(-0.237, -0.064), resolution=(1920, 1080))):
        return 1
    if exists(Template(r"tpl1584536788357.png", record_pos=(-0.236, -0.064), resolution=(1920, 1080))):
        return 1
    if exists(Template(r"tpl1584536774551.png", record_pos=(-0.235, -0.065), resolution=(1920, 1080))):
        return 1
        
    return 0


def BuySSR():
    if HasSSR() > 0:
        touch(Template(r"tpl1584537472374.png", record_pos=(0.153, 0.131), resolution=(1920, 1080)))
        touch(Template(r"tpl1584545379029.png", record_pos=(0.153, 0.131), resolution=(1280, 720)))
    else:
        touch(Template(r"tpl1584536195217.png", record_pos=(-0.154, 0.13), resolution=(1920, 1080)))
        
        
        
def Leave():
    wait(Template(r"tpl1585914524262.png", record_pos=(0.158, 0.13), resolution=(1920, 1080)))

    touch(Template(r"tpl1585914529264.png", record_pos=(0.157, 0.131), resolution=(1920, 1080)))
    
    wait(Template(r"tpl1585914647441.png", record_pos=(-0.006, 0.051), resolution=(1920, 1080)))

    touch(Template(r"tpl1585914656430.png", record_pos=(-0.007, 0.052), resolution=(1920, 1080)))
    
    wait(Template(r"tpl1585914669744.png", record_pos=(0.407, 0.244), resolution=(1920, 1080)))

    touch(Template(r"tpl1585914676151.png", record_pos=(0.411, 0.247), resolution=(1920, 1080)))
    
    
def ForFailCase():
    if exists(Template(r"tpl1586022381034.png", record_pos=(-0.008, 0.052), resolution=(1920, 1080))):
        touch(Template(r"tpl1586022395192.png", record_pos=(-0.007, 0.051), resolution=(1920, 1080)))

        wait(Template(r"tpl1585914669744.png", record_pos=(0.407, 0.244), resolution=(1920, 1080)))

        touch(Template(r"tpl1585914676151.png", record_pos=(0.411, 0.247), resolution=(1920, 1080)))
        
        
def ForNotExitCase():
    if exists(Template(r"tpl1585914508778.png", record_pos=(0.46, -0.247), resolution=(1920, 1080))):
        touch(Template(r"tpl1585914508778.png", record_pos=(0.46, -0.247), resolution=(1920, 1080)))
        Leave()

        
def PickGood(x, y, m, n):
    touch((m,n))
    touch((m,y))
    touch((m,(n+y)//2))
    dx = 80
    hx = 40
    for i in range(x, m, dx):
        for j in range(y, n, hx):
            touch((i,j))