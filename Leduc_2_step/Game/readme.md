# LeducGame

## Attributes
Frist we will explain each attribute:
- **deck:** *The deck contains each possible card of the game. At the initiation it will contains [J, J, Q, Q, K, K]. The hands and the boardcard will be taken from the deck*
- **firstplayer:** *Determines who starts the game*
  - *0 if the first player is the QAgent*
  - *1 if the first player is the opponent agent*
- **hand_player1:** *Hand of the Qagent*
  - *0 for a Jack*
  - *1 for a Queen*
  - *2 for a King*
- **hand_player2:** *Hand of the opponent agent*
  - *0 for a Jack*
  - *1 for a Queen*
  - *2 for a King*
- **boardcard:** *Community card*
  - *0 for a Jack*
  - *1 for a Queen*
  - *2 for a King*
- **result:** *Determines which hand is the best according to the boardcard*
  - *-1 if the hand of the opponent is the best one*
  - *0 if both hands are the same*
  - *1 if the hand of the QAgent is the best one*
- **game_round:** *Determines the current round*
  - *0 for preflop (the boradcard is hidden)*
  - *1 for postflop (the boardcard is revealed)*
- **step:** *Determines the current step in a round. There are only 3 steps at the maximum*
  - *0 for step1*
  - *1 for step2*
  - *2 for step3*
- **pot:** *Current content of the pot of the game*
- **stack1:** *Current stack of the QAgent. It starts at 10*
- **stack2:** *Current stack of the opponent agent. It starts at 10*
- **lastAction:** *Store the previous action taken by the precedent player. It can be None (when we are in the first step of a round), 0, 1 or 2*  
- **current_player:** *Determines the current player*
  - *0 if it is the QAgent*
  - *1 if it is the opponent agent*
- **game_is_over:** *Determines if the game is over or not*
  - *0 if the game is not over*
  - *1 if the game is over*
- **action_hist:** *List of actions taken by the QAgent at a corresponding state. The array has the following form: [[state, action],..., [state, action]]*

## How does it works?
### Round 0, Step 1
```python
game = LeducGame()
print(game)
game.step_prime(1)
```

| FirstPlayer | Hand1 | Hand2 | Boardcard | Deck | Result | Stack1 | Stack2 | Pot | Step | Round | GameIsOver | Current player |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | 2 | [0, 1, 2] | 1 | 9 | 9 | 2 | 0 | 0 | 0 | 0 | 

The first player, in this case the QAgent, checks.
  
### Round 0, Step 2

```python
print(game)
game.step_prime(1)
```

| FirstPlayer | Hand1 | Hand2 | Boardcard | Deck | Result | Stack1 | Stack2 | Pot | Step | Round | GameIsOver | Current player |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | 2 | [0, 1, 2] | 1 | 9 | 9 | 2 | 1 | 0 | 0 | 1 | 

The second player, in this case the opponent agent, checks.

### Round 1, Step 1
```python
print(game)
game.step_prime(1)
```

| FirstPlayer | Hand1 | Hand2 | Boardcard | Deck | Result | Stack1 | Stack2 | Pot | Step | Round | GameIsOver | Current player |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | 2 | [0, 1, 2] | 1 | 9 | 9 | 2 | 0 | 1 | 0 | 0 | 

The QAgent checks.

### Round 1, Step 2
```python
print(game)
game.step_prime(2)
```

| FirstPlayer | Hand1 | Hand2 | Boardcard | Deck | Result | Stack1 | Stack2 | Pot | Step | Round | GameIsOver | Current player |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | 2 | [0, 1, 2] | 1 | 9 | 9 | 2 | 1 | 1 | 0 | 1 |

The opponent agent pushes.

### Round 1, Step 3
```python
print(game)
game.step_prime(2)
```

| FirstPlayer | Hand1 | Hand2 | Boardcard | Deck | Result | Stack1 | Stack2 | Pot | Step | Round | GameIsOver | Current player |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | 2 | [0, 1, 2] | 1 | 9 | 0 | 12 | 2 | 1 | 0 | 0 | 

The QAgent pushes.
  
```python
print(game)
```
  
| FirstPlayer | Hand1 | Hand2 | Boardcard | Deck | Result | Stack1 | Stack2 | Pot | Step | Round | GameIsOver | Current player |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 0 | 2 | [0, 1, 2] | 1 | 0 | 0 | 20 | 2 | 1 | 1 | 1 | 
  
