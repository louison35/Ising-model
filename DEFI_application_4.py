import matplotlib.pyplot as plt
import numpy as np
import random as rd

"-----------------------------------------------------------"


J = 1
Kb = 1
N = 20
T = 2000
O = 0.01
Tk = 5

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


Ei = []
Ai = []
Tki = []

while Tk - O > 0:
    Tk = Tk - O
    Tki.append(Tk)
    for i in range(T):
        result4 = Ising(M1, Tk, N)
        M1 = result4[2]
    Ei.append(result4[0] / (N * N))
    Ai.append(result4[1])
    M1 = result4[2]

plt.subplots()
plt.subplot(121)
plt.plot(Tki, Ei, "r", label="Energie moyenne")
plt.grid()
plt.xlabel("Température")
plt.ylabel("Energie moyenne")
plt.legend()

plt.subplot(122)
plt.plot(Tki, Ai, "b", label="Aimantation moyenne")
plt.grid()
plt.xlabel("Température")
plt.ylabel("Aimantation moyenne")
plt.legend()

plt.tight_layout()
plt.show()
