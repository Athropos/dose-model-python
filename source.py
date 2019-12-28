
#LIST OF REFERENCES
#[1] AA10 - Accident Analysis Report - Public: Water leakage in Monolith Vessel, ESS-0052199
#[2] ESS - Activity transport and dose calculation models and tools used in safety analyses at ESS, ESS-0092033

def instant_release(x):
    if x==0:
        return 1
    else:
        return 0 

def constant_release(x):
    tmin = 0
    tmax = 1.4*10**6 #reference [1], 700 kg of water pumped at the rate of 1.80 Kg/hours 
    if x<tmax:
        return 1/(tmax-tmin)
    else:
        return 0 
