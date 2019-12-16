#we made thisrth
#tiger said copy the code from the documentation so we can test that all of our shit won't break

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        channel = discord.utils.get(self.get_all_channels(), guild__name='Libretine', name='commands')
        role = discord.utils.get(message.guild.roles, name='Pepe')
        if message.channel == channel and message.content == '$pepe':
            print('is a symbol of freedom')
            await message.author.add_roles(role)
            await message.channel.send('{} was successfully added to {}'.format(role.name, message.author.display_name))
        

client = MyClient()
client.run('')