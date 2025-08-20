import requests, time

token = input("Ton token Discord: ").strip()
guild_id = input("ID du serveur: ").strip()
channels = input("IDs des salons (séparés par des virgules): ").split(",")
channels = [c.strip() for c in channels if c.strip()]
nb = int(input("Combien de messages envoyer: ").strip())
msg = input("Message à envoyer: ").strip()

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

for channel_id in channels:
    print(f"Spam dans salon {channel_id} ...")
    for i in range(nb):
        r = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers=headers,
            json={"content": msg}
        )
        if r.status_code == 200:
            print(f"[OK] Message {i+1}/{nb} envoyé dans {channel_id}")
        else:
            print(f"[FAIL] {r.status_code} -> {r.text}")
        time.sleep(0.5)  # délai pour limiter le rate limit

print("Terminé ✅")
