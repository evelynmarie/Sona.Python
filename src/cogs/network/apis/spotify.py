import disnake
from disnake import ApplicationCommandInteraction, Member
from disnake.ext import commands

from client import Client


class Spotify(commands.Cog):
    """A set of commands for interacting with Spotify."""

    @commands.slash_command()
    async def spotify(self, interaction: ApplicationCommandInteraction):
        """Provides access to retrieving data from the Spotify API."""
        pass

    @spotify.sub_command()
    async def status(self, interaction: ApplicationCommandInteraction, member: Member = None) -> None:
        """Retrieves a given user's Spotify status. Defaults to your own."""

        if interaction.guild_id is None:
            # due to the way discord activities work, they cannot be accessed from direct
            # messages for some reason, so disallow the command from being used in guilds
            # to avoid it breaking.
            return await interaction.response.send_message("This command cannot be used from DMs.")

        if member is None:
            member = interaction.author
        elif member.bot:
            return await interaction.response.send_message("Bots can't listen to music, silly.")

        name = member.name.title()
        activity = member.activity

        if isinstance(activity, disnake.Spotify):
            title = activity.title
            artist = activity.artist
            album = activity.album

            if member is interaction.author:
                message = f"You are currently listening to **{title}** by **{artist}** on **{album}**."
            else:
                message = f"**{name}** is currently listening to **{title}** by **{artist}** on **{album}**."

            return await interaction.response.send_message(message)

        if member is interaction.author:
            return await interaction.response.send_message("You aren't currently istening to anything.")

        await interaction.response.send_message(f"**{name}** isn't currently listening to anything.")
        pass


def setup(client: Client):
    client.add_cog(Spotify(client))
    pass