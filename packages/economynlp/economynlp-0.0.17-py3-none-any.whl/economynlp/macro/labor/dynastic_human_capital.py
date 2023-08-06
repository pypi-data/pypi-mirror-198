from economynlp.macro.labor.human_capital import *
class DynasticHumanCapital(HumanCapital):
    """
 Dynastic human capital refers to the accumulation of human capital within a family or lineage over generations. In contrast, regular or ordinary human capital refers to the skills, knowledge, and experience that an individual acquires through education and work experience. Some of the key differences between dynastic human capital and regular human capital include:

Inheritance: Dynastic human capital is inherited within a family or lineage, while regular human capital is acquired by individuals through education and work experience.
Intergenerational transmission: Dynastic human capital is transmitted across generations within a family or lineage, while regular human capital is acquired and developed during an individual's lifetime.
Concentration: Dynastic human capital tends to be concentrated within a small group of families or lineages, while regular human capital is distributed more broadly across the population.
Durability: Dynastic human capital can be more durable and long-lasting than regular human capital, as it is transmitted across generations and can be reinforced by family traditions and cultural norms.   
    """
    def __init__(self, inheritance, intergenerational_transmission, concentration, durability,investment, productivity, non_transferable, depreciation):
        super().__init__(investment, productivity, non_transferable, depreciation)
        self.inheritance = inheritance
        self.intergenerational_transmission = intergenerational_transmission
        self.concentration = concentration
        self.durability = durability

    def describe_dynastic_human_capital(self):
        print("Dynastic human capital is inherited within a family or lineage:", self.inheritance)
        print("Dynastic human capital is transmitted across generations within a family or lineage:", self.intergenerational_transmission)
        print("Dynastic human capital tends to be concentrated within a small group of families or lineages:", self.concentration)
        print("Dynastic human capital can be more durable and long-lasting than regular human capital, as it is transmitted across generations and can be reinforced by family traditions and cultural norms:", self.durability)
