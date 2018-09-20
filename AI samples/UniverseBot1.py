import gym #OpenAI Gym library
import universe #OpenAI Universe Library, newer version of GYM
from universe import wrappers

#Game Environment for the both to train in
env = gym.make('flashgames.CoasterRacer-v0')
env = wrappers.experimental.SafeActionSpace(env)
env.configure(remotes=1)

#creating an observation of the environment to look at things such as:
# Pixel Data and Game State
observation_n = env.reset()

while True:
	action_n = [[('KeyEvent','ArrowUp', True)] for observe in observation_n]
	observation_n, reward_n, done_n, info = env.step(action_n)
	env.render()
