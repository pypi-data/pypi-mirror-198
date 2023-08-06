from politicsnlp.movement.political_movement import *

class TheEnlightenment(PoliticalMovement):
    """
    #### A class representing the philosophical movement of the Enlightenment, which emerged in the 18th century in Europe and emphasized reason,
    individualism, and progress, and sought to challenge traditional authority and institutions.
    
    The Enlightenment was a philosophical movement that emerged in the 18th century in Europe. It emphasized reason, individualism, and progress, and sought to challenge traditional authority and institutions. Enlightenment thinkers believed that reason and scientific inquiry could solve social and political problems, and sought to promote democracy, human rights, and religious tolerance. The Enlightenment laid the foundation for modern western political and social thought.
    
    Attributes:
    - emphasis_on_reason: A boolean indicating whether the Enlightenment emphasized the importance of reason and scientific inquiry in solving
    social and political problems.
    - promotion_of_democracy: A boolean indicating whether the Enlightenment sought to promote democracy, human rights, and religious tolerance.
    
    Methods:
    - advocate_for_reason: Advocates for the importance of reason and scientific inquiry in solving social and political problems.
    - promote_democracy: Promotes democracy, human rights, and religious tolerance.
    """
    
    def __init__(self, emphasis_on_reason, promotion_of_democracy,ideology, leaders, members, goals):
        """
        Initializes a TheEnlightenment instance with booleans indicating whether the importance of reason and scientific inquiry in solving
        social and political problems and the promotion of democracy, human rights, and religious tolerance are emphasized.
        """
        super().__init__(ideology, leaders, members, goals)
        self.emphasis_on_reason = emphasis_on_reason
        self.promotion_of_democracy = promotion_of_democracy
    
    def advocate_for_reason(self):
        """
        Advocates for the importance of reason and scientific inquiry in solving social and political problems.
        """
        pass
    
    def promote_democracy(self):
        """
        Promotes democracy, human rights, and religious tolerance.
        """
        pass
