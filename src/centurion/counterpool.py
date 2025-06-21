class CounterPool:
    """
    Shared pool of counters. Players take points from here.
    """

    def __init__(self, initial: int):
        self.remainingCounters: int = initial

    def take(self, n: int) -> int:
        """
        Remove up to n counters from the pool.
        Returns the actual number taken (could be less if pool runs out).
        """
        taken = min(n, self.remainingCounters)
        self.remainingCounters -= taken
        return taken
