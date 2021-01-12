import taichi as ti
import numpy as np
import tina

ti.init(ti.gpu)

scene = tina.PTScene(smoothing=True, texturing=True)
model = tina.MeshModel('assets/bunny.obj')
material = tina.PBR(roughness=0.2, metallic=0.8)
scene.add_object(model, material)

if isinstance(scene, tina.PTScene):
    scene.update()

gui = ti.GUI('noise', scene.res)

while gui.running:
    scene.input(gui)
    if isinstance(scene, tina.PTScene):
        scene.render(nsteps=5)
    else:
        scene.render()
    gui.set_image(scene.img)
    gui.show()

ti.imwrite(scene.img, 'noise.png')
