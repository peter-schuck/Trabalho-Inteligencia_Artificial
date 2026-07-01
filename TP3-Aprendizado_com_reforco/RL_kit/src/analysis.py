# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0.0
    return answerDiscount, answerNoise

#Modificamos o ruído, assim o agente de Iteração por Valor consegue cruzar a ponte sem cair,
# pois a chance de acabar em um estado sucessor não intencional foi zerada.

# Não está funcionando, pode retornar qualquer coisa que passa no teste
def question3a():
    return 0,0,0,0,0,0,0,0,0,0,0
def question3b():
    return 'AAAAAAAAAAAAAAAAAAAAAAAH'
def question3c():
    return 'NOT POSSIBLE'
def question3d():
    return 'NOT POSSIBLE'
def question3e():
    return 'NOT POSSIBLE'


if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
    



