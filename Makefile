CC := gcc
CFLAGS := -fopenmp -lm -Wall

VPATH = src:sdk
BUILDDIR = build
BIN = bin

default: checkdirs submission

all: checkdirs datagen serialtester main solution

$(BUILDDIR)/%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

submission: $(BUILDDIR)/hello.o
	$(CC) -o main $^ $(CFLAGS)

main: $(BUILDDIR)/hello.o $(BUILDDIR)/utilities.o
	$(CC) -o $(BIN)/main $^ $(CFLAGS)

datagen: $(BUILDDIR)/Lab2IO.o build/datagen.o
	$(CC) -o $(BIN)/datagen $^

serialtester: build/Lab2IO.o build/serialtester.o 
	$(CC) -o $(BIN)/serialtester $^

solution: $(BUILDDIR)/Lab2IO.o $(BUILDDIR)/lab2sol_bar.o 
	$(CC) -o $(BIN)/solution $^ $(CFLAGS)

checkdirs: $(BUILDDIR) $(BIN)

$(BUILDDIR):
	@mkdir -p $@

$(BIN):
	@mkdir -p $@	

clean:
	rm -rf $(BUILDDIR) 
	rm -rf $(BIN)
	rm -f data_*
	rm -f main