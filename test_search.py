import pytest
from search import *
import random
from termcolor import colored
import time

os.system('color')
random.seed("aima-python")

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
backwards_romania = GraphProblem('Bucharest', 'Arad', romania_map)
dont_move = GraphProblem('Arad', 'Arad', romania_map)



def test_best_first_graph_search():
    # uniform_cost_search and astar_search test it indirectly
    assert best_first_graph_search(
        romania_problem,
        lambda node: node.state).solution() == ['Sibiu', 'Fagaras', 'Bucharest']
    assert best_first_graph_search(
        romania_problem,
        lambda node: node.state[::-1]).solution() == ['Timisoara',
                                                      'Lugoj',
                                                      'Mehadia',
                                                      'Drobeta',
                                                      'Craiova',
                                                      'Pitesti',
                                                      'Bucharest']







def test_simulated_annealing(prob: GraphProblem):
    return simulated_annealing(prob)

def test_astar_search(prob: GraphProblem):
    return astar_search(prob).solution()
    # assert astar_search(eight_puzzle).solution() == ['LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP',
    #                                                  'LEFT', 'DOWN', 'RIGHT', 'RIGHT']
    # assert astar_search(EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))).solution() == ['RIGHT', 'RIGHT']
    # assert astar_search(nqueens).solution() == [7, 1, 3, 0, 6, 4, 2, 5]

def line_spacing():
    print("\n")


if __name__ == '__main__':
    start = time.time()
    print(colored("FIRST TEST. ARAD TO BUCHAREST", 'green'))
    print(colored("Romania Map A Star path: ", 'blue'), test_astar_search(romania_problem))
    end1 = time.time()
    print("Time taken: ", str(end1 - start))
    print(colored("Romania Map Simulated Annealing path:", 'blue'), test_simulated_annealing(romania_problem))
    end2 = time.time()
    print("Time taken: ", str(end2 - start))
    line_spacing()

    print(colored("SECOND TEST. BUCHAREST TO ARAD", 'green'))
    print(colored("Backwards Romania Map A Star path: ", 'blue'), test_astar_search(backwards_romania))
    end3 = time.time()
    print("Time taken: ", str(end3 - start))
    print(colored("Backwards Romania Map Simulated Annealing path:", 'blue'), test_simulated_annealing(backwards_romania))
    end4 = time.time()
    print("Time taken: ", str(end4 - start))

    line_spacing()

    print(colored("SECOND TEST. BUCHAREST TO BUCHAREST", 'green'))
    print(colored("Backwards Romania Map A Star path: ", 'blue'), test_astar_search(dont_move))
    end5 = time.time()
    print("Time taken: ", str(end5 - start))
    print(colored("Backwards Romania Map Simulated Annealing path:", 'blue'), test_simulated_annealing(dont_move))
    end6 = time.time()
    print("Time taken: ", str(end6 - start))





