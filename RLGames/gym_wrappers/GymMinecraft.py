
from gym.spaces import Discrete, Dict

from RLGames.Minecraft import Minecraft
import RLGames.Minecraft as m
from RLGames.gym_wrappers.GymPygameWrapper import GymPygameWrapper

import RLGames.Sapientino as s
from RLGames.utils import DummyAgent


class GymMinecraft(GymPygameWrapper, Minecraft):
    """Wrapper for the Breakout pygame"""

    PygameEnvClass = Minecraft

    def __init__(self):
        Minecraft.__init__(self, rows=10, cols=10, trainsessionname='test')
        self.init(DummyAgent())

        ntasks = 1
        for t in list(m.TASKS.keys()):
            ntasks *= len(m.TASKS[t])+1

        self.observation_space = Dict({
            "x":          Discrete(self.cols),
            "y":          Discrete(self.rows),
            "theta":      Discrete(4),                         # four directions: North - South - East - West
            "task_state": Discrete(ntasks),
        })
        self.action_space = Discrete(self.nactions)


    def getstate(self):
        return {
            "x":        self.pos_x,
            "y":        self.pos_y,
            "theta":    int(self.pos_th/90),
            "task_state":    self.encode_task_state(),
        }
