import taichi as ti
import numpy as np
import taichi_inject
import ezprof
import tina

ti.init(ti.cpu)

scene = tina.PTScene(smoothing=True, texturing=True)
scene.load_gltf('assets/cornell.gltf')

if isinstance(scene, tina.PTScene):
    scene.lighting.set_lights(np.array([
        [0, 3.9, 0],
    ], dtype=np.float32))
    scene.lighting.set_light_radii(np.array([
        0.09,
    ], dtype=np.float32))
    scene.lighting.set_light_colors(np.array([
        [4.0, 4.0, 4.0],
    ], dtype=np.float32))

if isinstance(scene, tina.PTScene):
    scene.update()

gui = ti.GUI('cornell_box', scene.res)
scene.init_control(gui, center=(0, 2, 0), radius=6)

while gui.running:
    scene.input(gui)
    if isinstance(scene, tina.PTScene):
        with ezprof.scope('render'):
            scene.render(nsteps=5)
        print(gui.frame + 1, 'samples')
    else:
        scene.render()
    gui.set_image(scene.img)
    gui.show()

ezprof.show()