import taichi as ti
import tina

ti.init(ti.gpu)

#scene = tina.Scene(smoothing=True, taa=True, rtx=True)
scene = tina.PTScene(smoothing=True)

roughness = tina.Param(float, initial=0.15)
metallic = tina.Param(float, initial=1.0)
material = tina.PBR(metallic=metallic, roughness=roughness)

model = tina.PrimitiveMesh.sphere()
scene.add_object(model, material)

gui = ti.GUI('matball')
roughness.make_slider(gui, 'roughness')
metallic.make_slider(gui, 'metallic')

if 'PTScene' in str(type(scene)):
    scene.update()
scene.init_control(gui, blendish=True)
while gui.running:
    scene.input(gui)
    scene.render()
    gui.set_image(scene.img)
    gui.show()