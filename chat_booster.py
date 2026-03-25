import requests
import random

WEBHOOK_URL = "https://discord.com/api/webhooks/1486307521009291304/nSBOOm1FmK3PLxRaJoVYpGzhM0EKFBGP6ds2VP-28YbYHvIrEf-GjYIRmX-D-aIr3ihL"

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
    "Clutch or kick?",
    "What's your most played game on Steam?",
    "If you could have any superpower, what would it be?",
    "What's the best animated movie?",
    "What game are you looking forward to the most?",
    "Describe your favorite game using only emojis.",
    "What's the worst trend in gaming right now?",
    "What's your favorite late-night snack?",
    "If you were stranded on an island, what 3 things would you bring?",
    "What's a movie you can quote from start to finish?",
    "What's your favorite meme format right now?",
    "Do you put milk or cereal first?",
    "What's the best weapon in your favorite game?",
    "What's the most annoying enemy in a video game?",
    "What's your favorite childhood show?",
    "If you could teleport anywhere, where to?",
    "What's the best board game?",
    "What's your favorite quote from a game?",
    "What's a song you have on repeat right now?",
    "What's your favorite console controller design?",
    "What's the scariest movie you've watched?",
    "What's your favorite mobile game?",
    "Have you ever 100% completed a game?",
    "What's the weirdest bug you've found in a game?",
    "What's your favorite skin/cosmetic you own?",
    "If you could be a voice actor for any character, who?",
    "What's the best gaming event/convention?",
    "What's your favorite energy drink?",
    "What's the best game trailer you've ever seen?",
    "What's your favorite easter egg in a game?",
    "Do you prefer physical or digital copies of games?"
]

def run_booster():
    base_message = random.choice(MESSAGES)
    # Formatted with spaces inside the spoiler tags: || @tag1 @tag2 ||
    hidden_tags = " || <@&818718468911136808> <@&617287002089455629> ||"
    
    payload = {"content": base_message + hidden_tags}
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print("Message sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_booster()
