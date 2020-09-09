import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()
players = list()


def randomize_teams():
    random.shuffle(players)
    split = len(players) // 2

    return (
        f'Team Alpha: {players[:split]}\n'
        f'Team Bravo: {players[split:]}'
    )


def randomize_map():
    maps = ["Altar of Flame", "Distant Shore", "Emperor's Respite",
            "Endless Vale", "Eternity", "Javelin-4",
            "Legion's Gulch", "Midtown", "Retribution",
            "The Dead Cliffs", "The Fortress", "Vostok",
            "Pacifica", "Radiant Cliffs", "Wormhaven",
            "The Burnout", "Solitude", "Meltdown",
            "Bannerfall", "Convergence", "Equinox",
            "Firebase Echo", "The Citadel", "Gambler's Ruin",
            "Fragment", "Twilight Gap", "Widow's Court",
            "Rusted Lands", "The Anomaly", "Exodus Blue",
            "The Cauldron"]
    return f'Map: {random.choice(maps)}'


def add_players(new_players):
    new_players = new_players.split()
    for new_player in new_players:
        players.append(new_player)
    return f'Added {new_players}!'


def remove_players(old_players):
    old_players = old_players.split()
    for old_player in old_players:
        players.remove(old_player)
    return f'Removed {old_players}!'


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} is connected to {guild.name}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!ra':
        response = (
            f'{randomize_teams()}\n'
            f'{randomize_map()}'
        )

    elif message.content == '!rt':
        response = randomize_teams()

    elif message.content == '!rm':
        response = randomize_map()

    elif message.content.startswith('!ap '):
        response = add_players(message.content[4:])

    elif message.content.startswith('!rp '):
        response = remove_players(message.content[4:])

    elif message.content == '!lp':
        response = f'Players: {players}'

    elif message.content == '!reset':
        players.clear()
        response = 'Removed all players!'

    elif message.content == '!randomrumble':
        response = (
            f'Randomize all = "!ra"\n'
            f'Randomize teams = "!rt"\n'
            f'Randomize map = "!rm"\n'
            f'Add players = "!ap <player> <player> <player>..."\n'
            f'Remove players = "!rp <player> <player> <player>..."\n'
            f'Show players = "!lp"\n'
            f'Reset players = "!reset"'
        )

    else:
        return
    await message.channel.send(response)

client.run(TOKEN)
