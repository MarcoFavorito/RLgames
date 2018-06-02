from abc import ABC
from time import sleep

from gym import Env
from gym.utils import EzPickle


class GymPygameWrapper(ABC, Env, EzPickle):

    def __init__(self, *args, delay=0.01, **kwargs):
        Env.__init__(self)
        EzPickle.__init__(self, *args, **kwargs)

        self.delay = delay


    @property
    def PygameEnvClass(self):
        raise NotImplementedError

    def step(self, action):
        self.update(action)
        obs = self.getstate()
        reward = self.getreward()
        done = self.finished
        info = {"goal": self.goal_reached()}
        return obs, reward, done, info

    def render(self, mode='human'):
        self.draw()
        sleep(self.delay)

    def getreward(self):
        r = self.current_reward
        return r

    def reset(self):
        self.PygameEnvClass.reset(self)
        return self.getstate()
