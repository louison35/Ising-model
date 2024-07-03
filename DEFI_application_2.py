import matplotlib.pyplot as plt
import numpy as np
import random as rd

"-----------------------------------------------------------"


J = 1
Kb = 1
N = 100
Tk = 0.5
T = 50000

"-----------------------------------------------------------"


M1 = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        M1[i, j] = rd.randrange(-1, 2, 2)

Mi = np.zeros((N, N))
M0 = M1.copy()

"-----------------------------------------------------------"


def energie(M, N):
    E = 0
    for i in range(N):
        for j in range(N):
            E += -J * (
                M[i, j] * M[(i - 1) % N, j]
                + M[i, j] * M[(i + 1) % N, j]
                + M[i, j] * M[i, (j - 1) % N]
                + M[i, j] * M[i, (j + 1) % N]
            )
    return E / 2


"-----------------------------------------------------------"


def inverse(M, A, B):
    Mi = M.copy()
    Mi[A, B] = -1 * Mi[A, B]
    return Mi


"-----------------------------------------------------------"


def aimantation(M, N):
    aimantation = 0
    for i in range(N):
        for j in range(N):
            aimantation += M[i, j]
    return aimantation / (N * N)


"-----------------------------------------------------------"


def Ising(M, Tk, N):
    A = aimantation(M, N)
    a = rd.randrange(0, N, 1)
    b = rd.randrange(0, N, 1)

    E1 = energie(M, N)

    M2 = inverse(M, a, b)

    E2 = energie(M2, N)
    dE = E2 - E1
    P = np.exp(-abs(dE) / (Kb * Tk))
    x = rd.random()

    if dE < 0:
        M = M2.copy()

    elif dE > 0 and x < P:
        M = M2.copy()
    return (E1, A, M)


"-----------------------------------------------------------"

for i in range(T):
    result2 = Ising(M1, Tk, N)
    M1 = result2[2]
plt.imshow(M1)
plt.show()
