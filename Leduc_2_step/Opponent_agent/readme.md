# Agents
## Random Agent
The random agent choose a random action among the allowed actions for each case.

The following method only uses the allowed_actions parameter, the other one are used for the greedy agent and can be set at any value when using the random agent.
```
def set_action(self,allowed_actions,qagent_action, game_round, hand, boardcard):
```

## Greedy Agent
The greedy agent is a probabilistic and deterministic agent. It will choose an action for each case according to the table bellow:

<img src="greedy_agent_qtable.png"></img>

With this agent,for the following method, the allowed_actions parameter is not used and can be set at any value.
```
def set_action(self,allowed_actions,qagent_action, game_round, hand, boardcard):
```
## Human Agent
This agent allows you to play against the QAgent pre-trained with the random agent or the greedy agent

# How to implement your own agent?
If you want to implement your own agent, its class should fit the following pattern:
```
class YourAgent():

action=None

def set_action(self,allowed_actions,qagent_action, game_round, hand, boardcard):            
    # Selection process of your agent

def get_action(self):
    return self.action
```

You may need more parameters. If it is the case, you have to modify the ** set_action ** of the other agents. Each agent need to have the same prototype.


