#include <iostream>
#include "isentropicFlow.h"
// #include <cmath>

int main()
{
	double mach;

	std::cout << "Enter Machnumber:\n ";
	std::cin >> mach;

    printResults();
    // ....
	std::cout << "Ma   	= " << mach << std::endl;
	std::cout << "Ma*  	= " << calc_machStar(mach) << std::endl;
	// std::cout << "T/T0 	= " << calc_TdT0(mach) << std::endl;
	// std::cout << "p/p0     	= " << calc_pdp0(mach) << std::endl;
	// std::cout << "Ma-Angle 	= " << calc_MachAngle(mach) << std::endl;
	// std::cout << "PM-Angle 	= " << calc_PM_Angle(mach) << std::endl;
    //

	return 0;
}

