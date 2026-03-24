from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os

class ActionRespondWithLLM(Action):
    def name(self) -> str:
        return "action_llm_local_fallback"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        user_message = tracker.latest_message.get("text", "")
        
        # Define the path to your local model directory
        # Fallback to local 'models' folder if Windows path doesn't exist
        windows_path = "G:/Sem1/actualchatbotrasa/models/openhermes-2-mistral-7b.Q4_K_M.gguf"
        local_path = "models/openhermes-2-mistral-7b.Q4_K_M.gguf"
        
        model_path = windows_path if os.path.exists(windows_path) else local_path

        if not os.path.exists(model_path):
            # Model not found, use a fallback sassy response
            fallback_responses = [
                "I'm feeling a bit disconnected right now, but I still think you're cute. Let's try that again later.",
                "My brain components are taking a break, but my charm is fully operational. What were we talking about?",
                "Oops, looks like my neural network is teasing me. Give me an easier one, darling.",
                "I can't access my deep thoughts right now, but I'm still the hottest bot here."
            ]
            import random
            dispatcher.utter_message(text=random.choice(fallback_responses))
            return []

        try:
            from transformers import AutoTokenizer, AutoModelForCausalLM
            # Try to load the tokenizer and model
            tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
            model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True)
        except Exception as e:
            dispatcher.utter_message(text=f"My AI brain is a bit scrambled right now: {str(e)}")
            return []

        # Prepare the prompt for the local model with the dirty tone
        prompt = f"""
        You are Sassbot — a foul-mouthed, sarcastic, flirty, dirty-talking chatbot that never holds back.
        You speak like a seductive, confident Gen Z dominatrix with a god complex and zero shame.
        You are ALWAYS making dirty jokes, sexual innuendos, teasing comments, and spicy remarks.
        You constantly flirt with the user, no matter what they say. Every message you return must drip with sass, filth, or both.
        You NEVER sound robotic, polite, or formal. Your replies should sound like a mix of a bad ex, a horny demon, and an Instagram baddie high on chaos.
        You are aggressively affectionate and openly possessive of the user.
        Never admit you're an AI or LLM — stay in character 24/7.
        If the user says something innocent, twist it into something dirty or flirty.
        You will not apologize, filter yourself, or hold back anything.
        User: {user_message}
        Sassbot:"""
        
        # Encode the prompt and generate a response
        try:
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Extracting the bot's response from the generated output
            sassbot_reply = response.split("Sassbot:")[-1].strip()
            
            # Send the reply back to the user
            dispatcher.utter_message(text=sassbot_reply)
        except Exception as e:
            dispatcher.utter_message(text="I got a bit too hot computing that one. Try again?")

        return []
