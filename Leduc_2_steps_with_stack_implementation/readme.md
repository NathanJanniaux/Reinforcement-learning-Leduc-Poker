#Leduc 2 steps with stack implementation

## Tutorial to play against the QAgent trained with the greedy agent

### First
Execute this code section:

```python

import random
import utils
import numpy as np
import matplotlib.pyplot as plt
from Game.LeducGame import *
from Environment.Environment import *
from Opponent_agent.RandAgent import *
from Opponent_agent.GreedyAgent import *
from Opponent_agent.HumanAgent import *
from Qagent.QAgent import *
from numpy import asarray
from numpy import savetxt

stack_size=5
random_agent_qtable=None
greedy_agent_qtable=None

```

### Second
Execute the **qAgent (trained with a greedy agent) vs HumanAgent** section
It will get back a saved QTable of our agent (in the big.npy file).

Then you can play against it. 
