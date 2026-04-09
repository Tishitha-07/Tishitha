import matplotlib.pyplot as plt

def draw(skeleton):
    plt.clf()
    for limb in skeleton.limbs:
        x = [limb.joint1.x, limb.joint2.x]
        y = [limb.joint1.y, limb.joint2.y]
        plt.plot(x, y, 'bo-')
    plt.pause(0.05)
