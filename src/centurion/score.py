class Score:
    """
    Calculates score for a finished deal:
     - basePoints = number of cards played
     - penalty    = 1 point per 10 over 100
     - finalPoints = basePoints – penalty
    """

    def __init__(self):
        self.basePoints: int = 0
        self.penalty: int = 0
        self.finalPoints: int = 0

    def computeBase(self, cardsPlayed: int) -> int:
        """Set and return basePoints."""
        self.basePoints = cardsPlayed
        return self.basePoints

    def computePenalty(self, fromTotal: int) -> int:
        """Set and return penalty (0 if ≤100, else floor((total–100)/10))."""
        if fromTotal <= 100:
            self.penalty = 0
        else:
            self.penalty = (fromTotal - 100) // 10
        return self.penalty

    def computeFinal(self) -> int:
        """Set and return finalPoints = basePoints – penalty."""
        self.finalPoints = self.basePoints - self.penalty
        return self.finalPoints
