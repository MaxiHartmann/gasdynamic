#include "isentropicFlow.h"
#include <iostream>
#include <cmath>

const double pi = 3.14159;
const double Gamma = 1.4;
const double gasConst = 287.058;

void MyFunc() {
    std::cout << "Ohai from another .cpp file!" << std::endl;
    std::cout << "Gamma = " << Gamma << std::endl;
    std::cout << "Cp = " << gasConst << std::endl;
    // std::cin.get();
}

double calc_machStar(double Ma)
{
	double result;
	result = std::sqrt(((Gamma + 1.) / 2. * Ma * Ma) /
			   (1. + (Gamma - 1.) / 2. * Ma * Ma));
	return result;
}
// 
// double calc_TdT0(double Ma)
// {
// 	double result;
// 	result = (1. / (1. + (Gamma - 1.) / 2. * Ma * Ma));
// 	return result;
// }
// 
// double calc_pdp0(double Ma)
// {
// 	double result;
// 	result = std::pow(((1. + (Gamma - 1.) / 2. * Ma * Ma)),
// 			  (-Gamma / (Gamma - 1.)));
// 	return result;
// }
// 
// double calc_MachAngle(double Ma)
// {
// 	double result;
// 	result = asin(1. / Ma) * 180. / M_PI;
// 	return result;
// }
// 
// double calc_PM_Angle(double Ma)
// {
// 	double result;
// 	result =
// 	    (std::sqrt((Gamma + 1.) / (Gamma - 1.)) *
// 		 atan(std::sqrt((Gamma - 1.) / (Gamma + 1.) * (Ma * Ma - 1.))) -
// 	     atan(std::sqrt(Ma * Ma - 1.))) *
// 	    180. / M_PI;
// 	return result;
// }
// 
// double calc_PM_Angle(double Ma)
// {
// 	double result;
// 	result =
// 	    (std::sqrt((Gamma + 1.) / (Gamma - 1.)) *
// 		 atan(std::sqrt((Gamma - 1.) / (Gamma + 1.) * (Ma * Ma - 1.))) -
// 	     atan(std::sqrt(Ma * Ma - 1.))) *
// 	    180. / M_PI;
// 	return result;
// }
//
void printResults() {
    std::cout << "----------------------------------------" << std::endl;
    std::cout << "-         Results:                     -" << std::endl;
    std::cout << "----------------------------------------" << std::endl;
    std::cout << "Gamma = " << Gamma << std::endl;
    std::cout << "Cp = " << gasConst << std::endl;
    // ....
}
