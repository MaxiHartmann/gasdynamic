#include "normalShock.h"
#include <cmath>
#include <iostream>

// constructor

normalShock::normalShock(int id, int inputType = 1, double inputValue = 2.0)
{
    index = id;
    input_Type = inputType;
    input_Value = inputValue;
    // ma = calcMachnumber(input_Type, input_Value);
    // calcResults();
    std::cout << "normalShock created" << std::endl;
    std::cout << "id = " << std::endl;
    std::cout << "inputType = " << input_Type << std::endl;
    std::cout << "inputValue = " << input_Value << std::endl;

}

// double normalShock::calcMachnumber(int type, double value)
// {
//     double machnumber;
// 
//     switch (type) {
//         case 1:
//             machnumber = value;
//             break;
//         case 2:
//             TdT0 = value;
//             machnumber = std::sqrt(2. / (Gamma - 1.) * (1. / TdT0 - 1.));
//             break;
//         case 3:
//             pdp0 = value;
//             machnumber = std::sqrt(2. / (Gamma - 1.) *
//                                    (std::pow(pdp0, (1. - Gamma) / Gamma) - 1.));
//             break;
//         case 4:
//             rhodrho0 = value;
//             machnumber =
//                 std::sqrt(2. / (Gamma - 1.) *
//                           (std::pow(rhodrho0, (1. - Gamma) / 1.) - 1.));
//             break;
//         case 5:
//             AdAstar = value;
//             machnumber = findMaFromAratio(AdAstar, 1);
//             break;
//         case 6:
//             AdAstar = value;
//             machnumber = findMaFromAratio(AdAstar, 2);
//             break;
//         case 7:
//             MachAngle = value;
//             machnumber = 1. / std::sin(MachAngle * pi / 180.);
//             break;
//         case 8:
//             PM_Angle = value;
//             machnumber = findMaFromPM_Angle(PM_Angle);
//             break;
// 
//         default:
//             std::cout << "Using default: Ma = 2.0" << std::endl;
//             machnumber = 2.0;
//     }
//     return machnumber;
// }

// double normalShock::findMaFromAratio(double Aratio, int flowType)
// {
//     // initial values
//     double dM = 0.1;
//     double M = 1e-6;
// 
//     // subsonic:
//     if (flowType == 1) M = 1e-6;
// 
//     // supersonic:
//     if (flowType == 2) {
//         M = 1.0;
//     }
// 
//     // iterate to solve root
//     int iterMax = 100;
//     int stepMax = 100;
//     double fj, fjp1;
//     double errTol = 1e-5;
// 
//     for (int i = 1; i < iterMax; i++) {
//         for (int j = 1; j < stepMax; j++) {
//             fj = calc_AdAstar(M) - Aratio;
//             fjp1 = calc_AdAstar(M + dM) - Aratio;
// 
//             // updating: depending on sign
//             if (fj * fjp1 > 0) {
//                 M = M + dM;
//             }
//             else {
//                 dM = dM * 0.1;
//                 // break j-loop
//                 j = stepMax;
//             }
//         }
//         // Checking convergence
//         if (std::abs(fj - fjp1) <= errTol) {
//             // std::cout << "i = " << i
//             // 	  << " and error = " << std::abs(fj - fjp1)
//             // 	  << std::endl;
// 
//             // break i-Loop
//             i = iterMax;
//         }
//     }
// 
//     return M;
// }

// double normalShock::findMaFromPM_Angle(double PM_Angle)
// {
//     // initial values
//     // must be supersonic!
//     double dM = 0.1;
//     double M = 1.0;
// 
//     // iterate to solve root
//     int iterMax = 100;
//     int stepMax = 100;
//     double fj, fjp1;
//     double errTol = 1e-5;
// 
//     for (int i = 1; i < iterMax; i++) {
//         for (int j = 1; j < stepMax; j++) {
//             fj = calc_PM_Angle(M) - PM_Angle;
//             fjp1 = calc_PM_Angle(M + dM) - PM_Angle;
// 
//             // updating: depending on sign
//             if (fj * fjp1 > 0) {
//                 M = M + dM;
//             }
//             else {
//                 dM = dM * 0.1;
//                 // break j-loop
//                 j = stepMax;
//             }
//         }
//         // Checking convergence
//         if (std::abs(fj - fjp1) <= errTol) {
//             // std::cout << "i = " << i
//             // 	  << " and error = " << std::abs(fj - fjp1)
//             // 	  << std::endl;
// 
//             // break i-Loop
//             i = iterMax;
//         }
//     }
// 
//     return M;
// }

