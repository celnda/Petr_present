#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include "sha0.h"
#include "string.h"
#include "time.h"


// void get_hash(const uint8_t *message, size_t length, uint8_t hash[SHA0HashSize])
// {
// 	SHA0Context ctx;
// 	SHA0Reset(&ctx);
// 	SHA0Input(&ctx, message, length);
// 	SHA0FinalBits(&ctx, 0, 0);	
// 	SHA0Result(&ctx, hash);	
// }


int main(int argc, char **argv) {
	// clock_t tic = clock(); // TIMING
	if (argc != 2) {
		fprintf(stderr, "%s [input_str]\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	
	unsigned int r = strlen(argv[1]);
	// if (r <= 0) {
	// 	fprintf(stderr, "%s [length(input_str)>0]\n", argv[0]);		
	// 	exit(EXIT_FAILURE);
	// }
	const uint8_t *in_message = (uint8_t*)argv[1];

	// SHA0Context ctx;
	// SHA0Reset(&ctx);

	// fprintf(stderr, "SHA0 over %ld bytes: ", r);

	// SHA0Input(&ctx, in_message, r);
	// SHA0FinalBits(&ctx, 0, 0);
	// SHA0Result(&ctx, dgst);
	uint8_t dgst[SHA0HashSize];
	get_hash(in_message, r, dgst);

	// clock_t toc= clock(); // TIMING
	for (int i = 0; i < SHA0HashSize; i++) {
		fprintf(stdout, "%02x", dgst[i]);
	}	
	// float sec = (float)(toc - tic) / CLOCKS_PER_SEC; // TIMING
	// printf("\n1 it took %e s\n",sec); // TIMING
	return 0;
}
