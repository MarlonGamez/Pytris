from queue import Queue
from tetrimino import Tetrimino, TPiece
import random


class TQueue(Queue):
    def __init__(self, size):
        super().__init__((size))

        # Fill queue up initially
        for i in range(size):
            super().put(Tetrimino(random.choice(list(TPiece))))

    def get():
        # get next tetrimino and push a random one to the queue
        result = super().get()
        super().put(Tetrimino(random.choice(list(TPiece))))
