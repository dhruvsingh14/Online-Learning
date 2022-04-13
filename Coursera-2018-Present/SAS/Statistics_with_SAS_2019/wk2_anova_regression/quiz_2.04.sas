%let path = C:\Users\dhnsingh\Documents\EST142;
libname stat1 "&path\data";

**********************;
* Practice Quiz 2.04  ;
**********************;

proc contents data = stat1.ameshousing;
run;

proc glm data=cr.ameshousing;
    class lot_config;
    model log_price = lot_config;
    means lot_config/hovtest;
run;
quit;

**********************;
* Quiz: One-way Anova ;
**********************;
data garlic;
	set stat1.garlic;
run;

* descriptive statistics;
proc means data = garlic;
	class fertilizer;
run;

* plotting means difference;
proc sgplot data = garlic;
	vbox bulbwt / category = fertilizer
				  connect = mean;
	title "Bulb Weight Differences Across Fertilizer";
run;

/* performing one way anova to test fertilizer effect on bulb weight */
proc glm data=garlic plots=diagnostics;
    class fertilizer;
    model bulbwt = fertilizer;
    means fertilizer/hovtest;
run;
quit;
