import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.
    return minimax_move(state, 5, evaluate_custom)


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    opponent = state.board.opponent(player)
    num_legal_moves_advantage = state.board.legal_moves(player).__len__() - state.board.legal_moves(opponent).__len__()
    num_pieces_advantage = state.board.num_pieces(player) - state.board.num_pieces(opponent)
    board = state.board.__str__().splitlines()
    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    corner_advantage = 0
    for corner in corners:
        if board[corner[0]][corner[1]] == player:
            corner_advantage += 100
        elif board[corner[0]][corner[1]] == opponent:
            corner_advantage -= 100
    return ((0.3 * num_legal_moves_advantage) + (0.4 * num_pieces_advantage) + (0.3 * corner_advantage))