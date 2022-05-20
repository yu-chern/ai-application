from utils import expr
from field_var import *
import numpy as np


def ask_solution(current_map, kb, n=8):
    solution = np.array([[0 for col in range(n)] for row in range(n)], dtype=object)
    for x in range(0, n):
        for y in range(0, n):
            if current_map[x][y] == 0:
                result = kb.ask(expr(Danger(x, y)))
                if result:
                    solution[x][y] = 'D'
            else:
                solution[x][y] = current_map[x][y]

    return solution
