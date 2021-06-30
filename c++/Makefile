# the compiler: 
# gcc for C program, 
# g++ for C++
CC = g++

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS  = -g -Wall

TARGET: myApp

all: $(TARGET)

myApp: main.o isentropicFlow.o
	$(CC) $(CFLAGS) -o myApp main.o isentropic.o

main.o: main.cpp isentropicFlow.h
	$(CC) $(CFLAGS) -c main.cpp

isentropicFlow.o: isentropicFlow.h

clean:
	rm -f *.o app
