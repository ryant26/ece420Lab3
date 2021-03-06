#ifndef UTILITIES_H
#define UTILITIES_H

// The function to parse the number of threads from the 
// command line
// Params: int argc, char** argv, int matrix size
int parse_number_threads(int, char**);

//Prints the usage of the binary from the terminal
void print_usage();

// Used for printing errors when creating elements like threads
void element_creation_error(char*);

#endif