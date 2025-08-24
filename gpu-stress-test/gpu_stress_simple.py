# cpu_stress_simple.py
# Estresse de CPU (~1 minuto) usando N processos paralelos com NumPy.
# Requisitos: pip install numpy

import os
# Defina antes de importar numpy: 1 thread por processo no BLAS
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import time
import numpy as np
import multiprocessing as mp

DURATION_SECONDS = 60       # tempo total
MATRIX_SIZE = 1536          # aumente p/ 2048 se não bater ~100%
DTYPE = np.float32
WORKERS = os.cpu_count() or 4  # nº de processos = nº de cores lógicos

def worker(n: int, duration: float, dtype=np.float32):
    rng = np.random.default_rng()
    t_end = time.time() + duration
    # warm-up
    a = rng.standard_normal((n, n), dtype=dtype)
    b = rng.standard_normal((n, n), dtype=dtype)
    _ = a @ b
    iters = 0
    while time.time() < t_end:
        a = rng.standard_normal((n, n), dtype=dtype)
        b = rng.standard_normal((n, n), dtype=dtype)
        _ = a @ b
        iters += 1
    return iters

if __name__ == "__main__":
    print(f"Iniciando com {WORKERS} processos, matrizes {MATRIX_SIZE}x{MATRIX_SIZE}, {DURATION_SECONDS}s.")
    with mp.Pool(processes=WORKERS) as pool:
        results = pool.starmap(worker, [(MATRIX_SIZE, DURATION_SECONDS, DTYPE)] * WORKERS)
    print(f"Concluído. Iterações totais (soma de todos os processos): {sum(results)}")
