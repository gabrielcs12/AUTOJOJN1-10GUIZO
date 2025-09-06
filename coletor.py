import requests
import time

TOKEN = "MTM5OTIxOTY4ODM1NzIzNjgzNw.GrJe6y.JaJxQPpQTkVVNgtRxfrh4hsk3vIkTcaf2yPHoo"
CANAL_ID = "1412641270274326528"
WEBHOOK_URL = "https://autojoin-free-1-10.onrender.com/webhook"
API_KEY = "key123"

HEADERS = {
    "Authorization": TOKEN,
    "User-Agent": "Mozilla/5.0",
    "X-API-KEY": API_KEY,
}

last_message_id = None
print("⏳ Coletor iniciado...")

while True:
    url = f"https://discord.com/api/v10/channels/{CANAL_ID}/messages?limit=5"
    if last_message_id:
        url += f"&after={last_message_id}"

    try:
        r = requests.get(url, headers=HEADERS)
        if r.status_code == 200:
            messages = r.json()
            if not messages:
                print("ℹ️ Nenhuma mensagem nova encontrada")
            else:
                messages.reverse()
                for msg in messages:
                    content = msg.get("content", "")
                    requests.post(WEBHOOK_URL, json={"content": content}, headers={"X-API-KEY": API_KEY})
                    last_message_id = msg["id"]
                    print("✅ Enviado ao backend:", content)
        else:
            print(f"❌ Erro ao buscar mensagens: {r.status_code} {r.text}")
    except Exception as e:
        print("Erro:", e)

    time.sleep(3)
