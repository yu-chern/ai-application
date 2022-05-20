import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox, TextArea
from utils import expr
from ask_solution import ask_solution

def find(mymap, field):
    pos = []
    for index, x in np.ndenumerate(mymap):
        if x == field:
            pos.append(index)
    return np.asarray(pos)


def draw_chessboard(mymap: np.ndarray = None):
    if mymap is None:
        mymap = np.array([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]])
    else:
        assert mymap.ndim == 2 and \
               mymap.shape[0] == mymap.shape[1] and \
               mymap.shape[0] > 1
               #and \
               #np.all(np.unique(mymap) == np.array([0, 1]))

    n = mymap.shape[0]
    fig, ax = plt.subplots()

    # plot lines
    for i in range(n + 1):
        ax.plot([i, i], [0, n], 'k')
        ax.plot([0, n], [i, i], 'k')

    # plot queens and reachable area
    queen_img = mpimg.imread('vis_utils/queen.png')
    queen_img = OffsetImage(queen_img, zoom= 1 / n)

    pawn_img = mpimg.imread('vis_utils/pawn.png')
    pawn_img = OffsetImage(pawn_img, zoom= 1 / n)

    trueDanger_img = mpimg.imread('vis_utils/trueDanger.png')
    trueDanger_img = OffsetImage(trueDanger_img, zoom= 1 / n)


    # find position of specific fields
    pos_Q = find(mymap, 'Q')
    pos_P = find(mymap, 'P')
    pos_D = find(mymap, 'D')

    for i, p in enumerate(pos_Q):
        # mirror
        p[1] = n-1-p[1]
        f = AnnotationBbox(queen_img, p + 0.5, frameon=False)
        ax.add_artist(f)

    for i, p in enumerate(pos_P):
        p[1] = n - 1 - p[1]
        f = AnnotationBbox(pawn_img, p + 0.5, frameon=False)
        ax.add_artist(f)

    for i, p in enumerate(pos_D):
        p[1] = n - 1 - p[1]
        f = AnnotationBbox(trueDanger_img, p + 0.5, frameon=False)
        ax.add_artist(f)

    plt.axis('off')
    plt.show()


def draw_tuples(board_size):
    fig, ax = plt.subplots()
    n = board_size

    for i in range(n + 1):
        ax.plot([i, i], [0, n], 'k')
        ax.plot([0, n], [i, i], 'k')


    for i in range(n):
        for j in range(n):
            text = TextArea("("+str(i)+","+str(n-1-j)+")", {"fontsize":15})
            f = AnnotationBbox(text, (i+0.5, j+0.5), frameon=False)
            ax.add_artist(f)

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    draw_map()
