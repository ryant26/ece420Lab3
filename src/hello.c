#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include "hello.h"
#include "utilities.h"

int main(int argc, char * argv[]){
	int threads = parse_number_threads(argc, argv, 500);

	// Classic multithread
	// #pragma omp parallel num_threads(threads)
	// say_hello(omp_get_thread_num());


	// More advance reduction
	int sum = 0;
	int i;
	#pragma omp parallel for num_threads(threads) \
		reduction(+:sum)
	for (i = 0; i < 500; i++){
		sum += 1;
	}

	printf("The sum is: %d\n", sum);

	return 0;
}

void say_hello(int threads){
	printf("Hello from thread %d of %d \n", threads, omp_get_num_threads());
}