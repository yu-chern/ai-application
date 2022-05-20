import numpy as np

# 5x5 chessboards
chessboard1 = np.zeros((5, 5), dtype=object)
chessboard1[0, 0] = 'Q'
chessboard1[2, 0] = 'Q'
chessboard1[1, 0] = 'P'
chessboard1[2, 2] = 'P'

chessboard2 = np.zeros((5, 5), dtype=object)
chessboard2[0, 4] = 'Q'
chessboard2[1, 2] = 'Q'
chessboard2[1, 1] = 'P'
chessboard2[1, 2] = 'P'
chessboard2[2, 2] = 'P'

chessboard3 = np.zeros((5, 5), dtype=object)
chessboard3[1, 1] = 'Q'
chessboard3[3, 4] = 'Q'
chessboard3[2, 1] = 'P'
chessboard3[2, 2] = 'P'
chessboard3[0, 2] = 'P'
chessboard3[2, 4] = 'P'

chessboard4 = np.zeros((5, 5), dtype=object)
chessboard4[0, 4] = 'Q'
chessboard4[0, 3] = 'P'
chessboard4[0, 2] = 'Q'
chessboard4[2, 3] = 'Q'
chessboard4[0, 1] = 'P'
chessboard4[2, 2] = 'P'
chessboard4[3, 1] = 'P'

chessboard5 = np.zeros((5, 5), dtype=object)
chessboard5[0, 0] = 'Q'
chessboard5[3, 2] = 'Q'
chessboard5[0, 2] = 'P'
chessboard5[2, 0] = 'P'
chessboard5[1, 2] = 'P'
chessboard5[1, 3] = 'P'
chessboard5[2, 3] = 'P'

# 6x6 chessboards
chessboard6 = np.zeros((6, 6), dtype=object)
chessboard6[0, 4] = 'P'
chessboard6[1, 3] = 'Q'
chessboard6[2, 0] = 'P'
chessboard6[3, 0] = 'Q'
chessboard6[3, 2] = 'P'
chessboard6[4, 5] = 'Q'

# 7x7 chessboards
chessboard7 = np.zeros((7, 7), dtype=object)
chessboard7[1, 1] = 'P'
chessboard7[2, 1] = 'Q'
chessboard7[2, 2] = 'P'
chessboard7[3, 3] = 'P'
chessboard7[3, 4] = 'Q'
chessboard7[4, 2] = 'Q'
chessboard7[5, 5] = 'Q'
chessboard7[6, 2] = 'P'

# 8 x 8 chessboard
chessboard8 = np.zeros((8, 8), dtype=object)
chessboard8[4, 0] = 'Q'
chessboard8[1, 1] = 'Q'
chessboard8[0, 7] = 'Q'
chessboard8[6, 3] = 'Q'
