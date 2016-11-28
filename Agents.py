class RandomAgent:
  def __init__(self, env):
    self.env = env
    self.env.Reset() 
  
  def Act(self):
    #Takes a random Action in the environment
    action = self.env.env.action_space.sample()
    self.env.Act(action)
  
  def Play(self):
    #plays one episode fully and returns the reward
    reward = 0
    self.env.Reset()
    while not self.env.Terminal:
      self.Act()
      reward += self.env.currentReward
    return reward
  
  def Evaluate(self):
    #plays through 30 full episodes and returns the 
    #mean reward and the standard deviation
    import numpy as np
    rewards = []
    for i in range(30):
      rewards.append(self.Play())
    return np.mean(rewards), np.std(rewards)
