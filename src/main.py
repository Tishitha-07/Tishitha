from src.joint import Joint
from src.skeleton import Skeleton
from src.motion_tracker import MotionTracker
from src.gait_simulator import GaitSimulator
from src.visualize import draw

skeleton = Skeleton()

hip = Joint("hip")
knee = Joint("knee")
ankle = Joint("ankle")

skeleton.add_joint(hip)
skeleton.add_joint(knee)
skeleton.add_joint(ankle)

skeleton.connect(hip, knee)
skeleton.connect(knee, ankle)

tracker = MotionTracker("data/gait_data.csv")
sim = GaitSimulator(skeleton, tracker)

for i in range(50):
    sim.update(i)
    draw(skeleton)
