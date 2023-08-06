
Changelog
=========
2.0 (2023-02)
------------------
* Changed all units of nameplate rating to the base unit Watt/var/VA, from kW/kvar/kVA in Version 1.0.
* Added one time delay feature to represent the DER active and reactive grid support functions’ reaction time, and a first order lag for in applicable voltage measurement.
* Added Battery Energy Storage System (BESS) DER specific functions including State-of-Charge (SOC) calculation, and their corresponding model input parameters.
* Updated applicable smart inverter functions to consider BESS DER behaviors, including volt-watt, active power limit, and watt-var functions.
* Changed the DER operation status from ON/OFF to “Continuous Operation”, “Mandatory Operation”, “Momentary Cessation”, “Trip”, etc., to better capture the DER ride-through status, and its performance in different ride-through modes.
* Added DER ride-through performance module, which includes the DER performance under different ride-through modes, including Momentary Cessation, etc.
* Added DER model output options as current source and voltage source behind impedance.


1.0.2 (2022-07-18)
------------------
* Improve model input validity check process

1.0.1 (2022-06-17)
------------------
* Include parameter csv files into the PyPI release

1.0.0 (2022-05-17)
------------------
* First release
* Model for photovoltaic (PV) DERs, including all smart inverter functions defined in IEEE Standard 1547-2018, as well as trip and enter service behaviors
* Output active and reactive power (P, Q) for power flow analysis
* Suitable for both steady-state, quasi-static time series (QSTS) and dynamic simulations
