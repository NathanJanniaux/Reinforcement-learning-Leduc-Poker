#!/usr/bin/env python
# coding: utf-8

import random
import utils
import numpy as np

stack_size=5


# ## QAgent



class QAgent():
    qtable=[]
 # Agent class definition   state=None
    learning_rate=0.1
    state=None #0-5
    gamma=1
    state_number=36
    state=None 
    perf=[]
    
    def __init__(self):
        #qtable creation
        self.qtable=np.zeros((9,self.state_number,3))
        self.perf=[]
        
    #allow to print leduc game state
    def __str__(self):
        return "State = {} \nQTable = {} \nLearning rate = {}".format(self.state,self.qtable,self.learning_rate)
    

        
    
    def explore_action(self, allowed_actions):
        action=random.choice(allowed_actions)
        return action
    
    def exploit_action(self, allowed_actions,stack_qagent):
        #print("allowed_actions",allowed_actions)
        #print("self.state", self.state)
        #print("self.qtable[stack-1][self.state]", self.qtable[stack_qagent-1][self.state])
      
        action=utils.get_max_list(self.qtable[stack_qagent-1][self.state], allowed_actions)
        
        return action
      
    def set_state(self, state):
        self.state=state    
        
    def set_qtable(self,qtable):
        self.qtable=qtable
        
    def set_perf(self,perf):
        self.perf.append(perf)

    def update(self,reward, actions_hist, stack1,stack2):
        #print("UPDATE action= {} \n reward = {} \n next_state = {}\n".format(action,reward,next_state))
        new_value = 0
        future_reward=5
        min_stack=None
        if (stack1<= stack2):
            min_stack=stack1
        else:
            min_stack=stack2
        if(stack1==0):
            reward=-5
            future_reward=0
        elif(stack2==0):
            reward=5
            future_reward=0
            
        #print ("Update: \n")
        #print ("reward = ", reward)
        #print ("actions_hist = ", actions_hist)
        if(len(actions_hist)==1):
            
            if(actions_hist[0][1]==0 and stack1==1):
                reward=-5
                future_reward=0

            new_value = (1 - self.learning_rate) * self.qtable[stack1-1, actions_hist[0][0], actions_hist[0][1]] +  self.learning_rate * (reward + self.gamma*future_reward)
            self.qtable[stack1-1, actions_hist[0][0], actions_hist[0][1]] = new_value
            #print(actions_hist)
        if(len(actions_hist)==2):

            if(actions_hist[1][1]==0 and stack1==1):
                reward=-5
                future_reward=0
                
            new_value = (1 - self.learning_rate) * self.qtable[stack1-1, actions_hist[1][0], actions_hist[1][1]] +  self.learning_rate * (reward + self.gamma*future_reward)
            self.qtable[stack1-1, actions_hist[1][0], actions_hist[1][1]] = new_value

            back = (1 - self.learning_rate) * self.qtable[stack1-1, actions_hist[0][0], actions_hist[0][1]] +  self.learning_rate * (0 + self.gamma*future_reward)
            self.qtable[stack1-1, actions_hist[0][0], actions_hist[0][1]] = back

        if(len(actions_hist)==3):
        
            if(actions_hist[2][1]==0 and stack1==1):
                reward=-5
                future_reward=0

            new_value = (1 - self.learning_rate) * self.qtable[stack1-1, actions_hist[2][0], actions_hist[2][1]] +  self.learning_rate * (reward + self.gamma*future_reward)
            self.qtable[stack1-1, actions_hist[2][0], actions_hist[2][1]] = new_value

            back = (1 - self.learning_rate) * self.qtable[stack1-1, actions_hist[1][0], actions_hist[1][1]] +  self.learning_rate * (0 + self.gamma*future_reward)
            self.qtable[stack1-1, actions_hist[1][0], actions_hist[1][1]] = back

            back_prime = (1 - self.learning_rate) * self.qtable[stack1-1, actions_hist[0][0], actions_hist[0][1]] +  self.learning_rate * (0 + self.gamma*future_reward)
            self.qtable[stack1-1, actions_hist[0][0], actions_hist[0][1]] = back_prime

