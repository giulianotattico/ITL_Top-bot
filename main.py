import discord


# la variabile intents contiene i permessi al bot

intents = discord.Intents.default()



# abilita il permesso a leggere i contenuti dei messaggi
discord.Intents.message_content = True


# crea un bot e passa gli indents

client = discord.Client(intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        print(f"Abbiamo fatto l'accesso come {client.user}")

    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()

            # this also works
            await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)

    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)




client = MyClient(intents=intents)
client.run('MTIyMTM5OTQwNzE1NzU3NTc2MQ.GthGV4.9cyVdNXs-LD3i761rnDc7MZt_OXcubx4gd0jK4')
