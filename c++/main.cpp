#include <cmath>
#include <iostream>

#define gamma 1.4
#define gasConst 287.058

// classes example
// class state {
//     public:
// 	void set_values(int, double);
//     private:
// 	int index;
// 	double mach;
//
// };

// void state::set_values(int idx, double Ma)
// {
// 	index = idx;
// 	mach = Ma;
// }

double calc_machStar(double Ma)
{
	double result;
	result = std::sqrt(((gamma + 1.) / 2. * Ma * Ma) /
			   (1. + (gamma - 1.) / 2. * Ma * Ma));
	return result;
}

double calc_TdT0(double Ma)
{
	double result;
	result = (1. / (1. + (gamma - 1.) / 2. * Ma * Ma));
	return result;
}
double calc_pdp0(double Ma)
{
	double result;
	result = std::pow(((1. + (gamma - 1.) / 2. * Ma * Ma)),
			  (-gamma / (gamma - 1.)));
	return result;
}
double calc_MachAngle(double Ma)
{
	double result;
	result = asin(1. / Ma) * 180. / M_PI;
	return result;
}
double calc_PM_Angle(double Ma)
{
	double result;
	result =
	    (std::sqrt((gamma + 1.) / (gamma - 1.)) *
		 atan(std::sqrt((gamma - 1.) / (gamma + 1.) * (Ma * Ma - 1.))) -
	     atan(std::sqrt(Ma * Ma - 1.))) *
	    180. / M_PI;
	return result;
}

int main()
{
	// char op;
	double mach;

	std::cout << "Enter Machnumber:\n ";
	std::cin >> mach;

	std::cout << "Ma   	= " << mach << std::endl;
	std::cout << "Ma*  	= " << calc_machStar(mach) << std::endl;
	std::cout << "T/T0 	= " << calc_TdT0(mach) << std::endl;
	std::cout << "p/p0     	= " << calc_pdp0(mach) << std::endl;
	std::cout << "Ma-Angle 	= " << calc_MachAngle(mach) << std::endl;
	std::cout << "PM-Angle 	= " << calc_PM_Angle(mach) << std::endl;

	return 0;
}

