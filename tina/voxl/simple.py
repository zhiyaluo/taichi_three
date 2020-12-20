from ..common import *


@ti.data_oriented
class SimpleVolume:
    def __init__(self, N, coloring=False):
        self.coloring = coloring
        self.N = N

        if self.coloring:
            self.dens = ti.Vector.field(3, float, (N, N, N))
        else:
            self.dens = ti.field(float, (N, N, N))

        @ti.materialize_callback
        def init_pars():
            self.dens.fill(1)

        self.trans = ti.Matrix.field(4, 4, float, ())

        @ti.materialize_callback
        @ti.kernel
        def init_trans():
            self.trans[None] = ti.Matrix.identity(float, 4)

    def set_volume_density(self, dens):
        self.dens.from_numpy(dens)

    @ti.func
    def pre_compute(self):
        pass

    @ti.func
    def sample_volume(self, pos):
        return trilerp(self.dens, pos * self.N)

    @ti.func
    def get_transform(self):
        return self.trans[None]

    def set_transform(self, trans):
        self.trans[None] = np.array(trans).tolist()