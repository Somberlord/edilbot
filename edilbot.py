import discord
from config.botconfig import Config
from perm.perm import Permanence

bot = discord.Bot()
config = Config()


@bot.slash_command()
async def button(ctx: discord.ApplicationContext):
    channel = bot.get_channel(config.perm_channel)
    await channel.send("Coucou")
    await ctx.send_response("Channel créé", ephemeral=True, delete_after=5)


def main():
    bot.add_cog(Permanence(bot, config))
    bot.run(config.client_secret)


@bot.slash_command()
async def test_thread(ctx: discord.ApplicationContext):
    newthread = await ctx.channel.create_thread(name="Test thread", message=None, auto_archive_duration=60,
                                                type=discord.ChannelType.private_thread, reason=None)
    await newthread.send(f"sending <@{ctx.author.id}> to court!")
    await ctx.send_response(f"Thread <#{newthread.id}> créé", ephemeral=True, delete_after=30)


if __name__ == "__main__":
    main()
