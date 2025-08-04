from ecdsa import SigningKey
class SignatureEngine:
    def __init__(self): self.sk = SigningKey.generate()
    def sign(self, msg): return self.sk.sign(msg)