from politicsnlp.form_of_government.regime import *

class Monarchy(Regime):
    def __init__(self, monarch,legitimacy, power_authority, control_of_territory, decision_making_procedures):
        super().__init__(legitimacy, power_authority, control_of_territory, decision_making_procedures)
        self.monarch = monarch

    def make_decision(self, decision):
        # Code to implement the decision-making process in a monarchy
        pass

    def uphold_ceremonial_duties(self):
        # Code to uphold the ceremonial duties of the monarch
        pass

    def control_access_to_power(self):
        # Code to control access to power and limit political participation to the monarch and their advisors
        pass
