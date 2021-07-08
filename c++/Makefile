# -*- MakeFile -*-

# the compiler: 
# gcc for C program, 
# g++ for C++
CC=g++

# compiler flags:
#  -g    adds debugging information to the executable file
#  -Wall turns on most, but not all, compiler warnings
CFLAGS=-g -Wall

all: myApp

myApp: main.o isentropicFlow.o normalShock.o
	$(CC) $(CFLAGS) main.o isentropicFlow.o normalShock.o -o myApp 

main.o: main.cpp isentropicFlow.h
	$(CC) $(CFLAGS) -c main.cpp

isentropicFlow.o: isentropicFlow.cpp
	$(CC) $(CFLAGS) -c isentropicFlow.cpp

normalShock.o: normalShock.cpp
	$(CC) $(CFLAGS) -c normalShock.cpp

clean:
	rm -f *.o myApp
