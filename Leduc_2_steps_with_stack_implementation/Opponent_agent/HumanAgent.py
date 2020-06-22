#!/usr/bin/env python
# coding: utf-8

# ## Human Agent

class HumanAgent():
    
    action=None
        
    def set_action(self,allowed_actions,qagent_action, game_round, hand, boardcard):            
        #if (game_round==0):
        #    if (qagent_action==None):
        #        print("Your card = ",hand,"\n\n")
        #    else:
        #        print("Your card =", hand ,"\nAction of the QAgent = ",qagent_action,"\n\n")
        #elif (game_round==1):
        #    if (qagent_action==None):
        #        print("Your card =", hand ,"\nBoardcard = ",boardcard ,"\n\n")
        #    else:
        #        print("Your card =", hand, "\nAction of the QAgent = ",qagent_action,"\nBoardcard = ", boardcard," \n\n")
        self.action = int(input("Please enter an action :(0,1 or 2)\n"))
        
        print("\n")
        
        
    def get_action(self):
        return self.action

