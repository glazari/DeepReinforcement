# DeepReinforcement (Work in progress)
This code is for running reinforcement learning algorithms on Gym platform using tensorflow. 

##Code Structure
The code is divided up in to 5 classes
- Environment
- Model
- Replay Memory
- Agent
- Trainer

###Environment
This class is essencialy a wrapper for the environment you are using to interact with your agent. It implements a function for observing, one for acting, one for reseting and one for getting input/output shape. In the future there could be a function for accessing environment metadata (like atari ram).
- Init (env)
  - Initializes environment: example case, gym.
- Observe()
  - Returns the current state (with any pre-processing already done)
- Act(action)
  - Executes action
  - Returns the resulting state (with any pre-processing already done)
- Reset
  - Resets environment
  - Returns resulting state (with any pre-processing already done)
- getStateShape()
  - Returns the shape of the environment state.
- getActionShape()
  - Returns the shape of the action space. (Not really sure of the most general way to state this yet, as far as I can tell actions can either be continuous vectors or binary vectors.)

###Model
This class is a wrapper around the model. This makes it easier to test differnt models or even different backend tools (tensorflow, keras, theano).
- Init(outputsize, inputsize)
  -builds the model
- Predict(example/batch)
  -returns the output of the model for the given batch or example
- fit(batch)
  - trains model on a given batch
  - possibly returns some metadata
- getGradient(example/batch)
  - returns the gradient of the error for the given batch or example
- getweights
  - Returns parameters that discribe your model
- loadweights(weights)
  - loads weights from a format compatible with what it outputs at getweight.


###ReplayMemory
The replaymemory is an artifact for the Deep Q Network (DQN) {REF} algorithm. It is implementes as a separate class because of the diferent configurations it can take. The replay can be uniform or prioritized, first in first out or some sort of relavance stay. 
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
This class is the one that defines how the agent uses the model and the environment state to choose an action (If it is a policy method, or a Q value method, or random). Therefore both the environment and model are initialized here. Maybe in the future the environment will be initialized elsewhere so that multiple agents can access one environment, but for now, one environment for each agent. Since the the environment is inicialized here the play method and the evaluate method are included here as well. If the environment leaves for the above mentioned reason, so should these methods.

- Init
  - Creates the environment object
  - Creates howevermany model object that are needed. In the case of DQN we need 2 convnets
- Act()
  - Observes the state, gets a prediction from the model, acts acordingly
  - If the environment is initialized in some other class, this method should be re-writen to recive the state as a parameter.
- Play
  - plays one full episode
  - renders if permitted
  - returns episode score
- Evaluate
  - plays n times
  - returns mean score and standard deviation
  
  
###Train
This class is the heart of the learning algorithm. It will dermine if it is a Q-learning algorithm of an async actor-critic or something else (ex: evolutionary algorithm). This is a separate class from agent first because one agent can be trained in different ways. And secondly because some algorithms rely on multiply agents on paralel environments to work (i.e. async actor-critic)  ls
  - Init
    - Initializes the agent (which in turn initializes the environment)

## Requirements

###Instalation

## Running the code

## ToDo

## References
