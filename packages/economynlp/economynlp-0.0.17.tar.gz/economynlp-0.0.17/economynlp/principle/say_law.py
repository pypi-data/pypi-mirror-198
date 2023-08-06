class SayLaw:
    """
 Say's Law is an economic principle that states that supply creates its own demand, meaning that the production of goods and services will generate enough income to ensure that all goods and services produced are sold. Some of the characteristics of Say's Law include:

Production leads to income: Say's Law predicts that production of goods and services will create income for workers, which will in turn generate demand for other goods and services.
No general overproduction: Say's Law suggests that there will not be general overproduction in the economy, as the production of goods and services will create enough income to ensure that all goods and services produced are sold.
Criticism: Say's Law has been criticized by some economists who argue that it does not take into account the possibility of market failures or the role of aggregate demand in the economy.   
    """
    def __init__(self, production_leads_to_income, no_general_overproduction, criticism):
        self.production_leads_to_income = production_leads_to_income
        self.no_general_overproduction = no_general_overproduction
        self.criticism = criticism

    def describe_says_law(self):
        print("Say's Law predicts that production of goods and services will create income for workers, which will in turn generate demand for other goods and services:", self.production_leads_to_income)
        print("Say's Law suggests that there will not be general overproduction in the economy, as the production of goods and services will create enough income to ensure that all goods and services produced are sold:", self.no_general_overproduction)
        print("Say's Law has been criticized by some economists who argue that it does not take into account the possibility of market failures or the role of aggregate demand in the economy:", self.criticism)
