from politicsnlp.ideology.economic_liberalism import *

class Ordoliberalism(EconomicLiberalism):
    """
    #### A class representing the social market economic philosophy of ordoliberalism, which emphasizes the importance of a competitive market economy
    and the role of government in creating and maintaining that market.
    
    Ordoliberalism is a social market economic philosophy that emphasizes the importance of a competitive market economy, as well as the role of government in creating and maintaining that market. It advocates for a stable monetary policy, fiscal discipline, and a strong legal system to enforce contracts and protect property rights. Ordoliberalism also emphasizes the importance of education and training to promote innovation and economic growth.
    
    Attributes:
    - competitive_market: A boolean indicating whether ordoliberalism emphasizes the importance of a competitive market economy.
    - government_role: A boolean indicating whether ordoliberalism emphasizes the role of government in creating and maintaining a competitive market.
    - policy_priorities: A list of policy priorities that are promoted by ordoliberalism, such as stable monetary policy, fiscal discipline,
    and a strong legal system.
    
    Methods:
    - promote_competitive_market(): Promotes a competitive market economy.
    - advocate_for_government_role(): Advocates for the role of government in creating and maintaining a competitive market.
    """
    
    def __init__(self, competitive_market, government_intervention, policy_priorities):
        """
        Initializes an Ordoliberalism instance with booleans indicating whether the importance of a competitive market economy and the role
        of government in creating and maintaining that market are emphasized, and a list of policy priorities.
        """
        super().__init__(government_intervention, policy_priorities)
        self.competitive_market = competitive_market
    
    def promote_competitive_market(self):
        """
        Promotes a competitive market economy.
        """
        pass
    
    def advocate_for_government_role(self):
        """
        Advocates for the role of government in creating and maintaining a competitive market.
        """
        pass
