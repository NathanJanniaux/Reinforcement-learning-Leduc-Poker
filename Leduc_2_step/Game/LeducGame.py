#!/usr/bin/env python
# coding: utf-8

import random
import utils
import numpy as np
import matplotlib.pyplot as plt

stack_size=5


# # LeducGame class definition

class LeducGame:
    deck = []
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
    epoch_is_over=None
    actions_hist=[]
    small_stack=None
    #inititate a game
    def __init__(self):
        self.deck = [0,0,1,1,2,2]
        
        #deal card to game from deck
        self.hand_player1=utils.choose_and_remove(self.deck)
        self.hand_player2=utils.choose_and_remove(self.deck)
        self.boardcard=utils.choose_and_remove(self.deck)
        self.result=self.get_result()
        self.firstplayer=random.randrange(0,2)
        self.step_number=0
        self.game_round=0
        self.pot=0
        self.stack1=stack_size
        self.stack2=stack_size
        self.current_player=self.firstplayer
        self.game_is_over=0 #0 not over, 1 over
        self.epoch_is_over=0
        self.small_stack=None

        #small blind at the beginning of the game
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
    
    def reset(self):
        self.deck = [0,0,1,1,2,2]
        
        #deal card to game from deck
        self.hand_player1=utils.choose_and_remove(self.deck)
        self.hand_player2=utils.choose_and_remove(self.deck)
        self.boardcard=utils.choose_and_remove(self.deck)
        self.result=self.get_result()
        self.firstplayer=random.randrange(0,2)
        self.step_number=0
        self.game_round=0
        self.pot=0
        self.current_player=self.firstplayer
        self.game_is_over=0 #0 not over, 1 over
        self.small_stack=None
        
        #small blind at the beginning of the game
        self.pot=2
        self.stack1=self.stack1-1
        self.stack2=self.stack2-1
        
        
    def step_prime(self, action):
        old_round=self.game_round
        gain=0
        
        if(self.stack1<=self.stack2):
            self.small_stack=self.stack1
        else:
            self.small_stack=self.stack2
        
        #QAGENT
        if(self.current_player==0):
            if(action==0):
                gain=-1
                self.game_is_over=1
                self.stack2=self.stack2+self.pot

            #step1
            if(self.step_number==0):
                if(action==1):
                    self.lastAction=1
    
                if(action==2):
                    self.pot=2+self.small_stack 
                    self.stack1=self.stack1-self.small_stack
                    self.lastAction=2
                self.step_number=1
            #step2        
            elif(self.step_number==1):
                if(action==1):
                    if(self.lastAction==1):
                        if(self.game_round==1):
                            self.game_is_over=1
                            if(self.stack2==0 or self.stack1==0):
                                self.epoch_is_over=1
                            if(self.get_result()==1):
                                gain=1
                            if(self.get_result()==-1):
                                gain=-1
                            
                        self.game_round=1
                        self.lastAction=None
                        self.step_number=0
                if(action==2):
                    if(self.lastAction==2):
                        self.pot=self.small_stack*2+2
                        self.game_is_over=1
                        self.epoch_is_over=1
                        if(self.get_result()==1):
                            gain=self.small_stack+1
                            self.stack1=self.small_stack+1
                        if(self.get_result()==-1):
                            gain=-self.small_stack-1
                            self.stack1=0
                    
                    if(self.lastAction==1):
                        self.step_number=2
                        self.stack1=0
                        self.pot=2+self.small_stack

            #step3
            elif(self.step_number==2):
                if(action==2):
                    self.pot=self.small_stack*2+2
                    self.game_is_over=1
                    self.epoch_is_over=1
                    
                    if(self.get_result()==1):
                        gain=self.small_stack+1
                        self.stack1=self.small_stack+1
                    if(self.get_result()==-1):
                        gain=-self.small_stack-1
                        self.stack1=0
               
               
        #OPPONENT          
        elif(self.current_player==1):
            if(action==0):
                gain=1
                self.game_is_over=1
                self.stack1=self.stack1+ self.pot

            #step1
            if(self.step_number==0):
                if(action==1):
                    self.lastAction=1
                if(action==2):
                    self.pot=2+self.small_stack 
                    self.stack2=self.stack2-self.small_stack
                    self.lastAction=2
                self.step_number=1
                    
            #step2        
            elif(self.step_number==1):
                if(action==1):
                    if(self.lastAction==1):
                        if(self.game_round==1):
                            self.game_is_over=1
                            if(self.stack2==0 or self.stack1==0):
                                self.epoch_is_over=1
                            
                            if(self.get_result()==1):
                                gain=1
                            if(self.get_result()==-1):
                                gain=-1
                            
                        self.game_round=1
                        self.lastAction=None
                        self.step_number=0
                if(action==2):
                    if(self.lastAction==2):
                        self.pot=self.small_stack*2+2
                        self.game_is_over=1
                        self.epoch_is_over=1
                        
                        if(self.get_result()==1):
                            gain=self.small_stack+1
                            self.stack2=0
                        if(self.get_result()==-1):
                            gain=-self.small_stack-1
                            self.stack2=self.small_stack+1
                            
                    if(self.lastAction==1):
                        self.step_number=2
                        self.stack2=0
                        self.pot=2+self.small_stack
            #step3
            elif(self.step_number==2):
                if(action==2):
                    self.pot=self.small_stack*2+2
                    self.game_is_over=1
                    self.epoch_is_over=1
                    
                    if(self.get_result()==1):
                        gain=self.small_stack+1
                        self.stack2=0
                    if(self.get_result()==-1):
                        gain=-self.small_stack-1
                        self.stack2=self.small_stack+1
            
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

