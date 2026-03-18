import requests
import random
import os

# Fetches the URL from your GitHub Secrets
WEBHOOK_URL = os.getenv("https://discord.com/api/webhooks/1483797389356830791/aMqLzNfDaw4I--PR92SF50ki_c0weLamvgs9SLqEYyHCvgFLpKGVBr9Amn3D8d8uov13")

# Role IDs - REPLACE THESE NUMBERS with your actual Discord Role IDs
# To get them, type \@Member and \@guest in Discord
MEMBER_ID = "123456789012345678" 
GUEST_ID = "876543210987654321"

# 50 Generic Identity Profiles
NAMES = ["Shadow", "Nova", "Cipher", "Vortex", "Pixel", "Zenith", "Alpha", "Omega", "Titan", "Neon", 
         "Frost", "Blaze", "Echo", "Static", "Logic", "Pulse", "Rift", "Viper", "Bolt", "Apex", 
         "Sonic", "Orbit", "Grim", "Flux", "Zero", "Aura", "Koda", "Sync", "Turbo", "Dusk", 
         "Dawn", "Zane", "Ryder", "Axel", "Raven", "Skye", "Blitz", "Comet", "Drift", "Edge"]

PROFILES = [{"name": f"{n}_{random.randint(10,99)}", "avatar": f"https://i.pravatar.cc/150?u={n}"} for n in NAMES]

# Huge List of Conversation Starters
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
    "What's your favorite pizza topping? {tag}", "Would you rather fly or be invisible? {tag}"
]

def run_booster():
    profile = random.choice(PROFILES)
    message = random.choice(STARTERS)
    
    # Tag Logic: 70% Member, 20% Both, 10% Guest
    roll = random.random()
    if roll < 0.70:
        tag = f"<@&{MEMBER_ID}>"
    elif roll < 0.90:
        tag = f"<@&{MEMBER_ID}> <@&{GUEST_ID}>"
    else:
        tag = f"<@&{GUEST_ID}>"

    payload = {
        "username": profile["name"],
        "avatar_url": profile["avatar"],
        "content": message.format(tag=tag),
        "allowed_mentions": {"parse": ["roles"]}
    }

    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    run_booster()
