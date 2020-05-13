import pytest
from search import *
import random


random.seed("aima-python")

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
# vacuum_world = GraphProblemStochastic('State_1', ['State_7', 'State_8'], vacuum_world)
# LRTA_problem = OnlineSearchProblem('State_3', 'State_5', one_dim_state_space)
# eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 7, 8, 6, 0))
# eight_puzzle2 = EightPuzzle((1, 0, 6, 8, 7, 5, 4, 2), (0, 1, 2, 3, 4, 5, 6, 7, 8))
# nqueens = NQueensProblem(8)
#
#
# def test_find_min_edge():
#     assert romania_problem.find_min_edge() == 70



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




def test_astar_search():
    return astar_search(romania_problem).solution()
    # assert astar_search(eight_puzzle).solution() == ['LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'UP',
    #                                                  'LEFT', 'DOWN', 'RIGHT', 'RIGHT']
    # assert astar_search(EightPuzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))).solution() == ['RIGHT', 'RIGHT']
    # assert astar_search(nqueens).solution() == [7, 1, 3, 0, 6, 4, 2, 5]




def test_recursive_best_first_search():
    assert recursive_best_first_search(
        romania_problem).solution() == ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']
    # assert recursive_best_first_search(
    #     EightPuzzle((2, 4, 3, 1, 5, 6, 7, 8, 0))).solution() == [
    #            'UP', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'DOWN']

    def manhattan(node):
        state = node.state
        index_goal = {0: [2, 2], 1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1]}
        index_state = {}
        index = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

        for i in range(len(state)):
            index_state[state[i]] = index[i]

        mhd = 0

        for i in range(8):
            for j in range(2):
                mhd = abs(index_goal[i][j] - index_state[i][j]) + mhd

        return mhd



def test_simulated_annealing():
    return simulated_annealing(romania_problem).solution()


def line_spacing():
    print("\n\n\n")


if __name__ == '__main__':
    print("Romania Map A Star path: ", test_astar_search())
    line_spacing()
    print("Romania Map Simulated Annealing path: ", test_simulated_annealing())

