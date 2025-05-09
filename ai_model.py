import random

class AIModel:
    def __init__(self):
        # Preload knowledge, models, personalities, etc.
        self.personalities = {
            "default": "friendly",
            "flirty": "romantic",
            "sassy": "savage"
        }

    def generate_response(self, user_input, mood="default"):
        """Generates a response based on input and mood."""
        if not user_input:
            return "Say something, will ya? I'm not a mind reader... yet."

        responses = {
            "default": [
                "Interesting! Tell me more.",
                "Okay, got it!",
                "Hmm, let me think about that..."
            ],
            "flirty": [
                "Is it hot in here or is it just your message? 😏",
                "You talk like poetry... and I’m weak for that.",
                "Careful, keep typing like that and I might fall for you."
            ],
            "sassy": [
                "Oh honey, that’s cute.",
                "You really woke me up for *that*?",
                "Try again. I know you can do better 😌"
            ]
        }

        mood_responses = responses.get(mood, responses["default"])
        return random.choice(mood_responses)

    def set_personality(self, mode):
        """Optional: change model's vibe/mood externally."""
        if mode in self.personalities:
            return f"Switched to {self.personalities[mode]} mode."
        return "I have no idea what that vibe is, fam."

