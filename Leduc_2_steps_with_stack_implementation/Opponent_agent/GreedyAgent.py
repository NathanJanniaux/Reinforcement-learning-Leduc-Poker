#!/usr/bin/env python
# coding: utf-8


import random


# ## Greedy Agent


class GreedyAgent():
    
    action=None
        
    def set_action(self,allowed_actions,qagent_action, game_round, hand, boardcard):            
        if game_round == 0:
            if qagent_action == None:
                if hand == 0:
                    action_list=[2,0,0,1,1,1,1,1,1,1] #10% of the time it will push, 20% of the time it will fall and 70% of the time it will check 
                    self.action=random.sample(action_list,1)[0]
                elif hand == 1:
                    action_list=[2,2,2,1,1,1,1,1,1,1] 
                    self.action=random.sample(action_list,1)[0]
                elif hand == 2:
                    action_list=[2,2,2,2,1,1,1,1,1,1] 
                    self.action=random.sample(action_list,1)[0]
            elif qagent_action == 1:
                if hand == 0:
                    action_list=[0,0,0,1,1,1,1,1,1,1] 
                    self.action=random.sample(action_list,1)[0]
                elif hand == 1:
                    self.action=1
                elif hand == 2:
                    action_list=[2,2,1,1,1,1,1,1,1,1] 
                    self.action=random.sample(action_list,1)[0]
            elif qagent_action == 2:
                if hand == 0:
                    self.action= [2,2,2,2,2,2,2,2,2,2] 
                elif hand == 1:
                    action_list=[2,2,2,2,2,2,2,2,2,2] 
                    self.action=random.sample(action_list,1)[0]
                elif hand == 2:
                    self.action= 2
        elif game_round == 1:
            if qagent_action == None:
                if hand == 0:
                    if boardcard == 0:
                        self.action= 2
                    elif boardcard == 1:
                        action_list=[0,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        action_list=[0,1] 
                        self.action=random.sample(action_list,1)[0]
                elif hand == 1:
                    if boardcard == 0:
                        action_list=[2,2,1,1,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 1:
                        action_list=[2,2,2,2,2,2,2,2,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        action_list=[2,2,2,1,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                elif hand == 2:
                    if boardcard == 0:
                        action_list=[0,2,2,1,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 1:
                        action_list=[0,0,2,1,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        self.action= 2
            elif qagent_action == 1:
                if hand == 0:
                    if boardcard == 0:
                        action_list=[2,2,2,2,2,2,2,2,2,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 1:
                        action_list=[0,0,1,1,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        action_list=[0,0,0,0,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                elif hand == 1:
                    if boardcard == 0:
                        action_list=[0,0,1,1,1,1,1,1,1,2] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 1:
                        action_list=[2,2,2,2,2,2,2,2,2,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        action_list=[0,0,0,0,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                elif hand == 2:
                    if boardcard == 0:
                        action_list=[0,2,2,2,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 1:
                        action_list=[0,0,2,2,1,1,1,1,1,1] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        action_list=[2,2,2,2,2,2,2,2,2,1] 
                        self.action=random.sample(action_list,1)[0]
            elif qagent_action == 2:
                if hand == 0:
                    if boardcard == 0:
                        self.action= 2
                    elif boardcard == 1:
                        self.action= 0
                    elif boardcard == 2:
                        self.action= 0
                elif hand == 1:
                    if boardcard == 0:
                        self.action= 0
                    elif boardcard == 1:
                        self.action= 2
                    elif boardcard == 2:
                        self.action= 0
                elif hand == 2:
                    if boardcard == 0:
                        action_list=[2,2,2,0,0,0,0,0,0,0] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 1:
                        action_list=[2,2,0,0,0,0,0,0,0,0] 
                        self.action=random.sample(action_list,1)[0]
                    elif boardcard == 2:
                        self.action= 2
        
    def get_action(self):
        return self.action

