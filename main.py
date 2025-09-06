import json
import random
from instagrapi import Client

# ⚠️ अपना SessionID डालें
SESSIONID = "2113474171:MjkkDRRZG4AshZ:29:AYe7sYmuPDJMuu1AKM8p3wdExMKz9Ia1V9mLelGlEg"

# Login
cl = Client()
cl.login_by_sessionid(SESSIONID)
print("✅ Logged in!")

# Target Chat (User या Group ID डालें)
CHAT_ID = "575593458876597"

# JSON फाइल से messages load करना
with open("mafia.json", "r", encoding="utf-8") as f:
    data = json.load(f)

messages = []
for node in data["drawflow"]["nodes"]:
    if "loopData" in node["data"]:
        try:
            loaded = json.loads(node["data"]["loopData"])
            messages.extend(loaded)
        except:
            pass

print(f"✅ Loaded {len(messages)} messages from JSON file.")

# Messages भेजना
for i in range(len(messages)):
    msg = random.choice(messages)
    cl.direct_send(msg, [CHAT_ID])
    print(f"📩 Sent: {msg}")
