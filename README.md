# DeepReinforcement (Work in progress)
This code is for running reinforcement learning algorithms on Gym platform using tensorflow. 

##Structure
The code is divided up in to 4 classes
- Environment
- Model
- Replay Memory
- Agent

###Environment
This class initializes the gym environment and takes care of all the interations with gym or with any other environment. Its main purpouse is to guarantee that the agent only interacts with observations that have already been preprocessed the way that is intentended. Atari games had a problem with blinking images, so a little pre-processing is necessary for that. And we tend to use more than one frame in a single state of the agent to guarantee that the information of motion is contained in the state. This takes up another bit of messy pre-processing. So this class does some dirty work to keep the code in Agent clean and readable. 
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

###Model
This classes initializes and takes care of the function aproximator (usualy a neural net). The model here is implemented in Tensorflow, but if you choose to change the model or the backend implementation all you have to do is implement the following functions accordingly and the rest of the code should work fine with it.
- Init(outputsize, inputsize)
  -builds the model
- Predict(example/batch)
  -returns the output of the model for the given batch or example
- fit(batch)
  - trains model on a given batch
  - possibly returns some metadata
- getweights
  - whatever the parameters that discribe your model this function should return them in a format which can later be used to load these parameters to another model.
  - Returns parameters
- loadweights(weights)
  - loads weights from a format compatible with what it outputs at getweight.


###ReplayMemory
This class is more specific for the Deep Q Network (DQN) {REF} algorithm. It stores the experiences it is asked to store. Now, some algorithms use this memory as a sliding window of the past, as experiences get too old they are overwriten, other algorithms keep "relevant" memories longer, or even some choose experiences for the batches from the memory with diferent probabilities. This class can be used to implement which ever of these algorithms you desire as long as the outside comunication functions are kept up and running. In our case we implement a simple sliding window memory
This class implements the following funcitons
- Init(replaysize)
  - Allocates memory and returns error if there is not enough memory available
- Store(experience)
  - Stores experience in the memory acording to the chosen algorithm, in our case it is a circular list.
- getFilled
  - returns amount of the memory that has allready been filled with experiences
- Full
  - returns a simple bool value for if the memory has been fully filled or not (true if full)
- makeBatch(size)
  - returns a batch of the apropiate size and following the chosen algorithm, in our case it is chosen uniformly at random
  - some attention should be paid to how much of the memory is filled.

###Agent

## Requirements

###Instalation

## Running the code

## ToDo

## References
