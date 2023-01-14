#ifndef ISENTROPICFLOW_H
#define ISENTROPICFLOW_H


class isentropicFlow
{
// public:
//     isentropicFlow();
private:
    const double pi = 3.14159265359;
    // const double Gamma = 1.4;
    const double gasConst = 287.058;

    int index;
    int input_Type;
    double input_Value;
    double Gamma;

//     double ma;
//     double machStar;
//     double TdT0;
//     double pdp0;
//     double rhodrho0;
//     double MachAngle;
//     double PM_Angle;
//     double AdAstar;

    double findMaFromAratio(double Aratio, int flowType);

    double findMaFromPM_Angle(double PM_Angle);

    double calcMachnumber(int type, double value);

    void calcResults();

    double calc_AdAstar(double ma);

    double calc_PM_Angle(double Ma);

public:
    // constructor declaration
    isentropicFlow(int id, int inputType, double inputValue, double gamma);

    void printResults();

    double ma;
    double machStar;
    double TdT0;
    double pdp0;
    double rhodrho0;
    double MachAngle;
    double PM_Angle;
    double AdAstar;

    double pdpstar;
    double rhodrhostar;
    double TdTstar;
};

#endif // ISENTROPICFLOW_H
