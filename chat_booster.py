import requests
import random

WEBHOOK_URL = "https://discord.com/api/webhooks/1483797389356830791/aMqLzNfDaw4I--PR92SF50ki_c0weLamvgs9SLqEYyHCvgFLpKGVBr9Amn3D8d8uov13"

MESSAGES = [
    "How's everyone doing today? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the funniest thing that happened this week? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Favorite color check! Drop yours. ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What game are we grinding tonight? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "If you could travel anywhere right now, where? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Is a hotdog a sandwich? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your go-to snack while gaming? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Best movie you've seen recently? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "PC or Console? Let's settle it. ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the most underrated game? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite season? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Night owl or early bird? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "If you won the lottery, what's the first buy? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Keyboard or Controller? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's a hobby you've always wanted to try? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite animal? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Best music to chill to? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Who is your favorite superhero? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your dream job? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Chocolate or Vanilla? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the scariest game you ever played? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite holiday? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Tea or Coffee? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the best gift you ever got? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "If you were an ice cream flavor, what would you be? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Desktop or Laptop? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite sport? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Marvel or DC? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the last song you listened to? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Do you prefer dogs or cats? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite pizza topping? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Would you rather fly or be invisible? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Favorite movie genre? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "If you could have dinner with any celebrity, who? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite book? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your all time favorite video game? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What show are you currently binging? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the best console ever made? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "If you could live in any game world, which one? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite throwback game? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Fortnite or Warzone? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your highest kill game ever? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Solo or squad? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite map in any game? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What game do you always go back to? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's your favorite anime? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Sub or dub? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What's the best anime arc ever? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "Who's your favorite anime character? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||",
    "What anime needs a season 2? ||@Member @𝙜𝙪𝙚𝙨𝙩 ➕||"
]

def run_booster():
    message = random.choice(MESSAGES)
    payload = {"content": message}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print(f"Successfully sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    run_booster()
