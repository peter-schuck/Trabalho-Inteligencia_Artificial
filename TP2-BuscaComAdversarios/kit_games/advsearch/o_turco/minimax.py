import random
from typing import Tuple, Callable
import math

def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    alpha = -math.inf
    beta = math.inf
    player = state.player
    action, value = Max(state, max_depth, lambda state: eval_func(state, player), alpha, beta)
    return action
    
def Max(state, max_depth:int, eval_func:Callable, alpha, beta): #-> Tuple[Tuple[int, int], int]
    if state.is_terminal() or max_depth == 0:
        return (-1,-1), eval_func(state)
    value = -math.inf
    action = (-1, -1)
    for possible_action in state.legal_moves():
        next_state = state.next_state(possible_action)
        if next_state.player == state.player:
            a, new_value = Max(next_state, max_depth-1, eval_func, alpha, beta)
        else:
            a, new_value = Min(next_state, max_depth-1, eval_func, alpha, beta)
        if new_value > value:
            value = new_value
            action = possible_action
        alpha = max(alpha, value)
        if alpha >= beta:
            break

    return action, value
    
def Min(state, max_depth:int, eval_func:Callable, alpha, beta): #-> Tuple[Tuple[int, int], int]
    if state.is_terminal() or max_depth == 0:
        return (-1,-1), eval_func(state)
    value = math.inf
    action = (-1, -1)
    for possible_action in state.legal_moves():
        next_state = state.next_state(possible_action)
        if next_state.player == state.player:
            a, new_value = Min(next_state, max_depth-1, eval_func, alpha, beta)
        else:
            a, new_value = Max(next_state, max_depth-1, eval_func, alpha, beta)
        if new_value < value:
            value = new_value
            action = possible_action
        beta = min(beta, value)
        if beta <= alpha:
            break

    return action, value