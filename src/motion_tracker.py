import pandas as pd

class MotionTracker:
    def __init__(self, file):
        self.data = pd.read_csv(file)

    def get_frame(self, i):
        return self.data.iloc[i]
