#!/usr/bin/env python
# coding: utf-8



import random


# Random Agent

class RandAgent():
    
    action=None
          
        
    def __init__(self):
        #qtable creation
        self.set_action([0,1,2], 0,0,0,0)
        
    def set_action(self,allowed_actions,qagent_action, game_round, hand, boardcard):            
        self.action=random.choice(allowed_actions)
        
    def get_action(self):
        return self.action

