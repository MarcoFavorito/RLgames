import os
import sys

import numpy as np
from gym import Env
from gym.spaces import Discrete, Box, Dict

from RLGames.gym_wrappers.GymPygameWrapper import GymPygameWrapper

from RLGames.Sapientino import Sapientino
import RLGames.Sapientino as s
from RLGames.utils import DummyAgent


class GymSapientino(GymPygameWrapper, Sapientino):
    """Wrapper for the Breakout pygame"""

    PygameEnvClass = Sapientino

    def __init__(self, rows=5, cols=7, trainsessionname='test', ncol=7, nvisitpercol=2, deterministic=True):
        Sapientino.__init__(self, rows, cols, trainsessionname, ncol, nvisitpercol)
        self.deterministic = deterministic
        self.sound_enabled = False
        self.init(DummyAgent())


        self.observation_space = Dict({
            "x": Discrete(self.cols),
            "y": Discrete(self.rows),
            "theta": Discrete(4),                           # four directions: North - South - East - West
            # "color": Discrete(self.ncolors + 1)           # number of colors + no-color
            "color": Discrete(len(s.TOKENS) + 1),           # from encode_colors()
            "RAState": Discrete(self.RA.nRAstates + 2)      # RA states + goal + fail state

        })
        self.action_space = Discrete(self.nactions)


    def getstate(self):
        return {
            "x":        self.pos_x,
            "y":        self.pos_y,
            "theta":    int(self.pos_th/90),
            "color":    self.encode_color(),
            "RAState":  self.RA.current_node
        }
