import discord

# Definir intents, incluindo membros
intents = discord.Intents.default()
intents.members = True  # Habilita o rastreamento de membros

# Criar a classe do bot com os intents
client = discord.Client(intents=intents)

# Evento quando o bot está pronto
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Evento quando um novo membro entra no servidor
@client.event
async def on_member_join(member):
    # Enviar uma mensagem no privado para o novo membro
    try:
        await member.send(f'Bom dia, {member.name}! Seja bem-vindo ao servidor! 😊')
    except discord.Forbidden:
        print(f"Não foi possível enviar DM para {member.name}.")

# Iniciar o bot
client.run('seu-token-real-aqui')
