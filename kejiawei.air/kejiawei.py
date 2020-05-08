# -*- encoding=utf8 -*-
__author__ = "zjseg"


from airtest.core.api import *

auto_setup(__file__)


def haveBusinessman():
    if exists(Template(r"tpl1584536439217.png", record_pos=(-0.016, -0.053), resolution=(1920, 1080))):
        return 1
    else:
        return 0
    
    
def ForFailCase():
    if exists(Template(r"tpl1586022381034.png", record_pos=(-0.008, 0.052), resolution=(1920, 1080))):
        touch(Template(r"tpl1586022395192.png", record_pos=(-0.007, 0.051), resolution=(1920, 1080)))

        wait(Template(r"tpl1585914669744.png", record_pos=(0.407, 0.244), resolution=(1920, 1080)))

        touch(Template(r"tpl1585914676151.png", record_pos=(0.411, 0.247), resolution=(1920, 1080)))
    
def buySSR():
#     if exists(Template(r"tpl1584545559860.png", record_pos=(-0.211, 0.02), resolution=(1280, 720))):
# #     if exists(Template(r"tpl1584546273630.png", rgb=True, record_pos=(-0.163, -0.091), resolution=(1280, 720))):
#         touch(Template(r"tpl1584547535439.png", record_pos=(-0.151, 0.132), resolution=(1280, 720)))

#         return 0
    if exists(Template(r"tpl1584536754992.png", record_pos=(-0.239, -0.063), resolution=(1920, 1080))):
        return 1
#     if exists(Template(r"tpl1585664905325.png", record_pos=(-0.237, -0.064), resolution=(1920, 1080))):
#         return 1
    if exists(Template(r"tpl1584536788357.png", record_pos=(-0.236, -0.064), resolution=(1920, 1080))):
        return 1
    if exists(Template(r"tpl1584536774551.png", record_pos=(-0.235, -0.065), resolution=(1920, 1080))):
        return 1
        
    return 0

        
        
def leave():
    touch(Template(r"tpl1584536214699.png", record_pos=(0.156, 0.13), resolution=(1920, 1080)))


    touch(Template(r"tpl1584549096725.png", record_pos=(-0.085, -0.006), resolution=(1280, 720)))

    touch(Template(r"tpl1584536229571.png", record_pos=(0.41, 0.249), resolution=(1920, 1080)))



def begin():
    wait(Template(r"tpl1584538189324.png", record_pos=(0.018, 0.027), resolution=(1920, 1080)))

    touch(Template(r"tpl1584536030753.png", record_pos=(0.083, -0.039), resolution=(1920, 1080)))

    touch(Template(r"tpl1585669212478.png", record_pos=(0.196, 0.19), resolution=(1920, 1080)))


    touch(Template(r"tpl1584536041226.png", record_pos=(-0.014, 0.244), resolution=(1920, 1080)))



    wait(Template(r"tpl1584537763961.png", record_pos=(-0.391, -0.246), resolution=(1920, 1080)))
    
    sleep(1.0)

    touch(Template(r"tpl1584543953166.png", record_pos=(-0.416, 0.124), resolution=(1280, 720)))

    


    touch(Template(r"tpl1584538973230.png", record_pos=(-0.407, 0.002), resolution=(1920, 1080)))



    
    wait(Template(r"tpl1584538608030.png", record_pos=(-0.124, -0.084), resolution=(1920, 1080)))



    if haveBusinessman() > 0:
        touch(Template(r"tpl1584536446300.png", record_pos=(-0.013, -0.059), resolution=(1920, 1080)))
        if buySSR() > 0:
            touch(Template(r"tpl1584537472374.png", record_pos=(0.153, 0.131), resolution=(1920, 1080)))
            touch(Template(r"tpl1584545379029.png", record_pos=(0.153, 0.131), resolution=(1280, 720)))
        else:
            touch(Template(r"tpl1584536195217.png", record_pos=(-0.154, 0.13), resolution=(1920, 1080)))
        touch(Template(r"tpl1584537490352.png", record_pos=(0.456, -0.246), resolution=(1920, 1080)))
        leave()
    else:
        swipe(Template(r"tpl1584536082760.png", record_pos=(0.035, 0.134), resolution=(1920, 1080)), vector=[0.2185, -0.1115])
        touch(Template(r"tpl1584536101904.png", record_pos=(-0.352, 0.063), resolution=(1920, 1080)))

        swipe(Template(r"tpl1584536113284.png", record_pos=(0.257, 0.069), resolution=(1920, 1080)), vector=[0.1944, -0.107])

        swipe(Template(r"tpl1584536124169.png", record_pos=(0.267, 0.02), resolution=(1920, 1080)), vector=[0.2113, -0.0627])
        touch(Template(r"tpl1584536134110.png", record_pos=(-0.431, -0.042), resolution=(1920, 1080)))
        touch(Template(r"tpl1584536140821.png", record_pos=(-0.447, 0.148), resolution=(1920, 1080)))    
        touch(Template(r"tpl1584536151483.png", record_pos=(0.031, 0.13), resolution=(1920, 1080)))
        touch(Template(r"tpl1584536160076.png", record_pos=(0.362, 0.093), resolution=(1920, 1080)))
        if buySSR() > 0:
            touch(Template(r"tpl1584537472374.png", record_pos=(0.153, 0.131), resolution=(1920, 1080)))
            touch(Template(r"tpl1584545379029.png", record_pos=(0.153, 0.131), resolution=(1280, 720)))
        else:
            touch(Template(r"tpl1584536195217.png", record_pos=(-0.154, 0.13), resolution=(1920, 1080)))
        touch(Template(r"tpl1584536208300.png", record_pos=(0.458, -0.246), resolution=(1920, 1080)))
        leave()    

        
        
while 1 :
    ForFailCase()
    begin()








