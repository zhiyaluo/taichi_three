import taichi as ti
import taichi_three as t3
import numpy as np

ti.init(ti.cpu)

scene = t3.Scene()
texture = ti.imread("assets/cloth.jpg")
model = t3.Model(obj=t3.readobj('assets/torus.obj', scale=0.6))
scene.add_model(model)
camera = t3.Camera()
scene.add_camera(camera)

camera2 = t3.Camera()
camera2.set([0, 0, 2], [0, 0, 0], [0, 1, 0])
scene.add_camera(camera2)

scene.set_light_dir([0.4, 1.5, 1.8])
gui = ti.GUI('Model', camera.res)
gui2 = ti.GUI('Model2', camera2.res)

while gui.running:
    gui.running = not gui.get_event(ti.GUI.ESCAPE)
    #scene.camera.from_mouse(gui)
    model.L2W.from_mouse(gui)
    scene.render()
    gui.set_image(camera.img)
    gui.show()
    gui2.set_image(camera2.img)
    gui2.show()
