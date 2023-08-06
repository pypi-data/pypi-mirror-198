from politicsnlp.form_of_government.regime import *

class DirectDemocracy(Regime):
    """
    Direct democracy is a form of government in which citizens have a direct say in the decision-making process, rather than being represented by elected officials. The following are some common characteristics of direct democracy:

    Popular sovereignty: Direct democracy emphasizes popular sovereignty, meaning that ultimate authority and power rests with the people.
    Citizen participation: Direct democracy involves active participation by citizens in the decision-making process, through methods such as referendums, initiatives, and popular assemblies.
    Decentralization: Direct democracy often involves a decentralized political system, with power and decision-making distributed among different levels and branches of government.
    Transparency: Direct democracy emphasizes transparency and openness in the decision-making process, with citizens having access to information and the ability to monitor and scrutinize government actions.

    """
    def __init__(self,popular_sovereignty, citizen_participation, decentralization, transparency,legitimacy, power_authority, control_of_territory, decision_making_procedures):
        super().__init__(legitimacy, power_authority, control_of_territory, decision_making_procedures)
        self.popular_sovereignty = popular_sovereignty
        self.citizen_participation = citizen_participation
        self.decentralization = decentralization
        self.transparency = transparency

    def is_direct_democracy(self):
        return True

    def emphasizes_popular_sovereignty(self):
        return self.popular_sovereignty

    def involves_citizen_participation(self):
        return self.citizen_participation

    def involves_decentralization(self):
        return self.decentralization

    def emphasizes_transparency(self):
        return self.transparency
