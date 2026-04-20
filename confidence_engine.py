# Assigns confidence scores to AI outputs

def score_response(model_output):
    return model_output.get('confidence', 0.5)
