class RateHikingPath:
    """
    #### A class representing a rate-hiking path, which consists of a series of planned or projected interest rate increases over a certain period by a central bank or monetary authority.

    Features:
    - The "rate-hiking path" refers to a series of planned or projected increases in interest rates over a certain period of time by a central bank or monetary authority. This path is usually based on economic indicators, such as inflation and unemployment rates, and is meant to control the economy and achieve stability. The rate-hiking path can impact borrowing costs, investments, and consumer spending.
    
    Attributes:
    - central_bank (str): The name of the central bank or monetary authority.
    - rate_increases (list): A list of tuples containing the date and the corresponding
                             interest rate increase (e.g., [('2023-03-20', 0.25), ('2023-09-20', 0.25)]).
    """

    def __init__(self, central_bank, rate_increases):
        """
        Initialize a RateHikingPath instance.

        Args:
        - central_bank (str): The name of the central bank or monetary authority.
        - rate_increases (list): A list of tuples containing the date and the corresponding
                                 interest rate increase.
        """
        self.central_bank = central_bank
        self.rate_increases = rate_increases
