from economynlp.environment.economic_environment.economic_environment import *

class CreditEnvironment(EconomicEnvironment):
    def __init__(self,interest_rate=None,default_rate=None,economic_growth=None, inflation=None, unemployment=None, exchange_rate=None):
        super().__init__(economic_growth, inflation, unemployment, exchange_rate,interest_rate)
        self.add_factor("interest_rate", 0)
        self.add_factor("default_rate", 0)

def credit_tightening(interest_rate):
    # 如果利率超过 5%，则认为信贷条件已经紧缩
    if interest_rate > 0.05:
        return "信贷条件已经紧缩。"
    # 如果利率不足 5%，则认为信贷条件宽松
    else:
        return "信贷条件宽松。"
def lending_tightening(interest_rate, economic_growth_rate):
    # 如果利率高于 5% 或者经济增长率低于 2%，则认为 lending will tighten
    if interest_rate > 0.05 or economic_growth_rate < 0.02:
        return "lending will tighten"
    # 否则，认为 lending will not tighten
    else:
        return "lending will not tighten"