// void normalShock::calcResults()
// {
//     machStar = std::sqrt(((Gamma + 1.) / 2. * ma * ma) /
//                          (1. + (Gamma - 1.) / 2. * ma * ma));
// 
//     TdT0 = (1. / (1. + (Gamma - 1.) / 2. * ma * ma));
// 
//     pdp0 =
//         std::pow(((1. + (Gamma - 1.) / 2. * ma * ma)), (-Gamma / (Gamma - 1.)));
// 
//     rhodrho0 =
//         std::pow((1. + (Gamma - 1.) / 2. * ma * ma), (-1. / (Gamma - 1.)));
// 
//     if (ma >= 1.0) {
//         MachAngle = asin(1. / ma) * 180. / pi;
//     }
//     else {
//         // eigentlich NAN
//         MachAngle = 0.000;
//     }
// 
//     if (ma >= 1.0) {
//         PM_Angle =
//             (std::sqrt((Gamma + 1.) / (Gamma - 1.)) *
//                  atan(std::sqrt((Gamma - 1.) / (Gamma + 1.) * (ma * ma - 1.))) -
//              atan(std::sqrt(ma * ma - 1.))) *
//             180. / pi;
//     }
//     else {
//         // eigentlich NAN
//         PM_Angle = 0.000;
//     }
// 
//     AdAstar =
//         1. /
//         (ma * std::pow((2. / (Gamma + 1.) * (1. + (Gamma - 1.) / 2. * ma * ma)),
//                        (-(Gamma + 1.) / (2. * Gamma - 2.))));
// }

void normalShock::printResults()
{
    std::cout << "----------------------------------------" << std::endl;
    std::cout << "|         Results: Normal shock         |" << std::endl;
    std::cout << "----------------------------------------" << std::endl;
    std::cout << "TODO: ..." << std::endl;
    // 	std::cout << "Position:   " << index << std::endl;
    // 	std::cout << "Gamma 	= " << Gamma << std::endl;
    // 	std::cout << "Cp 	= " << gasConst << std::endl;
    // 	std::cout << "Ma   	= " << ma << std::endl;
    // 	std::cout << "Ma*  	= " << machStar << std::endl;
    // 	std::cout << "T/T0 	= " << TdT0 << std::endl;
    // 	std::cout << "p/p0     	= " << pdp0 << std::endl;
    // 	std::cout << "rho/rho0 	= " << rhodrho0 << std::endl;
    // 	std::cout << "Ma-Angle 	= " << MachAngle << std::endl;
    // 	std::cout << "PM-Angle 	= " << PM_Angle << std::endl;
    // 	std::cout << "A / A* 	= " << AdAstar << std::endl;
}

// double normalShock::calc_AdAstar(double ma)
// {
// 	double result;
// 	result = 1. / (ma * std::pow((2. / (Gamma + 1.) *
// 				      (1. + (Gamma - 1.) / 2. * ma * ma)),
// 				     (-(Gamma + 1.) / (2. * Gamma - 2.))));
// 	return result;
// }
//
// double normalShock::calc_PM_Angle(double Ma)
// {
// 	double result;
// 	result =
// 	    (std::sqrt((Gamma + 1.) / (Gamma - 1.)) *
// 		 atan(std::sqrt((Gamma - 1.) / (Gamma + 1.) * (Ma * Ma - 1.))) -
// 	     atan(std::sqrt(Ma * Ma - 1.))) *
// 	    180. / pi;
// 	return result;
// }
//
