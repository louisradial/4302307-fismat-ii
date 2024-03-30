import numpy as np
def g(x: np.longdouble) -> np.longdouble:
    return np.exp(-np.exp(-x))

if __name__ == "__main__":
    omega = np.longdouble(0.5671432904097838729999)
    x = np.longdouble(0)
    for i in range(40):
        x = g(x)
        print(f"Iteração {i+1}: {x:.18f}")
    print(f"Erro absoluto: {omega - x}")
    print(f"Precisão de {np.finfo(np.longdouble).precision} dígitos")
