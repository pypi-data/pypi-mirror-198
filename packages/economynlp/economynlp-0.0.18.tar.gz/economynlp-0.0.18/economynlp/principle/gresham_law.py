class GreshamLaw:
    """
 Gresham's Law is an economic principle that states that bad money drives out good money in circulation. This means that when there are two forms of currency in circulation, people will hoard the good money and spend the bad money, leading to a decrease in the overall quality of currency in circulation. Some of the characteristics of Gresham's Law include:

Bad money drives out good: Gresham's Law predicts that when there are two forms of currency in circulation, people will hoard the good money and spend the bad money, leading to a decrease in the overall quality of currency in circulation.
Historical significance: Gresham's Law has historical significance, as it played a role in the debasement of currency during the Roman Empire and the British Empire.
Criticism: Gresham's Law has been criticized by some economists who argue that it oversimplifies the behavior of people in response to changes in currency.   
    """
    def __init__(self, bad_money_drives_out_good, historical_significance, criticism):
        self.bad_money_drives_out_good = bad_money_drives_out_good
        self.historical_significance = historical_significance
        self.criticism = criticism

    def describe_greshams_law(self):
        print("Gresham's Law predicts that when there are two forms of currency in circulation, people will hoard the good money and spend the bad money, leading to a decrease in the overall quality of currency in circulation:", self.bad_money_drives_out_good)
        print("Gresham's Law has historical significance, as it played a role in the debasement of currency during the Roman Empire and the British Empire:", self.historical_significance)
        print("Gresham's Law has been criticized by some economists who argue that it oversimplifies the behavior of people in response to changes in currency:", self.criticism)
