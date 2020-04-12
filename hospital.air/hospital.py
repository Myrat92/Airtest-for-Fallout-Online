# -*- encoding=utf8 -*-
__author__ = "zjseg"

from airtest.core.api import *

using("MyTools.air")
from MyTools import BuySSR
from MyTools import Leave
from MyTools import PickGood
from MyTools import ForFailCase
from MyTools import ForNotExitCase
 
auto_setup(__file__)


def begin():    

    wait(Template(r"tpl1585835475533.png", record_pos=(0.001, 0.002), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835484728.png", record_pos=(0.002, -0.001), resolution=(1920, 1080)))

    sleep(1)

    touch(Template(r"tpl1585835493165.png", record_pos=(0.184, 0.189), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835502394.png", record_pos=(-0.004, 0.245), resolution=(1920, 1080)))

    wait(Template(r"tpl1585843359046.png", record_pos=(-0.373, -0.246), resolution=(1920, 1080)))



    sleep(2)


    pinch("in")


    sleep(1)
    
    if not exists(Template(r"tpl1585835546178.png", record_pos=(0.258, 0.081), resolution=(1920, 1080))):
        pinch("in")

    touch(Template(r"tpl1585835546178.png", record_pos=(0.258, 0.081), resolution=(1920, 1080)))
    sleep(1)

    if not exists(Template(r"tpl1585923557312.png", target_pos=8, record_pos=(0.399, 0.081), resolution=(1920, 1080))):
        pinch("in")


    touch(Template(r"tpl1585923557312.png", target_pos=8, record_pos=(0.399, 0.081), resolution=(1920, 1080)))

        

    wait(Template(r"tpl1585835624958.png", record_pos=(0.256, 0.007), resolution=(1920, 1080)))






    # 第一个怪捡东西 'rectangle': [(570, 465), (570, 607), (1343, 607), (1343, 465)],
    wait(Template(r"tpl1585844689271.png", record_pos=(-0.001, 0.001), resolution=(1920, 1080)))

    PickGood(570,465,1343,607)
    # x = 570
    # y = 465
    # m = 1343
    # n = 607
    # dx = (1343 - 570) // 10
    # hx = (607 - 465) // 3

    # for i in range(x, m, dx):
    #     for j in range(y, n, hx):
    #         touch((i,j))





    touch(Template(r"tpl1585835650649.png", record_pos=(0.253, 0.007), resolution=(1920, 1080)))

    sleep(1)

    touch(Template(r"tpl1585835661815.png", record_pos=(0.292, 0.097), resolution=(1920, 1080)))
    
    if not exists(Template(r"tpl1585835673397.png", record_pos=(0.019, 0.094), resolution=(1920, 1080))):
        touch(Template(r"tpl1585835661815.png", record_pos=(0.292, 0.097), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835673397.png", record_pos=(0.019, 0.094), resolution=(1920, 1080)))


    # 捡东西， 房间自带物品 'rectangle': [(16, 660), (16, 796), (801, 796), (801, 660)],
    wait(Template(r"tpl1585844011919.png", record_pos=(-0.286, 0.098), resolution=(1920, 1080)))

    PickGood(16,660,801,796)






    swipe(Template(r"tpl1585835698058.png", record_pos=(-0.027, -0.008), resolution=(1920, 1080)), vector=[0.288, -0.022])

    touch(Template(r"tpl1585835715908.png", record_pos=(-0.155, 0.072), resolution=(1920, 1080)))

    sleep(1)

    touch(Template(r"tpl1585835728537.png", record_pos=(-0.155, 0.058), resolution=(1920, 1080)))

    if not exists(Template(r"tpl1585835735132.png", record_pos=(0.156, 0.129), resolution=(1920, 1080))):
        touch(Template(r"tpl1585835728537.png", record_pos=(-0.155, 0.058), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835735132.png", record_pos=(0.156, 0.129), resolution=(1920, 1080)))

    wait(Template(r"tpl1585910851000.png", record_pos=(0.034, -0.001), resolution=(1920, 1080)))



    touch(Template(r"tpl1585835742092.png", record_pos=(0.041, -0.004), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835750645.png", record_pos=(0.189, -0.006), resolution=(1920, 1080)))




    # 'rectangle': [(601, 461), (601, 609), (1349, 609), (1349, 461)],
    # touch(Template(r"tpl1585844112026.png", record_pos=(0.008, -0.002), resolution=(1920, 1080)))
    wait(Template(r"tpl1585835774909.png", record_pos=(0.262, 0.01), resolution=(1920, 1080)))

    PickGood(601, 461, 1349, 609)

    touch(Template(r"tpl1585837513030.png", record_pos=(0.264, 0.007), resolution=(1920, 1080)))


    touch(Template(r"tpl1585835781210.png", record_pos=(0.4, 0.007), resolution=(1920, 1080)))



    # 'rectangle': [(586, 473), (586, 601), (1329, 601), (1329, 473)],
    wait(Template(r"tpl1585844242807.png", record_pos=(-0.001, -0.001), resolution=(1920, 1080)))


    PickGood(586, 473, 1329, 601)



    x ,y = touch(Template(r"tpl1585835812461.png", rgb=True, record_pos=(0.374, 0.02), resolution=(1920, 1080)))   #获取坐标再点击一次
    sleep(1)
    touch((x,y))


    touch(Template(r"tpl1585835900544.png", record_pos=(-0.226, 0.102), resolution=(1920, 1080)))



    wait(Template(r"tpl1585844340359.png", record_pos=(0.002, 0.094), resolution=(1920, 1080)))



    touch(Template(r"tpl1585835920243.png", threshold=0.65, rgb=True, record_pos=(-0.132, 0.132), resolution=(1920, 1080)))



    wait(Template(r"tpl1585844361590.png", record_pos=(-0.004, -0.001), resolution=(1920, 1080)))
    # 'rectangle': [(599, 464), (599, 613), (1302, 613), (1302, 464)],
    PickGood(599, 464, 1302, 613)



    wait(Template(r"tpl1585835937809.png", record_pos=(0.366, 0.012), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835942806.png", record_pos=(0.365, 0.009), resolution=(1920, 1080)))

    swipe(Template(r"tpl1585835960345.png", record_pos=(0.163, -0.085), resolution=(1920, 1080)), vector=[-0.1685, 0.0286])


    wait(Template(r"tpl1585925712067.png", record_pos=(0.399, 0.001), resolution=(1920, 1080)))

    touch(Template(r"tpl1585925712067.png", record_pos=(0.399, 0.001), resolution=(1920, 1080)))

    touch(Template(r"tpl1585925712067.png", record_pos=(0.399, 0.001), resolution=(1920, 1080)))


    if not exists(Template(r"tpl1585835989192.png", record_pos=(0.158, 0.132), resolution=(1920, 1080))):
        touch(Template(r"tpl1585925712067.png", record_pos=(0.399, 0.001), resolution=(1920, 1080)))

    touch(Template(r"tpl1585835989192.png", record_pos=(0.158, 0.132), resolution=(1920, 1080)))

    wait(Template(r"tpl1585912905777.png", record_pos=(0.138, -0.069), resolution=(1920, 1080)))


    touch(Template(r"tpl1585836000321.png", target_pos=4, record_pos=(0.345, -0.055), resolution=(1920, 1080)))

    sleep(2)

    touch(Template(r"tpl1585836016006.png", target_pos=6, record_pos=(0.348, -0.059), resolution=(1920, 1080)))

    if not exists(Template(r"tpl1585836035682.png", record_pos=(0.155, 0.132), resolution=(1920, 1080))):
        touch(Template(r"tpl1585836016006.png", target_pos=6, record_pos=(0.348, -0.059), resolution=(1920, 1080)))

    touch(Template(r"tpl1585836035682.png", record_pos=(0.155, 0.132), resolution=(1920, 1080)))

    wait(Template(r"tpl1585836042727.png", target_pos=6, record_pos=(0.348, -0.149), resolution=(1920, 1080)))

    touch(Template(r"tpl1585836042727.png", target_pos=6, record_pos=(0.348, -0.149), resolution=(1920, 1080)))

    sleep(1)
    swipe(Template(r"tpl1585837781111.png", record_pos=(0.011, -0.007), resolution=(1920, 1080)), vector=[-0.0197, 0.1205])
    sleep(1)
    
    if not exists(Template(r"tpl1585837802514.png", record_pos=(0.192, -0.09), resolution=(1920, 1080))):
        touch(Template(r"tpl1585836042727.png", target_pos=6, record_pos=(0.348, -0.149), resolution=(1920, 1080)))

    touch(Template(r"tpl1585837802514.png", record_pos=(0.192, -0.09), resolution=(1920, 1080)))  #[(1090, 293), (1090, 440), (1564, 440), (1564, 293)]   需要遍历坐标，拿物品
    sleep(1)

    PickGood(1090, 293, 1564, 440)

    touch(Template(r"tpl1585913046046.png", record_pos=(-0.153, -0.104), resolution=(1920, 1080)))

    wait(Template(r"tpl1585913073494.png", record_pos=(0.0, 0.0), resolution=(1920, 1080)))  #[(611, 467), (611, 612), (1309, 612), (1309, 467)]

    PickGood(611, 467, 1309, 612)



    touch(Template(r"tpl1585913116907.png", record_pos=(-0.312, -0.003), resolution=(1920, 1080)))


    swipe(Template(r"tpl1585913128491.png", record_pos=(-0.228, 0.094), resolution=(1920, 1080)), vector=[0.1339, -0.0394])


    touch(Template(r"tpl1585913139966.png", record_pos=(-0.362, -0.026), resolution=(1920, 1080)))



    swipe(Template(r"tpl1585913152013.png", record_pos=(-0.242, 0.055), resolution=(1920, 1080)), vector=[0.177, 0.0423])


    touch(Template(r"tpl1585913166003.png", record_pos=(-0.41, -0.009), resolution=(1920, 1080)))


    # 处理购买
    BuySSR()

    touch(Template(r"tpl1585914369273.png", record_pos=(-0.157, -0.089), resolution=(1920, 1080)))

    wait(Template(r"tpl1585914381921.png", record_pos=(0.04, -0.086), resolution=(1920, 1080)))


    touch(Template(r"tpl1585914390801.png", record_pos=(0.036, -0.085), resolution=(1920, 1080))) # [(803, 309), (803, 441), (1253, 441), (1253, 309)],

    sleep(1)

    PickGood(803, 309, 1253, 441)

    touch(Template(r"tpl1585914450371.png", record_pos=(0.336, -0.103), resolution=(1920, 1080)))

    wait(Template(r"tpl1585914465121.png", record_pos=(-0.001, 0.0), resolution=(1920, 1080))) # 'rectangle': [(616, 467), (616, 611), (1301, 611), (1301, 467)]

    PickGood(616, 467, 1301, 611)

    touch(Template(r"tpl1585914508778.png", record_pos=(0.46, -0.247), resolution=(1920, 1080)))


    Leave()

ForNotExitCase()
while 1:
    ForFailCase()
    begin()







