import numpy as np

def field_var(value, x, y):
    # Formalizes the sentence "Field (x,y) has value 'value'"
    assert value in {'Q', 'P', 'D',} and isinstance(x, (int, np.int64, np.int32)) and isinstance(y, (int, np.int64, np.int32))
    return f'{value}{x}{y}'


def Queen(x, y):
    # Formalizes the sentence "There is a Queen in field (x,y)"
    return field_var('Q', x, y)


def Pawn(x, y):
    # Formalizes the sentence "There is a Pawn in field (x,y)"
    return field_var('P', x, y)


def Danger(x, y):
    # Formalizes the sentence "Field (x,y) is in danger"
    return field_var('D', x, y)
