from source import Source
import math
import numpy as np

#LIST OF REFERENCES
#[1] AA10 - Accident Analysis Report - Public: Water leakage in Monolith Vessel, ESS-0052199
#[2] ESS - Activity transport and dose calculation models and tools used in safety analyses at ESS, ESS-0092033
#[3] AA10_LP-102-PIE1 Publ UnMit - Transport_calc_a020_out_181014.xlsx

class Transport:
    """
    Define the class for the transport of activity through rooms.
    Details of the accidents like rooms number and volumes should be defined if not default.
    Times in seconds and volumes in m^3
    """
    def __init__(self, source, time_step = 100, final_time = 1500000):
        self.source = source
        self.time_step = time_step 
        self.final_time = final_time

        self.room_number = 0
        self.V = np.array([])
        self.Flows = np.matrix([[]])
        self.T = np.matrix([[]])
        self.D = np.array([])

        self.emission_fraction = np.array([0.01, 0.1, 0.5, 0.9, 0.99])
        self.emission_times = np.zeros(self.emission_fraction.size)
        self.steps_number = 0
        self.N = np.matrix([[]])

    def Init(self, **kwargs):
        """
        Method for the initialization of transport. If called with no arguments, default case is assumed.

        Keyward Args:
            rooms_number (int) = rooms + environment
            V (np.array)  = list of rooms volume
            Flows (np.matrix) = matrix flows from i to j
            D (np.array) = deposition array
            T (np.matrix) = Transport matrix
        """
        if "rooms_number" in kwargs:
            self.room_number =  kwargs["rooms_number"]
        else:
            self.room_number = 4

        if "V" in kwargs:
            self.V = kwargs["V"]
        else:
            self.V = np.zeros(self.room_number)
            #array of volumes from [3]
            self.V[0] = 42
            self.V[1] = 812
            self.V[2] = 40700
            self.V[3] = 1 #EXTERNAL VOLUME NOT RELEVANT

        if "Flows" in kwargs:
            self.Flows = kwargs["Flows"]
        else:
            self.Flows = np.zeros((self.room_number,self.room_number))
            #constant flows, reference [3]
            self.Flows[0,1] = 0.03
            self.Flows[1,2] = 0.045167
            self.Flows[2,3] = 2.261167

        if "D" in kwargs:
            self.D = kwargs["D"]
        else:
            #Deposition array
            self.D = np.zeros(self.room_number) 

        if "T" in kwargs:
            self.T = kwargs["T"]
        else:
            self.T = np.zeros((self.room_number,self.room_number))
            #transport matrix
            self.T[0,1] = self.Flows[0,1]*self.time_step/self.V[0]
            self.T[1,2] = self.Flows[1,2]*self.time_step/self.V[1]
            self.T[2,3] = self.Flows[2,3]*self.time_step/self.V[2]

            #Define the diagonal Tii as 1 - Di - sum_j(Tij)
            sum_out_flows = self.T.sum(axis=1)
        
            for i in range(self.room_number):
                self.T[i,i] = 1 - self.D[i] - sum_out_flows[i]
        

    def Go(self):
        """
        Call this method when transport parameters are correctly set.
        After this, emission_times can be retrieved.
        """
        self.steps_number = int(self.final_time/self.time_step)
        self.N = np.zeros((self.steps_number+1,self.room_number))
        time_mark = 0

        #for step in range(self.steps_number)
        


s = Source()
t = Transport(s)
t.Init()

print(np.array(t.emission_fraction).size)

    