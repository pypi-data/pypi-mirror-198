class DiminishingMarginalUtility:
    """
 The Law of Diminishing Marginal Utility is a principle in economics that states that as a person consumes more of a good or service, the additional satisfaction (or utility) they derive from each additional unit will decrease. Some of the characteristics of the Law of Diminishing Marginal Utility include:

Decreasing marginal utility: The Law of Diminishing Marginal Utility predicts that the marginal utility of each additional unit of a good or service will decrease as a person consumes more of it.
Consumer behavior: The Law of Diminishing Marginal Utility explains consumer behavior, as individuals are less likely to continue consuming a good or service at the same rate once they have reached a point of diminishing marginal utility.
Optimal consumption: The Law of Diminishing Marginal Utility can be used to determine the optimal level of consumption for a good or service, as individuals will consume up to the point where the marginal utility is equal to the price they pay for the good or service.
   
    """
    def __init__(self, decreasing_marginal_utility, consumer_behavior, optimal_consumption):
        self.decreasing_marginal_utility = decreasing_marginal_utility
        self.consumer_behavior = consumer_behavior
        self.optimal_consumption = optimal_consumption

    def describe_diminishing_marginal_utility(self):
        print("The Law of Diminishing Marginal Utility predicts that the marginal utility of each additional unit of a good or service will decrease as a person consumes more of it:", self.decreasing_marginal_utility)
        print("The Law of Diminishing Marginal Utility explains consumer behavior, as individuals are less likely to continue consuming a good or service at the same rate once they have reached a point of diminishing marginal utility:", self.consumer_behavior)
        print("The Law of Diminishing Marginal Utility can be used to determine the optimal level of consumption for a good or service, as individuals will consume up to the point where the marginal utility is equal to the price they pay for the good or service:", self.optimal_consumption)
