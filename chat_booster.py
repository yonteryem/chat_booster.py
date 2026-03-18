import requests
import random

# CONFIGURATION
WEBHOOK_URL = "https://discord.com/api/webhooks/1483797389356830791/aMqLzNfDaw4I--PR92SF50ki_c0weLamvgs9SLqEYyHCvgFLpKGVBr9Amn3D8d8uov13"

# Tags
TAG_MEMBER = "@Member"
TAG_GUEST = "@𝙜𝙪𝙚𝙨𝙩 ➕"

# 100 Messages
MESSAGES = [
    "How's everyone doing today? {tag}",
    "What's the funniest thing that happened this week? {tag}",
    "Favorite color check! Drop yours. {tag}",
    "What game are we grinding tonight? {tag}",
    "If you could travel anywhere right now, where? {tag}",
    "Is a hotdog a sandwich? {tag}",
    "What's your go-to snack while gaming? {tag}",
    "Best movie you've seen recently? {tag}",
    "PC or Console? Let's settle it. {tag}",
    "What's the most underrated game? {tag}",
    "What's your favorite season? {tag}",
    "Night owl or early bird? {tag}",
    "If you won the lottery, what's the first buy? {tag}",
    "Keyboard or Controller? {tag}",
    "What's a hobby you've always wanted to try? {tag}",
    "What's your favorite animal? {tag}",
    "Best music to chill to? {tag}",
    "Who is your favorite superhero? {tag}",
    "What's your dream job? {tag}",
    "Chocolate or Vanilla? {tag}",
    "What's the scariest game you ever played? {tag}",
    "What's your favorite holiday? {tag}",
    "Tea or Coffee? {tag}",
    "What's the best gift you ever got? {tag}",
    "If you were an ice cream flavor, what would you be? {tag}",
    "Desktop or Laptop? {tag}",
    "What's your favorite sport? {tag}",
    "Marvel or DC? {tag}",
    "What's the last song you listened to? {tag}",
    "Do you prefer dogs or cats? {tag}",
    "What's your favorite pizza topping? {tag}",
    "Would you rather fly or be invisible? {tag}",
    "Favorite movie genre? {tag}",
    "If you could have dinner with any celebrity, who? {tag}",
    "What's your favorite book? {tag}",
    "What's your all time favorite video game? {tag}",
    "What show are you currently binging? {tag}",
    "What's the best console ever made? {tag}",
    "If you could live in any game world, which one? {tag}",
    "What's your favorite throwback game? {tag}",
    "Fortnite or Warzone? {tag}",
    "What's your highest kill game ever? {tag}",
    "Solo or squad? {tag}",
    "What's your favorite map in any game? {tag}",
    "What game do you always go back to? {tag}",
    "What's your favorite anime? {tag}",
    "Sub or dub? {tag}",
    "What's the best anime arc ever? {tag}",
    "Who's your favorite anime character? {tag}",
    "What anime needs a season 2? {tag}",
    "What's your favorite food? {tag}",
    "Burger or pizza? {tag}",
    "What's the best fast food chain? {tag}",
    "Cook at home or eat out? {tag}",
    "What's your go-to late night snack? {tag}",
    "What's your dream car? {tag}",
    "What country do you want to visit most? {tag}",
    "Beach or mountains? {tag}",
    "City life or countryside? {tag}",
    "What's your favorite weather? {tag}",
    "What's the best sport to watch live? {tag}",
    "Who's your favorite athlete of all time? {tag}",
    "What skill do you wish you had? {tag}",
    "What language do you want to learn? {tag}",
    "What's something you're proud of? {tag}",
    "Morning shower or night shower? {tag}",
    "What's your phone wallpaper right now? {tag}",
    "What app do you use the most? {tag}",
    "Spotify or Apple Music? {tag}",
    "What song is stuck in your head? {tag}",
    "Who's your favorite music artist? {tag}",
    "Concerts or festivals? {tag}",
    "What's the best decade for music? {tag}",
    "What movie could you watch a hundred times? {tag}",
    "What's a movie everyone loves but you hate? {tag}",
    "What's your favorite childhood memory? {tag}",
    "What superpower would you pick? {tag}",
    "Would you rather be rich or famous? {tag}",
    "Time travel: past or future? {tag}",
    "What's something you want to learn this year? {tag}",
    "What's your biggest flex? {tag}",
    "Drop your unpopular opinion. {tag}",
    "What's a random fun fact you know? {tag}",
    "What would your last meal be? {tag}",
    "What's the best thing about this server? {tag}",
    "What emoji describes your mood right now? {tag}",
    "Sneakers or boots? {tag}",
    "What's your go-to comfort show? {tag}",
    "If you could master any instrument, what would it be? {tag}",
    "What's your sleep schedule like? {tag}",
    "What's the weirdest food combo you actually enjoy? {tag}",
    "What's your most used emoji? {tag}",
    "If you had a warning label, what would it say? {tag}",
    "What's your spirit animal? {tag}",
    "What fictional universe would you live in? {tag}",
    "What's the best meme format ever? {tag}",
    "What's your go-to karaoke song? {tag}",
    "What's one thing you can't live without? {tag}",
    "If you could rename yourself, what would you pick? {tag}",
    "What's your biggest gaming achievement? {tag}",
]

def run_booster():
    message = random.choice(MESSAGES)

    roll = random.random()
    if roll < 0.70:
        tag = TAG_MEMBER
    elif roll < 0.90:
        tag = f"{TAG_MEMBER} {TAG_GUEST}"
    else:
        tag = TAG_GUEST

    payload = {
        "content": message.format(tag=tag),
        "allowed_mentions": {"parse": []}
    }
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    run_booster()
