import requests
import random
import time

# --- CONFIGURATION ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1483797389356830791/aMqLzNfDaw4I--PR92SF50ki_c0weLamvgs9SLqEYyHCvgFLpKGVBr9Amn3D8d8uov13"

# Replace these with the actual ID numbers from your server (e.g., <@&123456789>)
ROLE_GUEST = "@guest"  
ROLE_MEMBER = "@Member"

# 50 Generic Identity Profiles (Names + Static Placeholder Icons)
PROFILES = [
    {"name": "ShadowReaper", "avatar": "https://i.pravatar.cc/150?u=1"},
    {"name": "CyberGhost", "avatar": "https://i.pravatar.cc/150?u=2"},
    {"name": "PixelKnight", "avatar": "https://i.pravatar.cc/150?u=3"},
    {"name": "NovaStorm", "avatar": "https://i.pravatar.cc/150?u=4"},
    {"name": "VoidWalker", "avatar": "https://i.pravatar.cc/150?u=5"},
    {"name": "LunarEcho", "avatar": "https://i.pravatar.cc/150?u=6"},
    {"name": "FrostByte", "avatar": "https://i.pravatar.cc/150?u=7"},
    {"name": "Zenith", "avatar": "https://i.pravatar.cc/150?u=8"},
    {"name": "RogueSignal", "avatar": "https://i.pravatar.cc/150?u=9"},
    {"name": "AlphaOmega", "avatar": "https://i.pravatar.cc/150?u=10"},
    # ... You can copy-paste these and change the 'u=number' to get 50 unique faces
]

# Random Conversation Starters (Categorized for variety)
STARTERS = [
    # General/Icebreakers
    "How's everyone doing today? {tag}",
    "What's the funniest thing that happened to you this week? {tag}",
    "Favorite color check! Drop yours below. {tag}",
    "If you could travel anywhere right now, where would it be? {tag}",
    "What’s the last movie that actually made you laugh out loud? {tag}",
    "What is your go-to comfort food? {tag}",
    "If you won the lottery tomorrow, what's the first thing you're buying? {tag}",
    
    # Gaming/Tech
    "What game are we grinding tonight? {tag}",
    "Mouse or Controller? Let's settle this. {tag}",
    "What's the most overrated game in your opinion? {tag}",
    "Show us your setups! {tag}",
    "Best gaming memory from when you were a kid? {tag}",
    "What's the hardest boss fight you've ever beaten? {tag}",
    "If you could live in any video game world, which one? {tag}",
    
    # Random/Fun
    "Is a hotdog a sandwich? Debate starts now. {tag}",
    "What's your most controversial food opinion? {tag}",
    "If you were a superhero, what would your name be? {tag}",
    "Would you rather always be 10 minutes late or 20 minutes early? {tag}",
    "What's a skill you've always wanted to learn? {tag}",
    "What’s the best piece of advice you’ve ever received? {tag}",
    "Pineapple on pizza: Yes or No? {tag}"
]

def get_random_tag():
    """Logic to randomize tags: Mostly Member, sometimes Guest, sometimes both."""
    choice = random.choice(["member", "member", "member", "guest", "both"])
    if choice == "member":
        return ROLE_MEMBER
    elif choice == "guest":
        return ROLE_GUEST
    else:
        return f"{ROLE_MEMBER} & {ROLE_GUEST}"

def post_to_webhook():
    profile = random.choice(PROFILES)
    question = random.choice(STARTERS)
    tag = get_random_tag()

    payload = {
        "username": profile["name"],
        "avatar_url": profile["avatar"],
        "content": question.format(tag=tag),
        "allowed_mentions": {"parse": ["roles", "everyone"]}
    }

    try:
        r = requests.post(WEBHOOK_URL, json=payload)
        if r.status_code == 204:
            print(f"Posted as {profile['name']} tagging {tag}")
        else:
            print(f"Error: {r.status_code}")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    # Adjust interval (e.g., 1800 seconds for every 30 mins)
    while True:
        post_to_webhook()
        interval = random.randint(1200, 3600) # Randomizes timing so it looks more natural
        time.sleep(interval)
