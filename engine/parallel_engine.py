from concurrent.futures import ThreadPoolExecutor, as_completed
import os

def parallel_run(symbols, func):

    results = []

    workers = min(10, os.cpu_count() or 4)

    with ThreadPoolExecutor(max_workers=workers) as executor:

        futures = {executor.submit(func, s): s for s in symbols}

        for future in as_completed(futures):

            try:
                r = future.result()

                if r:
                    results.append(r)

            except:
                pass
