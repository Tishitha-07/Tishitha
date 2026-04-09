from src.limb import Limb

class Skeleton:
    def __init__(self):
        self.joints = {}
        self.limbs = []

    def add_joint(self, joint):
        self.joints[joint.name] = joint

    def connect(self, j1, j2):
        self.limbs.append(Limb(j1, j2))
