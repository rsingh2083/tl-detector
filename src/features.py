from skimage.feature import hog
from matplotlib import pyplot as plt


class Descriptor:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def compute(self, **kwargs):
        pass

    def display(self, **kwargs):
        pass

    def __repr__(self):
        pass


class HogDescriptor(Descriptor):
    def __init__(self, win_size, block_size, block_stride, cell_size, orientations):
        self.win_size = win_size
        self.block_size = block_size
        self.block_stride = block_stride
        self.cell_size = cell_size
        self.orientations = orientations
        Descriptor.__init__(self)

    def compute(self, image, multichannel=True, visualize=False):
        return hog(image, self.orientations, pixels_per_cell=self.cell_size, cells_per_block=self.block_size,
                   multichannel=multichannel, visualize=visualize, block_norm='L2-Hys')

    def display(self, image):
        fd, hog_image = self.compute(image, visualize=True)
        plt.imshow(hog_image, cmap='gray')
        plt.show()

    def __repr__(self):
        return " Window Size: {0} \n Block Size: {1} \n Block Stride: {2} \n Cell Size: {3} \n Orientations: {4}" \
               .format(self.win_size, self.block_size, self.block_stride, self.cell_size, self.orientations)


class LBPDescriptor(Descriptor):
    def __init__(self, points, radius, method='default'):
        self.points = points
        self.radius = radius
        self.method = method
        Descriptor.__init__(self)

    def compute(self):
        pass

    def display(self):
        pass

    def __repr__(self):
        pass