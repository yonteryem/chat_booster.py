import requests
import random

WEBHOOK_URL = "https://discord.com/api/webhooks/1483797389356830791/aMqLzNfDaw4I--PR92SF50ki_c0weLamvgs9SLqEYyHCvgFLpKGVBr9Amn3D8d8uov13"


   MESSAGES = [
    "How's everyone doing today?",
    "What's the funniest thing that happened this week?",
    "Favorite color check! Drop yours.",
    "What game are we grinding tonight?",
    "If you could travel anywhere right now, where?",
    "Is a hotdog a sandwich?",
    "What's your go-to snack while gaming?",
    "Best movie you've seen recently?",
    "PC or Console? Let's settle it.",
    "What's the most underrated game?",
    "What's your favorite season?",
    "Night owl or early bird?",
    "If you won the lottery, what's the first buy?",
    "Keyboard or Controller?",
    "What's a hobby you've always wanted to try?",
    "What's your favorite animal?",
    "Best music to chill to?",
    "Who is your favorite superhero?",
    "What's your dream job?",
    "Chocolate or Vanilla?",
    "What's the scariest game you ever played?",
    "What's your favorite holiday?",
    "Tea or Coffee?",
    "What's the best gift you ever got?",
    "If you were an ice cream flavor, what would you be?",
    "Desktop or Laptop?",
    "What's your favorite sport?",
    "Marvel or DC?",
    "What's the last song you listened to?",
    "Do you prefer dogs or cats?",
    "What's your favorite pizza topping?",
    "Would you rather fly or be invisible?",
    "Favorite movie genre?",
    "If you could have dinner with any celebrity, who?",
    "What's your favorite book?",
    "What's your all time favorite video game?",
    "What show are you currently binging?",
    "What's the best console ever made?",
    "If you could live in any game world, which one?",
    "What's your favorite throwback game?",
    "Fortnite or Warzone?",
    "What's your highest kill game ever?",
    "Solo or squad?",
    "What's your favorite map in any game?",
    "What game do you always go back to?",
    "What's your favorite anime?",
    "Sub or dub?",
    "What's the best anime arc ever?",
    "Who's your favorite anime character?",
    "What anime needs a season 2?",
    "What's the best map in CS2?",
    "What's your most expensive skin?",
    "Dream knife pull? Go.",
    "What's the best rank you've ever hit?",
    "Clutch or kick?"
]

def run_booster():
    message = random.choice(MESSAGES)
    payload = {"content": message}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_booster()
