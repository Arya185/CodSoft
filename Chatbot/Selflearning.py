import random
import re

class MentalHealthBot:
    negative_res = ("no","nope","nah","naw","not feeling up to it","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    
    random_question = (
        "How are you feeling today?",
        "What's been on your mind lately?",
        "Do you find it difficult to express your emotions?",
        "Have you been sleeping well?",
        "Are you experiencing any stress or anxiety?",
    )
    
    def __init__(self):
        self.bot_responses = {
            'describe_feelings_intent': r'.*\s*feel.*',
            'answer_why_intent': r'why\sare.*',
            'about_mental_health': r'.*\s*mental health.*'
        }
    
    def greet(self):
        self.name = input("Hello, I'm here to chat with you. What's your name?\n")
        will_help = input(
            f"Hi {self.name}, I'm here to support you with your mental health. Would you like to talk?\n")
        if will_help in self.negative_res:
            print("Take care of yourself!")
            return 
        self.chat()
        
    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Take care and remember, I'm here if you need me.")
                return True

    def make_exit(self, reply):
        for command in self.negative_res:
            if reply == command:
                print("Take care and remember, I'm here if you need me.")
                return True

    def chat(self):
        reply = input(random.choice(self.random_question)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    
    def match_reply(self, reply):
        for intent, regex_pattern in self.bot_responses.items():
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_feelings_intent':
                return self.describe_feelings_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_mental_health':
                return self.about_mental_health()
        
        if not found_match:
            return self.no_match_intent() 

    def describe_feelings_intent(self):
        responses = ("It's important to acknowledge and express your feelings.\n",
                     "Feelings are valid, no matter what they are.\n")
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = ("Exploring why we feel a certain way can help us understand ourselves better.\n",
                     "Understanding the reasons behind our feelings can lead to positive changes.\n")
        return random.choice(responses)
    
    def about_mental_health(self):
        responses = ("Mental health is a vital aspect of overall well-being.\n",
                     "Taking care of your mental health is just as important as taking care of your physical health.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ( "I'm here to listen. Please feel free to share more.\n",
                      "Tell me more about what's on your mind.\n",
                      "It's okay, you can elaborate further.\n",
                      "I'm interested in hearing more about your thoughts and feelings.\n",
                      "Can you tell me more about that?\n",
                      "Why do you think that is?\n")
        return random.choice(responses)

bot = MentalHealthBot()
bot.greet()
