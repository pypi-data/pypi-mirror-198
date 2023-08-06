class Inflation:
    """
    ### Example:
    ```
    inflation = Inflation(100, 0.05, 0.02)
    inflation.print_price_level()  # Output: Current price level is:  100
    
    inflation.update_price_level()
    inflation.print_price_level()  # Output: Current price level is:  107.0
    
    inflation.update_price_level()
    inflation.print_price_level()  # Output: Current price level is:  114.49
    ```
    """
    def __init__(self, initial_price_level, money_supply, demand):
        self.price_level = initial_price_level
        self.money_supply = money_supply
        self.demand = demand
        
    def update_price_level(self):
        # 根据货币供应量和需求过剩的程度更新物价水平
        self.price_level *= (1 + self.money_supply + self.demand)
        
    def print_price_level(self):
        print("Current price level is: ", self.price_level)
def fight_inflation(inflation_rate):
    """
    Determine if action needs to be taken to fight inflation based on the current inflation rate.

    Args:
    inflation_rate (float): The current inflation rate as a decimal.

    Returns:
    str: A message indicating if action needs to be taken to fight inflation.
    """
    if inflation_rate > 0.05:
        return "Inflation is high. Action needs to be taken to fight inflation."
    else:
        return "Inflation is under control. No action is needed to fight inflation."
