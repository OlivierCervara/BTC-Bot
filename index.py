import discord
import requests
import json

# initialisation du client Discord
client = discord.Client(intents=discord.Intents.default())

# URL pour obtenir le prix du bitcoin en dollars
btc_price_usd_url = "https://api.coindesk.com/v1/bpi/currentprice/USD.json"

# URL pour obtenir le prix du bitcoin en euros
btc_price_eur_url = "https://api.coindesk.com/v1/bpi/currentprice/EUR.json"

# Embed template pour le prix du bitcoin
embed_template = discord.Embed(title="Prix actuel du Bitcoin", color=0x00ff00)
embed_template.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/4/46/Bitcoin.svg")

# Lorsque le bot est prêt
@client.event
async def on_ready():
    print("Bot connecté avec succès")

# Lorsqu'un utilisateur envoie la commande !btc
@client.event
async def on_message(message):
    if message.content == "!btc":
        # Obtenir le prix du bitcoin en dollars
        response = requests.get(btc_price_usd_url)
        btc_price_usd = json.loads(response.text)["bpi"]["USD"]["rate_float"]
        
        # Obtenir le prix du bitcoin en euros
        response = requests.get(btc_price_eur_url)
        btc_price_eur = json.loads(response.text)["bpi"]["EUR"]["rate_float"]
        
        # Construire l'embed avec les prix actuels
        embed = embed_template.copy()
        embed.add_field(name="Prix en dollars", value=f"${btc_price_usd:.2f}", inline=False)
        embed.add_field(name="Prix en euros", value=f"€{btc_price_eur:.2f}", inline=False)
        
        # Envoyer l'embed au salon
        await message.channel.send(embed=embed)

# Démarrage du client Discord
client.run("DISCORD_BOT_TOKEN")
