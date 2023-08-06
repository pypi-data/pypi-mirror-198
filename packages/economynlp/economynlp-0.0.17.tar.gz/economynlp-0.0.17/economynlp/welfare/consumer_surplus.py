class ConsumerSurplus:
    """
    Consumer Surplus is a measure of the welfare or benefit that consumers receive from purchasing a good or service at a price lower than what they are willing to pay. It is calculated as the difference between the maximum price a consumer is willing to pay and the actual price they pay for a good or service.

Some of the features of Consumer Surplus include:

Willingness to pay: Consumer Surplus is based on the difference between what consumers are willing to pay and the actual price they pay. This indicates the value that consumers place on a good or service.
Marginal utility: Consumer Surplus is derived from the concept of marginal utility, which is the additional utility that a consumer receives from consuming one additional unit of a good or service.
Consumer sovereignty: Consumer Surplus reflects the idea of consumer sovereignty, which is the principle that consumers should have the power to decide what goods and services are produced.
Diminishing marginal utility: Consumer Surplus takes into account the concept of diminishing marginal utility, which states that as a consumer consumes more units of a good or service, the additional utility they receive from each additional unit decreases.

    """
    def __init__(self, willingness_to_pay, actual_price, quantity):
        self.willingness_to_pay = willingness_to_pay
        self.actual_price = actual_price
        self.quantity = quantity
        self.marginal_utility = self.calculate_marginal_utility()
        self.consumer_sovereignty = True
        self.diminishing_marginal_utility = True

    def calculate_surplus(self):
        # Calculate the consumer surplus
        return (self.willingness_to_pay - self.actual_price) * self.quantity

    def calculate_marginal_utility(self):
        # Calculate the marginal utility of the good or service
        pass
