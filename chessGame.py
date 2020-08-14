from __future__ import division

from copy import deepcopy
from mcts1 import mcts
# from functools import reduce
# import operator
import chess

class ChessState():
    def __init__(self):
        self.board = chess.Board()
        self.currentPlayer = 1 

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getPossibleActions(self):
        possibleActions = []
        #输出所有可能的action
        for move in self.board.legal_moves:
            possibleActions.append(move)
        return possibleActions #type [<class 'chess.Move'>,<class 'chess.Move'>,...]
    
    def takeAction(self, action):
        newState = deepcopy(self)
        newState.board.push(action)
        newState.currentPlayer = self.currentPlayer * -1 #另一个玩家
        return newState

    def isTerminal(self):
        if self.board.is_game_over():
            return True
        # if self.board.is_stalemate():
        #     return True
        # if self.board.is_insufficient_material():
        #     return True
        return False #reduce(operator.mul, sum(self.board, []), 1)

    def getReward(self,f):
        if self.board.is_game_over():
            print(self.board.result(),end=",",file=f)
            if self.board.result() == "1/2-1/2":
                print("平局",file=f)
                return 0
            else:
                print("获胜者",-1*self.currentPlayer,file=f)
                return -1*self.currentPlayer

        return False


# class Action():
#     def __init__(self, player, move):
#         self.player = player
#         self.move = move

#     def __str__(self):
#         return str((self.x, self.y))

#     def __repr__(self):
#         return str(self)

#     def __eq__(self, other):
#         return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y and self.player == other.player

#     def __hash__(self):
#         return hash((self.x, self.y, self.player))


initialState = ChessState()
mcts = mcts(timeLimit=1000000)
action = mcts.search(initialState=initialState)
print(action)