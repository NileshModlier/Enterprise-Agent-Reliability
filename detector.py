# Detects intent shift across conversation turns

def detect_intent_drift(previous_intent, current_intent, confidence):
    if confidence < 0.7 or previous_intent != current_intent:
        return True
    return False
