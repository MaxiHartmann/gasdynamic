#include <iostream>
#include "isentropicFlow.h"
#include "normalShock.h"

int main()
{

	// export in function: ...
	int type;
	double input;

	std::cout << "Enter Type for calculation: " << std::endl;
	std::cout << "\t(1) Machnumber" << std::endl;
	std::cout << "\t(2) T/T0" << std::endl;
	std::cout << "\t(3) p/p0" << std::endl;
	std::cout << "\t(4) rho / rho0" << std::endl;
	std::cout << "\t(5) A / A* (sub)" << std::endl;
	std::cout << "\t(6) A / A* (sup)" << std::endl;
	std::cout << "\t(7) Mach-Angle" << std::endl;
	std::cout << "\t(8) PM-Angle" << std::endl;
	std::cin >> type;

	std::cout << "Enter Inputvalue:" << std::endl;
	std::cin >> input;

	// index,Typ und InputValue
	zustand pos1(1, type, input);
	pos1.printResults();

	normalShock ns1(1, 1, 2.0);
	ns1.printResults();

	return 0;
}

