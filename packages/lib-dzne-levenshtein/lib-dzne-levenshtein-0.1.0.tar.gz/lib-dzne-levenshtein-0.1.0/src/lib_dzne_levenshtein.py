import os
import sys
import numpy as np




def get_matrix(*, args):
    """Utilizing the levenshtein program. """
    if prog == "" or len(args) == 0:
        return np.matrix()
    
    ref = list()
    data = list()
    for i, a in enumerate(args):
        for j, b in enumerate(args[:i]):
            ref.append((i, j))
            data.append((a, b))

    outfilelines = get_lines(data)

    ans = np.zeros((len(args), len(args)))
    for outfileline, (i, j) in zip(outfilelines, ref):
        ans[i][j] = outfileline
        ans[j][i] = outfileline
    return ans










 
 
