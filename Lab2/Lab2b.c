#include <stdio.h>
#include <time.h>
#include "mpi.h"
int main(int argc, char *argv[])
{
    int rank, size;
    MPI_INIT(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&rank);
    MPI_Comm_size(MPI_COMM_WORLD,&size);
    printf("Hola, senor Ryan del #%d de %d!\n",rank,size);
    MPI_Finalize();
    return 0;
}
