import win32api
import win32con
import numpy as np
import torch
from model import LSTM1
import time
import sys


def getInt(num):
    if num < 0:
        val = np.floor(num)
    else:
        val = np.ceil(num)
    return int(val)


class aiMove:
    def __init__(self, model, WIDTH, HEIGHT, seq, threshold):
        self.model = model
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.seq = seq
        self.threshold = threshold
        self.model_type = 'lstm'
        self.distances = []

    def move(self, targetX, targetY, maxIt):
        for i in range(maxIt):
            # x, y = win32api.GetCursorPos()
            dist = [targetX, targetY]
            self.distances.append(dist)

            if len(self.distances) > self.seq - 1:
                if self.model_type == 'lstm':
                    dist = [self.distances[-self.seq:]]
                else:
                    dist = [self.distances[-1]]

                dist = torch.tensor(dist, dtype=torch.float) / \
                    torch.tensor([self.WIDTH, self.HEIGHT], dtype=torch.float)
                outputs = self.model(dist)
                pred_vel = outputs.detach().numpy()[0]

                move_x = getInt(pred_vel[0] * self.WIDTH)
                move_y = getInt(pred_vel[1] * self.HEIGHT)

                win32api.mouse_event(
                    win32con.MOUSEEVENTF_MOVE, move_x, move_y, 0, 0)
                targetX -= move_x
                targetY -= move_y
                print(targetX, targetY)

                if abs(targetX) <= self.threshold and abs(targetY) <= self.threshold:
                    print("Reached the target within the threshold area.")
                    break

            time.sleep(0.01)


if __name__ == "__main__":
    WIDTH, HEIGHT = 1920, 1080

    input_size = 2
    hidden_size = 128
    num_layers = 1
    num_classes = 2

    seq = 10
    threshold = 5  # Set the threshold area in pixels

    targetX = int(sys.argv[1])
    targetY = int(sys.argv[2])
    maxSteps = int(sys.argv[3])+10

    model = LSTM1(num_classes, input_size, hidden_size, num_layers, 1)
    model.load_state_dict(torch.load("mouse.pt"))

    model.cpu()
    model.eval()

    mover = aiMove(model, WIDTH, HEIGHT, seq, threshold)
    mover.move(targetX, targetY, maxSteps)
