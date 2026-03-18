import requests
import random

# CONFIGURATION
WEBHOOK_URL = "https://discord.com/api/webhooks/1483797389356830791/aMqLzNfDaw4I--PR92SF50ki_c0weLamvgs9SLqEYyHCvgFLpKGVBr9Amn3D8d8uov13"

# 50 Identities
NAMES = ["Shadow", "Nova", "Cipher", "Vortex", "Pixel", "Zenith", "Alpha", "Omega", "Titan", "Neon",
         "Frost", "Blaze", "Echo", "Static", "Logic", "Pulse", "Rift", "Viper", "Bolt", "Apex",
         "Sonic", "Orbit", "Grim", "Flux", "Zero", "Aura", "Koda", "Sync", "Turbo", "Dusk",
         "Dawn", "Zane", "Ryder", "Axel", "Raven", "Skye", "Blitz", "Comet", "Drift", "Edge",
         "Hunter", "Sniper", "Ghost", "Glitch", "Circuit", "Spark", "Thunder", "Aero", "Mist", "Stealth"]

PROFILES = [{"name": f"{n}_{random.randint(10,99)}", "avatar": f"https://i.pravatar.cc/150?u={n}"} for n in NAMES]

# Starters List
STARTERS = [
    "How's everyone doing today? {tag}", "What's the funniest thing that happened this week? {tag}",
    "Favorite color check! Drop yours. {tag}", "What game are we grinding tonight? {tag}",
    "If you could travel anywhere right now, where? {tag}", "Is a hotdog a sandwich? {tag}",
    "What's your go-to snack while gaming? {tag}", "Best movie you've seen recently? {tag}",
    "PC or Console? Let's settle it. {tag}", "What's the most underrated game? {tag}",
    "What's your favorite season? {tag}", "Night owl or early bird? {tag}",
    "If you won the lottery, what's the first buy? {tag}", "Keyboard or Controller? {tag}",
    "What's a hobby you've always wanted to try? {tag}", "What's your favorite animal? {tag}",
    "Best music to chill to? {tag}", "Who is your favorite superhero? {tag}",
    "What's your dream job? {tag}", "Chocolate or Vanilla? {tag}",
    "What's the scariest game you ever played? {tag}", "What's your favorite holiday? {tag}",
    "Tea or Coffee? {tag}", "What's the best gift you ever got? {tag}",
    "If you were an ice cream flavor, what would you be? {tag}", "Desktop or Laptop? {tag}",
    "What's your favorite sport? {tag}", "Marvel or DC? {tag}",
    "What's the last song you listened to? {tag}", "Do you prefer dogs or cats? {tag}",
    "What's your favorite pizza topping? {tag}", "Would you rather fly or be invisible? {tag}",
    "What's the best pizza place? {tag}", "Favorite movie genre? {tag}",
    "If you could have dinner with any celebrity, who? {tag}", "What's your favorite book? {tag}",
         # More starters to add
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
    "What's the best thing about this server? {tag}",
    "Drop your unpopular opinion. {tag}",
    "What's a random fun fact you know? {tag}",
    "What would your last meal be? {tag}"
]

def run_booster():
    profile = random.choice(PROFILES)
    message = random.choice(STARTERS)

    # Random Tags
    roll = random.random()
    if roll < 0.70:
        tag = "@Member"
    elif roll < 0.90:
        tag = "@Member @𝙜𝙪𝙚𝙨𝙩 ➕"
    else:
        tag = "@𝙜𝙪𝙚𝙨𝙩 ➕"

    payload = {
        "username": profile["name"],
        "avatar_url": profile["avatar"],
        "content": message.format(tag=tag),
        "allowed_mentions": {"parse": []}
    }
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    run_booster()
