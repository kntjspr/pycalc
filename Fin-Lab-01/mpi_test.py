from mpi4py import MPI  # pyright: ignore[reportMissingImports]
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print(f"Process {rank} out of {size}")