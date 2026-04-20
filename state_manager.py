# Maintains structured conversation state

class ConversationState:
    def __init__(self):
        self.intent_history = []
        self.confidence_scores = []
        self.context_window = []
