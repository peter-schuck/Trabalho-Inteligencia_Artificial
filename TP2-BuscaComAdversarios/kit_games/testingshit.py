def back_propagate(node:MCTSNode, result:str | None):
    while True:
        node.visits += 1
        if result == None:
            node.reward += 0.5
        elif node.state.player == result:
            node.reward += 1
            
        if node.father is None:
            break
        node = node.father
    return