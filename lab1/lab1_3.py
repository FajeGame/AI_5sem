import numpy as np

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введите число.")


def main():
    print("Решаем систему:\n a11*x + a12*y = b1\n a21*x + a22*y = b2")
    a11 = read_float("a11: ")
    a12 = read_float("a12: ")
    a21 = read_float("a21: ")
    a22 = read_float("a22: ")
    b1 = read_float("b1: ")
    b2 = read_float("b2: ")

    A = np.array([[a11, a12], [a21, a22]], dtype=float)
    b = np.array([b1, b2], dtype=float)

    det = np.linalg.det(A)
    if np.isclose(det, 0.0):
        print("Определитель равен 0. Система не имеет единственного решения.")
        return

    x = np.linalg.solve(A, b)
    print("Решение (x, y):", x)


if __name__ == "__main__":
    main()




