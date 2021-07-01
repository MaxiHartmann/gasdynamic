class zustand {
    private:
	const double pi = 3.14159265359;
	const double Gamma = 1.4;
	const double gasConst = 287.058;

	int index;
	double ma;

	double machStar;
	double TdT0;
	double pdp0;
	double rhodrho0;
	double MachAngle;
	double PM_Angle;
	double AdAstar;

    public:
	// constructor declaration
	zustand(int id, double mach);

	void calcResults();
	void printResults();
};
