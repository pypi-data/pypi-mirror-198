class GoodGovernance:
    """
 A government that is considered to be "good" or "effective" typically has the following characteristics:

Transparency: The government should operate in a transparent manner, providing clear and accessible information about its activities, policies, and decision-making processes to the public.
Accountability: The government should be accountable to the people it serves, and should take responsibility for its actions and decisions.
Responsiveness: The government should be responsive to the needs and concerns of its citizens, and should take action to address their concerns in a timely and effective manner.
Efficiency: The government should operate efficiently and effectively, using resources wisely and making decisions that result in the greatest benefit for the greatest number of people.
Fairness: The government should treat all citizens equally and fairly, without discrimination or favoritism.   
    """
    def __init__(self, transparency, accountability, responsiveness, efficiency, fairness):
        self.transparency = transparency
        self.accountability = accountability
        self.responsiveness = responsiveness
        self.efficiency = efficiency
        self.fairness = fairness
    
    def get_transparency(self):
        return self.transparency
    
    def get_accountability(self):
        return self.accountability
    
    def get_responsiveness(self):
        return self.responsiveness
    
    def get_efficiency(self):
        return self.efficiency
    
    def get_fairness(self):
        return self.fairness
    
    def set_transparency(self, transparency):
        self.transparency = transparency
    
    def set_accountability(self, accountability):
        self.accountability = accountability
    
    def set_responsiveness(self, responsiveness):
        self.responsiveness = responsiveness
    
    def set_efficiency(self, efficiency):
        self.efficiency = efficiency
    
    def set_fairness(self, fairness):
        self.fairness = fairness
