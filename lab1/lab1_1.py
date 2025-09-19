import os
import numpy as np


def task1_create_and_persist_array(base_dir="."):
    a = np.array([1, 7, 13, 105])
    size = a.nbytes
    txt = os.path.join(base_dir, "task1_array.txt")
    npy = os.path.join(base_dir, "task1_array.npy")
    np.savetxt(txt, a, fmt="%d")
    np.save(npy, a)
    b = np.loadtxt(txt, dtype=a.dtype)
    c = np.load(npy)
    return a, size, b, c


def task2_create_fixed_value_arrays():
    return np.zeros(10), np.ones(10), np.full(10, 5)


def task3_even_integers_30_to_70():
    return np.arange(30, 71, 2)


def task4_linspace_5_to_50():
    return np.linspace(5, 50, 10)


def task5_random_3x3x3_1_to_100():
    return np.random.randint(1, 101, (3, 3, 3))


def task6_fill_3x4_30_to_41():
    return np.arange(30, 42).reshape(3, 4)


def task7_border_ones_inner_zeros_10x10():
    x = np.zeros((10, 10))
    x[0] = 1
    x[-1] = 1
    x[:, 0] = 1
    x[:, -1] = 1
    return x


def task8_diag_1_to_5_in_5x5():
    x = np.zeros((5, 5))
    np.fill_diagonal(x, np.arange(1, 6))
    return x


def task9_chessboard_4x4_zero_diag():
    x = np.indices((4, 4)).sum(0) % 2
    np.fill_diagonal(x, 0)
    return x


def task10_march_2017_dates():
    return np.arange(np.datetime64("2017-03-01"), np.datetime64("2017-04-01"))


def main():
    a, size, b, c = task1_create_and_persist_array()
    print("Задание 1:", a, size, b, c, sep="\n")

    z, o, f = task2_create_fixed_value_arrays()
    print("\nЗадание 2:", z, o, f, sep="\n")

    print("\nЗадание 3:", task3_even_integers_30_to_70(), sep="\n")
    print("\nЗадание 4:", task4_linspace_5_to_50(), sep="\n")
    print("\nЗадание 5:\n", task5_random_3x3x3_1_to_100(), sep="")
    print("\nЗадание 6:\n", task6_fill_3x4_30_to_41(), sep="")
    print("\nЗадание 7:\n", task7_border_ones_inner_zeros_10x10(), sep="")
    print("\nЗадание 8:\n", task8_diag_1_to_5_in_5x5(), sep="")
    print("\nЗадание 9:\n", task9_chessboard_4x4_zero_diag(), sep="")
    print("\nЗадание 10:\n", task10_march_2017_dates(), sep="")


if __name__ == "__main__":
    main()


