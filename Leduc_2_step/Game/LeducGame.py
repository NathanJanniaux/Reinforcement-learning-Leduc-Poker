#!/usr/bin/env python
# coding: utf-8

import random
import utils
import numpy as np
import matplotlib.pyplot as plt

stack_size=10
random_agent_qtable=None
greedy_agent_qtable=None


# # LeducGame class definition

class LeducGame:
    deck = []
    actions = [0,1,2] #0 is fold, 1 is check, 2 push
    firstplayer=None; #0 if player1 and 1 if player2
    hand_player1=0;
    hand_player2=0;
    boardcard=0;
    result=0;
    step_number=0
    roundGame=0 #0 preflop, 1 postflop
    game_round=0
    pot=None
    stack1=None
    stack2=None
    lastAction=None
    current_player=None
    game_is_over=None #0 game is not over, #1 game is over
    actions_hist=[]
    #inititate a game
    def __init__(self):
        self.deck = [0,0,1,1,2,2]
        
        #deal card to game from deck
        self.hand_player1=utils.choose_and_remove(self.deck)
        self.hand_player2=utils.choose_and_remove(self.deck)
        self.boardcard=utils.choose_and_remove(self.deck)
        self.result=self.get_result()
        self.firstplayer=random.randrange(0,2)
        #self.firstplayer=0
        self.step_number=0
        self.roundGame=0
        self.game_round=0
        self.pot=0
        self.stack1=stack_size
        self.stack2=stack_size
        self.current_player=self.firstplayer
        self.game_is_over=0 #0 not over, 1 over
        
        self.pot=2
        self.stack1=self.stack1-1
        self.stack2=self.stack2-1
        
    #allow to print leduc game state
    def __str__(self):
        return "FirstPlayer = {} \nHand1 = {} \nHand2 = {} \nBoard = {} \nDeck = {}\nResult = {}\nStack1={}\nStack2={}\nPot={}\nStep={}\nRound={}\nGameIsOver={}\nCurrent_player{}\n\n".format(self.firstplayer,self.hand_player1,self.hand_player2,self.boardcard,self.deck, self.result,self.stack1,self.stack2,self.pot,self.step_number,self.game_round,self.game_is_over, self.current_player)
     
    def get_firstplayer(self):
        return self.firstplayer
        
    def get_hand_player1(self):
        return self.hand_player1
    
    def get_hand_player2(self):
        return self.hand_player2
        
    def get_boardcard(self):
        return self.boardcard
        
    def get_current_player(self):
        return self.current_player
        
    def is_game_over(self):
        return self.game_is_over
    
    def get_game_round(self):
        return self.game_round
        
    #result() : 
    # 0  -> draw
    # 1  -> player1 win
    #-1  -> player2 win
    def get_result(self): #determine the best hand
        #Pairs
        if (self.hand_player1==self.boardcard):
            result=1
        elif (self.hand_player2==self.boardcard):
            result=-1
        #Highest card
        elif (self.hand_player1>self.hand_player2):
            result=1
        elif(self.hand_player1<self.hand_player2):
            result=-1
        #Draw
        else:
            result=0
        return result    
    
    def get_allowed_actions(self, action):
        if (action==0):
            return None
        elif (action==1):        
            return [0,1,2]
        elif (action==2):
            return [0, 2]
        
    def step_prime(self, action):
        old_round=self.game_round
        gain=0
        
        #QAGENT
        if(self.current_player==0):
            if(action==0):
                gain=-1
                self.game_is_over=1
            elif(action==2):
                self.stack1=0

            #step1
            if(self.step_number==0):
                if(action==1):
                    self.lastAction=1
    
                if(action==2):
                    self.pot=12
                    self.lastAction=2
                self.step_number=1
            #step2        
            elif(self.step_number==1):
                if(action==1):
                    if(self.lastAction==1):
                        if(self.game_round==1):
                            self.game_is_over=1
                            
                            if(self.get_result()==1):
                                gain=1
                            if(self.get_result()==-1):
                                gain=-1
                            
                        self.game_round=1
                        self.lastAction=None
                        self.step_number=0
                if(action==2):
                    if(self.lastAction==2):
                        self.pot=20
                        self.game_is_over=1
                        
                        if(self.get_result()==1):
                            gain=10
                        if(self.get_result()==-1):
                            gain=-10
                
                            
                    if(self.lastAction==1):
                        self.pot=12
                        self.step_number=2

            #step3
            elif(self.step_number==2):
                if(action==2):
                    self.pot=20
                    self.game_is_over=1
                    
                    if(self.get_result()==1):
                        gain=10
                    if(self.get_result()==-1):
                        gain=-10
                        
        #OPPONENT          
        elif(self.current_player==1):
            if(action==0):
                gain=1
                self.game_is_over=1
            elif(action==2):
                self.stack2=0

            #step1
            if(self.step_number==0):
                if(action==1):
                    self.lastAction=1
                if(action==2):
                    self.pot=12
                    self.lastAction=2
                self.step_number=1
                    
            #step2        
            elif(self.step_number==1):
                if(action==1):
                    if(self.lastAction==1):
                        if(self.game_round==1):
                            self.game_is_over=1
                            
                            if(self.get_result()==1):
                                gain=1
                            if(self.get_result()==-1):
                                gain=-1
                            
                        self.game_round=1
                        self.lastAction=None
                        self.step_number=0
                if(action==2):
                    if(self.lastAction==2):
                        self.pot=20
                        self.game_is_over=1
                        
                        if(self.get_result()==1):
                            gain=10
                        if(self.get_result()==-1):
                            gain=-10
                            
                    if(self.lastAction==1):
                        self.pot=12
                        self.step_number=2
            #step3
            elif(self.step_number==2):
                if(action==2):
                    self.pot=20
                    self.game_is_over=1
                    
                    if(self.get_result()==1):
                        gain=10
                    if(self.get_result()==-1):
                        gain=-10
            
        allowed_actions= self.get_allowed_actions(action)
        #print("allowed_actions in step_prime: ", allowed_actions)
        #print("action= ", action)
        #print(self)
        if(old_round==self.game_round):
            if(self.current_player==0):
                self.current_player=1
            elif(self.current_player==1):
                self.current_player=0
            #self.current_player=not(self.current_player)
        else:
            self.current_player=self.firstplayer   
        
        return gain,self.current_player, allowed_actions        

