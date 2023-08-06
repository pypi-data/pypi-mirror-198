class BusinessCycle:
    """
    The business cycle is a recurring pattern of growth and decline in economic activity over time. It is characterized by alternating periods of expansion and contraction in economic output, employment, and other economic indicators. Some of the characteristics of the business cycle include:

Expansion: During the expansion phase, the economy experiences growth in output, employment, and other indicators of economic activity.
Peak: The peak marks the end of the expansion phase and the beginning of the contraction phase. At the peak, the economy has reached its maximum level of output and employment.
Contraction: During the contraction phase, the economy experiences a decline in output, employment, and other indicators of economic activity.
Trough: The trough marks the end of the contraction phase and the beginning of the expansion phase. At the trough, the economy has reached its lowest level of output and employment.
Cyclical fluctuations: The business cycle is characterized by cyclical fluctuations in economic activity that are driven by various factors such as changes in demand, supply shocks, and monetary policy.
    """
    def __init__(self, expansion, peak, contraction, trough, cyclical_fluctuations):
        self.expansion = expansion
        self.peak = peak
        self.contraction = contraction
        self.trough = trough
        self.cyclical_fluctuations = cyclical_fluctuations

    def describe_business_cycle(self):
        print("During the expansion phase, the economy experiences growth in output, employment, and other indicators of economic activity:", self.expansion)
        print("The peak marks the end of the expansion phase and the beginning of the contraction phase. At the peak, the economy has reached its maximum level of output and employment:", self.peak)
        print("During the contraction phase, the economy experiences a decline in output, employment, and other indicators of economic activity:", self.contraction)
        print("The trough marks the end of the contraction phase and the beginning of the expansion phase. At the trough, the economy has reached its lowest level of output and employment:", self.trough)
        print("The business cycle is characterized by cyclical fluctuations in economic activity that are driven by various factors such as changes in demand, supply shocks, and monetary policy:", self.cyclical_fluctuations)
