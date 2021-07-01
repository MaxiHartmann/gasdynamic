class normalShock {
    private:
	const double pi = 3.14159265359;
	const double Gamma = 1.4;
	const double gasConst = 287.058;

	int index;
	int input_Type;
	double input_Value;

    double M1;
    double M2;
    double p02dp01;
    double p1dp02;
    double p2dp1;
    double rho2drho1;
    double T2dT1;

// 	double findMaFromAratio(double Aratio, int flowType);
// 
// 	double findMaFromPM_Angle(double PM_Angle);
// 
// 	double calcMachnumber(int type, double value);
// 
// 	void calcResults();
// 
// 	double calc_AdAstar(double ma);
// 
// 	double calc_PM_Angle(double Ma);
// 
    public:
	// constructor declaration
	normalShock(int id, int inputType, double inputValue);

	void printResults();
};
