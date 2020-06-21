# Environment

This readme will help you to better understand how the environment works.

## Parameters
The environment is composed of several attributes : 
- ```agent``` which is the pre-trained opponent that you want to beat (here is the agents list and how to add your own agent) 
- ```game``` which is the 2 rounds LeducGame (here is the explanation of the game)
- ```opponent_action``` which is the choosen action of the agent/opponent in order to step forward in the game
- ```actions_hist``` which is an array that memorize the actions of a game (in order to update the QTable and backpropagate the reward)


## How to use it?

First, you create the environment which is composed of an agent (the opponent). 

Here we decide to use the randAgent:
```python
env=Environment(randAgent)
```

Then, you need to get the first player of the game (find more details in the game section). We save it in a variable call ```current_player```:
```python
current_player=envTest.game.get_firstplayer()
```
If the first player is the opponent, then it should play first:
```python
if(current_player==1):
                #select an action (the random only need the allowed_actions vector to work)
                envTest.agent.set_action(allowed_actions,None,0,0,0)
                #the agent plays with its action
                _,current_player,allowed_actions=envTest.game.step_prime(envTest.agent.get_action())
```
Now, we are sure that the current player is 0 (meaning that it's qagent's turn). 

According to the state and the exploring/exploiting process, it will choose an action and performs it:

```python
#loop
while(envTest.game.is_game_over()==0):            
                #get state given game and opponent action
                state=envTest.get_state()
                #set the state attribute of QAgent
                qagent.set_state(state)
                #exploration (training)
                qagent_action=qagent.explore_action(allowed_actions)
                #exploitation (testing)
                qagent_action=qagent.exploit_action(allowed_actions)
                
                #QAgent plays and then, if the game is not over, the opponent plays
                #get a reward and a new state according to the QLearning process (more details in the master section)
                reward,allowed_actions, new_state=envTest.step(qagent_action)
```

Finally, the game is over, and you reset the ```env``` to get new values:

```python
env.reset()
```
