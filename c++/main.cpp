#include <iostream>
#include "isentropicFlow.h"

int main()
{
	double mach;

	std::cout << "Enter Machnumber: " << std::endl;
	// std::cin >> mach;
	mach = 2.0;

	
	// index, und Machnumber
	zustand pos1(1, mach);

	pos1.calcResults();
	pos1.printResults();

	return 0;
}
