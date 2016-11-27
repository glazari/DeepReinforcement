class EnvironmentGym:
  
  def __init__(self, name = 'CartPole-v0'):
    import gym
    self.env = gym.make(name)
    observation = self.env.reset()
    self.currentState = self.observation2State(observation)
    self.currentReward = 0
    self.Terminal = False
    
#####################################################################
#The following methods are the "pretty" ones to help make outside   #
#code more readable                                                 #
#####################################################################
  
  def Observe(self):
    #Returns current State
    return self.currentState
  
  def Act(self, action):
    #Executes 'action' and returns new current state
    observation, self.currentReward, self.Terminal, info = self.env.step(action)
    currentState = self.observation2State(observation)
    return currentState
  
  def Reset(self):
    #Resets environment and returns new current state
    observation = self.env.reset()
    self.currentState = self.observation2State(observation)
    self.Terminal = False
    return self.currentState

######################################################################
#

  def getStateShape(self):
    return self.env.observation_space.shape
  
  def getActionSpace(self):
    return self.env.action_space.n

  def observation2State(self, observation):
    #the observation from the environment might not be exactly the
    #state you want to use on your model. Include this kind of pre-
    #processing in this method 
    return observation

