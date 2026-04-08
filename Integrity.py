def compute_integrity(damage, maintenance, feedback):
    score = (0.4 * (1 - damage) +
             0.3 * maintenance +
             0.3 * feedback) * 100
    return score
