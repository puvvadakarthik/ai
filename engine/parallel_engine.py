
from multiprocessing import Pool, cpu_count

def parallel_run(symbols, func):

    workers = cpu_count()

    with Pool(workers) as pool:
        results = pool.map(func, symbols)

    return [r for r in results if r]
