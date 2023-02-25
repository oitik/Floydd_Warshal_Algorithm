import numpy as np


def floyd_warshall2(w, m_pi):
    # This is to find the parent matrix
    # This was left as an exercise
    ln = len(w)
    prev = w.copy()
    prev_pi = m_pi
    for k in range(ln):
        new = np.zeros((ln, ln))
        new_pi = np.zeros((ln, ln))
        for i in range(ln):
            for j in range(ln):
                new[i][j] = min(prev[i][j], prev[i][k]+prev[k][j])
                if prev[i][j] <= (prev[i][k] + prev[k][j]):
                    new_pi[i][j] = prev_pi[i][j]
                elif prev[i][j] > (prev[i][k] + prev[k][j]):
                    new_pi[i][j] = prev_pi[k][j]
        prev_pi = new_pi.copy()
        prev = new.copy()
    return prev_pi


def floyd_warshall(w):
    ln = len(w)
    prev = w.copy()
    for k in range(ln):
        new = np.zeros((ln, ln))
        for i in range(ln):
            for j in range(ln):
                new[i][j] = min(prev[i][j], prev[i][k]+prev[k][j])
        prev = new.copy()
        # print(prev) comment out this to see all the matrix forms.
    return prev


if __name__ == '__main__':
    n = int(input('Enter number of vertices: '))
    mat = np.full((n, n), np.inf)
    pi_mat = np.full((n, n), np.nan)
    print('Enter your graph with weight: ')
    # enter 0 0 0 to end input section.
    while True:
        a, b, c = [int(x) for x in input().split()]
        if a == 0 and b == 0 and c == 0:
            break
        mat[a - 1][b - 1] = c
        pi_mat[a - 1][b - 1] = a
    # generate W
    for i in range(n):
        mat[i][i] = 0
    # print(mat)
    ans = floyd_warshall(mat)
    print(f'     D({n}) matrix\n{ans}')
    # print(pi_mat)
    parents = floyd_warshall2(mat, pi_mat)
    print(f'     Pi({n}) matrix \n{parents}')
