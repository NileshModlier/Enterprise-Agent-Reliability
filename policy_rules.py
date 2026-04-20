# Deterministic policy rules for agent behavior

def evaluate_policy(confidence, drift_detected):
    if drift_detected or confidence < 0.6:
        return 'ESCALATE'
    return 'PROCEED'
