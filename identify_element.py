def find_molar_mass(V, T):
    m = 50.0
    R = 0.0821
    P = 2.00
    M = (m * R * T) / (P * V)
    return M


if __name__ == "__main__":
    V = [11.6, 14.0, 16.2, 19.4, 21.8]
    T = [-50, 0, 50, 100, 150]
    M = []
    for i in range(len(T)):
        T[i] = T[i] + 273.0
        M.append(find_molar_mass(V[i], T[i]))
    print("Average: ", str(sum(M) / len(T)))
