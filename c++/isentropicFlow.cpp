#include "isentropicFlow.h"
#include <cmath>
#include <iostream>

// constructor
zustand::zustand(int id, double mach)
{
	index = id;
	ma = mach;
}

void zustand::calcResults()
{
	machStar = std::sqrt(((Gamma + 1.) / 2. * ma * ma) /
			     (1. + (Gamma - 1.) / 2. * ma * ma));

	TdT0 = (1. / (1. + (Gamma - 1.) / 2. * ma * ma));

	pdp0 = std::pow(((1. + (Gamma - 1.) / 2. * ma * ma)),
			(-Gamma / (Gamma - 1.)));

	rhodrho0 =
	    std::pow((1. + (Gamma - 1.) / 2. * ma * ma), (-1. / (Gamma - 1.)));

	MachAngle = asin(1. / ma) * 180. / pi;

	PM_Angle =
	    (std::sqrt((Gamma + 1.) / (Gamma - 1.)) *
		 atan(std::sqrt((Gamma - 1.) / (Gamma + 1.) * (ma * ma - 1.))) -
	     atan(std::sqrt(ma * ma - 1.))) *
	    180. / pi;

	AdAstar =
	    1. /
	    (ma * std::pow((2. / (Gamma + 1.) * (1. + (Gamma - 1.) / 2. * ma * ma)),
			   (-(Gamma + 1.) / (2. * Gamma - 2.))));
}

void zustand::printResults()
{
	std::cout << "----------------------------------------" << std::endl;
	std::cout << "|         Results:                      |" << std::endl;
	std::cout << "----------------------------------------" << std::endl;
	std::cout << "Position:   " << index << std::endl;
	std::cout << "Gamma 	= " << Gamma << std::endl;
	std::cout << "Cp 	= " << gasConst << std::endl;
	std::cout << "Ma   	= " << ma << std::endl;
	std::cout << "Ma*  	= " << machStar << std::endl;
	std::cout << "T/T0 	= " << TdT0 << std::endl;
	std::cout << "p/p0     	= " << pdp0 << std::endl;
	std::cout << "rho/rho0 	= " << rhodrho0 << std::endl;
	std::cout << "Ma-Angle 	= " << MachAngle << std::endl;
	std::cout << "Ma-Angle 	= " << MachAngle << std::endl;
	std::cout << "PM-Angle 	= " << PM_Angle << std::endl;
	std::cout << "A / A* 	= " << AdAstar << std::endl;
}

// double zustand::calc_machStar(double ma)
// {
// 	double result;
// 	result = std::sqrt(((Gamma + 1.) / 2. * ma * ma) /
// 			   (1. + (Gamma - 1.) / 2. * ma * ma));
// 	return result;
// }
//
// double zustand::calc_TdT0(double Ma)
// {
// 	double result;
// 	result = (1. / (1. + (Gamma - 1.) / 2. * Ma * Ma));
// 	return result;
// }
//
// double zustand::calc_pdp0(double Ma)
// {
// 	double result;
// 	result = std::pow(((1. + (Gamma - 1.) / 2. * Ma * Ma)),
// 			  (-Gamma / (Gamma - 1.)));
// 	return result;
// }
//
// double zustand::calc_MachAngle(double Ma)
// {
// 	double result;
// 	result = asin(1. / Ma) * 180. / M_PI;
// 	return result;
// }
//
// double zustand::calc_PM_Angle(double Ma)
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
// double zustand::calc_PM_Angle(double Ma)
// {
// 	double result;
// 	result =
// 	    (std::sqrt((Gamma + 1.) / (Gamma - 1.)) *
// 		 atan(std::sqrt((Gamma - 1.) / (Gamma + 1.) * (Ma * Ma - 1.))) -
// 	     atan(std::sqrt(Ma * Ma - 1.))) *
// 	    180. / M_PI;
// 	return result;
// }
