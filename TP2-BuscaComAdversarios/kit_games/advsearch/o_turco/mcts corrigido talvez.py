import random
from typing import Tuple, Callable
import time
import math

#from dataclasses import dataclass
# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.
#@dataclass(slots=True)

#from othello.gamestate import GameState # apagar isso depois
class MCTSNode:
    __slots__ = ('state','visits','reward','children','father','unexplored_actions')

    def __init__(self,state, visits:int = 0, reward:float = 0, father = None):
        self.state = state
        self.visits = visits
        self.reward = reward
        self.children = dict[tuple[int,int], MCTSNode]()
        self.father = father
        self.unexplored_actions = set[tuple[int,int]]()

#quero ver se crio uma heurística para a simulação
def make_move(state, eval_func:Callable | None = None) -> Tuple[int, int] | None: 
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo retorna uma jogada ilegal
    # Remova-o e coloque a sua implementacao do MCTS
    #return (-1, -1)
    start = time.time()
    root = MCTSNode(state)
    root.unexplored_actions = set(root.state.legal_moves())  
    player = state.player
    times_played = 0
    # 4.5 por segurança, mas podemos deixar mais próximo de 5
    while time.time() - start < 4.9:
        child = select_and_expand(root)
        result = simulate(child, eval_func)
        back_propagate(child,result)
        times_played += 1
    print(times_played)
    return best_move(root)



    

EXPLORATION_CONSTANT = 1.414 #1.414 # ver melhor isso aqui depois, talvez exista algum valor melhor
def select_and_expand(node:MCTSNode):
    best_score = -float('inf')
    best_node = None
    parent_visits = 0
    if node.visits != 0:
        parent_visits = math.log(node.visits)

    if node.unexplored_actions: ##### isso aqui possivelmente vai precisar ser melhorado
        action = node.unexplored_actions.pop()
        next_state = node.state.next_state(action)
        child = MCTSNode(next_state, father=node)
        node.children[action] = child
        return child

    for child in node.children.values():
        exploitation = child.reward/child.visits
        exploration = math.sqrt(parent_visits/child.visits)
        ucb1 = exploitation + EXPLORATION_CONSTANT * exploration
        if ucb1 > best_score:
            best_score = ucb1
            best_node = child
    
    if best_node is None:
        return node
    
    return select_and_expand(best_node)

# seleciona qualquer ação até chegar em um terminal
#retorna None se for empate
def simulate(node:MCTSNode, eval_func:Callable | None) -> (str | None):
    if not node.state.is_terminal():
        node.unexplored_actions = set(node.state.legal_moves())
    current = node.state
    while not current.is_terminal():
        legal_moves = current.legal_moves()
        #isso ainda pode mudar, queria uma forma de que fosse aleatória essa seleção
        chosen_move = random.choice(tuple(legal_moves))
        current = current.next_state(chosen_move)
    return current.winner()
    

def back_propagate(node:MCTSNode, result:str | None):
    while True:
        node.visits += 1
        if result == None:
            node.reward += 0.5
        elif node.state.player != result:
            node.reward += 1
            
        if node.father is None:
            break
        node = node.father
    return

def best_move(node:MCTSNode) -> (tuple[int,int] | None):
    most_visited = 0
    best_action = None
    for action in node.children:
        child = node.children[action]
        if child.visits > most_visited:
            most_visited = child.visits
            best_action = action

    return best_action