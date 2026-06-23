**Relatório Técnico \- Problemas de Busca com Adversários**

**Autores:** Pedro Schuck de Azevedo (587553);   
Rafael Hillebrand Alexandrini (587786); Vicente Pianezzola (587456)  
**Disciplina:** Inteligência Artificial \- Turma B  
**Professor:** Joel Luis Carbonera

**Tic-Tac-Toe Misere**

	Ao analisarmos o desempenho do Minimax com poda alfa-beta em diferentes cenários podemos perceber que ele 1\. Ganhou a maioria e não perdeu nenhuma partida sequer para o randomplayer; 2\. Empatou todas as vezes que jogou contra si mesmo; E por fim 3\. Não conseguimos ganhar dele nenhuma vez. Dessa forma, por nunca ter perdido alguma partida independente do oponente, considera-se que o planejamento para suas jogadas, capaz de percorrer a árvore Minimax inteira sem limite de profundidade, encontra sempre a solução ótima para cada estado do tabuleiro e cenário de jogo.

**Othello**

| 1° \\ 2° a jogar | Contagem de Peças (CP) | Valor Posicional (VP) | Heurística Customizada (HC) |
| ----- | :---: | :---: | :---: |
| Contagem de Peças (CP) | X | Vitória de CP com 37 peças vs 27 | Vitória de HC com 56 peças vs 8 |
| Valor Posicional (VP) | Vitória de CP com 38 peças vs 26 | X | Vitória de HC com 39 peças vs 25 |
| Heurística Customizada (HC) | Vitória de HC com 53 vs 11 | Vitória de HC com 33 vs 31 | X |

	A Heurística Customizada é uma combinação de heurísticas distintas por soma ponderada, sendo assim capaz de levar em consideração múltiplos fatores importantes para determinar a qualidade de cada jogada: a contagem de peças, a ocupação de cantos e a quantidade de jogadas legais possíveis. 

	Uma vez realizado o mini-torneio entre as diferentes heurísticas de avaliação para o Minimax com poda alfa-beta, reuniu-se os dados armazenados na tabela acima, que indicam uma série de fatores, como as vitórias da Contagem de Peças sobre o Valor Posicional, indicando que manter mais peças que o adversário durante a partida torna-se, em certo nível, mais valioso a longo prazo do que dominar determinados espaços do tabuleiro. Fora isso, pode-se observar uma leve disparidade no número de peças obtidas, entre as heurísticas vencedoras, quando uma começa a partida e quando é a segunda a jogar, demonstrando a possibilidade de existir uma leve desvantagem ao começar-se jogando. 

	Outra característica marcante é a quantidade de vitórias da Heurística Customizada, que ganhou o mini-torneio acumulando quase o dobro de peças da segunda melhor heurística, a Contagem de Peças. Em comparação com a Contagem de Peças, nota-se que a Customizada ganha com grande vantagem, indicando que a análise simples daquela é um tanto inadequada em relação a avaliações mais complexas de valores de estados. Além disso, a heurística customizada foi totalmente projetada pelos membros do grupo sem o auxílio de fontes externas, e o critério de parada do agente Minimax é dado por um limite fixo de profundidade máxima.  

	Para o torneio optamos por escolher uma combinação nova criada por nós, que mistura a heurística discutida acima junto com o algoritmo Monte Carlo Tree Search, o qual permite facilmente limitar a execução levando em conta o tempo para fazer a jogada. O algoritmo tem as funções de seleção, expansão e back-propagate idênticas ao MCTS original, mas na função simulate, ao invés de gerar nodos aleatórios até chegar em um estado terminal, nossa implementação usa uma heurística para decidir quem é o vencedor naquele nodo. Dessa forma o mcts\_custom consegue iterar muitas vezes mais que a versão original, indo de 300 até 500 vezes para mais de 25.000 vezes. A versão custom do MCTS constantemente se saiu melhor que a versão normal, e ganhava a maioria das vezes contra o minimax\_custom, que usava a mesma heurística, sendo portanto a base de nosso agente para competir no torneio.

**Itens Opcionais**

	Visando garantir que o nosso agente do torneio respeitasse o limite de 5 segundos para fazer a jogada buscamos implementar o algoritmo Monte Carlo Tree Search (MCTS). A implementação foi baseada nos slides da disciplina e segue o modelo normal do MCTS, com uma função que seleciona e expande a árvore, uma função que simula, uma que retro propaga os valores obtidos e uma função que retorna o nodo filho, da raiz, mais visitado.  

	Ademais, testamos algumas outras heurísticas, como uma mistura da custom com a mask, para testar distintas versões entre si, possibilitando que fosse determinada a que obtém o maior número de vitórias.

**Declaração do uso de IA**

	Neste trabalho foram utilizadas ferramentas de IA somente para consultar detalhes de sintaxe, assim como funções pré-existentes em certas bibliotecas, da linguagem de programação Python e tirar dúvidas sobre o código disponibilizado.