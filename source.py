import math 

#LIST OF REFERENCES
#[1] AA10 - Accident Analysis Report - Public: Water leakage in Monolith Vessel, ESS-0052199
#[2] ESS - Activity transport and dose calculation models and tools used in safety analyses at ESS, ESS-0092033

def instant_release(x):
    """
    Instant release source at time 0.
    """
    if x==0:
        return 1
    else:
        return 0 

def constant_release(x, tmin = 0, tmax = 1.4*10**6 ):
    """
    Constant release source between tmin e tmax.
    Defaults from reference ESS-0052199, 700 kg of water pumped at the rate of 1.80 Kg/hours 
    """
    if x<tmax:
        return 1/(tmax-tmin)
    else:
        return 0 

class Source:
    """
    Define the class for the radioactivity source. Defaults from ESS-0052199
    """
    def __init__(self, name = "", half_life = 1*10**9, function = constant_release):
        self.name = name
        self.half_life = half_life
        self.function = function

    def getNuclei(self):
        """
        Return the number of nuclei of the source
        """
        return int(self.half_life/math.log(2))

    def getDecayConst(self):
        """
        Return the decay constant lambda of the source 
        """
        return 0.693/self.half_life

    def Eval(self, time):
        """
        Evaluate the source at a certain time 
        """
        return self.function(float(time))
