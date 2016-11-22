# DeepReinforcement (Work in progress)
This code is for running reinforcement learning algorithms on Gym platform using tensorflow. 

##Structure
The code is divided up in to 4 classes
- Environment
- Model
- Replay Memory
- Agent

###Environment
This class initializes the gym environment and takes care of all the interations with gym. Its main purpouse is to guarantee that the agent only interacts with observations that have already been preprocessed the way that is intentended. Atari games had a problem with blinking images, so a little pre-processing is necessary for that. And we tend to use more than one frame in a single state of the agent to guarantee that the information of motion is contained in the state. This takes up another bit of messy pre-processing. So this class does some dirty work to keep the code in Agent clean and readable. 
This class implements the following functions
- Init (env)
  - initializes the environment at gym
- Observe()
  - Returns the current state (with any pre-processing already done)
- Act(action)
  - Executes action
  - Returns the resulting state (with any pre-processing already done)
- Reset
  - Resets environment
  - Returns resulting state (with any pre-processing already done)

## Requirements

###Instalation

## Running the code

## ToDo

## References
