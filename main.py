import numpy as np
import logging
from datetime import datetime
import concurrent.futures


def thread_function(matrix):
    min_array.append(min(matrix))


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.getLogger().setLevel(logging.DEBUG)
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    matrix = np.random.rand(1000, 1000)
    threads = int(input("Введите ко-во потоков: "))
    min_array = []

    start_time = datetime.now()

    with concurrent.futures.ThreadPoolExecutor(max_workers = threads) as executor:
        executor.map(thread_function, matrix)

    logging.info("min %s: ", min(min_array))
    logging.info(datetime.now() - start_time)
