import numpy as np


class Week3Functions(object):
    def setToZero(self, vector_x):
        x_out = []
        if vector_x is None:
            return 'FAILED'

        for item in vector_x:
            if isinstance(item, str):
                return 'FAILED'
            else:
                x_out.append(0)

        return x_out
