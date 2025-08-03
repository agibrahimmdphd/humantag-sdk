from src.entropy_analyzer import EntropyAnalyzer

def test_entropy_fluctuates():
    e = EntropyAnalyzer()
    data = [1.0, 1.2, 1.1, 1.4, 1.3]
    for d in data:
        e.add_sample(d)
    assert e.compute_entropy_score() > 0