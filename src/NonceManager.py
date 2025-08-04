class NonceManager:
    used = set()
    def is_fresh(self, n): return n not in self.used