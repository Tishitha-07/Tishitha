class GaitSimulator:
    def __init__(self, skeleton, tracker):
        self.skeleton = skeleton
        self.tracker = tracker

    def update(self, i):
        frame = self.tracker.get_frame(i)

        for name, joint in self.skeleton.joints.items():
            joint.update(frame[name+"_x"], frame[name+"_y"])
