#!/usr/bin/env python
# coding: utf-8


import random
import utils
import numpy as np
import matplotlib.pyplot as plt
from Game.LeducGame import *

stack_size=5
random_agent_qtable=None
greedy_agent_qtable=None


# Environment

class Environment:
    agent=None
    game=None
    opponent_action=None
    actions_hist=[]
    
    def __init__(self,agent):
        self.game=LeducGame()
        self.agent=agent
        self.actions_hist.clear()
        
    def __str__(self):
        return "{} \nOpponent_Action = {}\nStack = {}".format(self.game,self.agent.get_action(),self.stack)
    
    def get_actions_hist(self):
        return self.actions_hist
    
    def set_opponent_action(self, action):
        self.opponent_action=action
    
    def get_state(self):
       
        hand1=self.game.get_hand_player1()
        first=self.game.get_firstplayer()
        boardcard= self.game.get_boardcard()
        
        #print("--get_state--")
        #print("hand1= ", hand1)
        #print("first= ", first)
        #print("boardcard= ", boardcard)
        #print("oppponent_action= ", self.opponent_action)
        #print("lastAction= ", self.game.lastAction )
        #print("----")
        
        
        if self.game.game_round == 0:
            if (first == 0 and self.game.lastAction == None):
                return hand1
            elif (first ==0 and self.game.lastAction == 1):
                return hand1+6
            elif(first==1 and self.opponent_action==1):
                return hand1+3
            elif(first==1 and self.opponent_action==2):
                return hand1+6
            
        elif self.game.game_round == 1:
            if (first == 0 and self.game.lastAction == None):
                if hand1==0:
                    return boardcard+9
                elif hand1== 1:
                    return boardcard+12
                elif hand1== 2:
                    return boardcard+15
            elif (first== 0 and self.game.lastAction == 1):
                if hand1==0:
                    return boardcard+27
                elif hand1==1:
                    return boardcard+30
                elif hand1==2:
                    return boardcard+33
            elif first == 1:
                if (self.opponent_action==1):
                    if hand1==0:
                        return boardcard+18
                    elif hand1==1:
                        return boardcard+21
                    elif hand1==2:
                        return boardcard+24
                if(self.opponent_action==2):
                    if hand1==0:
                        return boardcard+27
                    elif hand1==1:
                        return boardcard+30
                    elif hand1==2:
                        return boardcard+33
    
    def reset(self):
        self.game=LeducGame()
        self.actions_hist.clear()
        
    def reset_card(self):
        self.game.reset()
        self.actions_hist.clear()
    
    def step(self, qagent_action):
        r=0
        state=None
        last_game_round=self.game.get_game_round()
        
        self.actions_hist.append([self.get_state(),qagent_action])
        r,current_player,allowed_actions=self.game.step_prime(qagent_action)
        if(allowed_actions==None):
            self.game.game_is_over=1
        if(self.game.is_game_over()==0):
            if(last_game_round==self.game.get_game_round()):
                self.agent.set_action(allowed_actions,qagent_action, self.game.get_game_round(), self.game.get_hand_player2(),self.game.get_boardcard())
            else:
                self.agent.set_action(allowed_actions,None, self.game.get_game_round(), self.game.get_hand_player2(),self.game.get_boardcard())
            
            self.opponent_action=self.agent.get_action()
            print("opponent_action :", self.agent.get_action())
            r,current_player,allowed_actions= self.game.step_prime(self.opponent_action)
            if(self.game.is_game_over()==1):
                state=None
            else:
                state=self.get_state()
        
        return r, allowed_actions, state
          

