import arrow
from disnake import ApplicationCommandInteraction, Member
from disnake.ext import commands

from client import Client


class User(commands.Cog):
    """A set of commands for interacting with users."""

    @commands.slash_command()
    async def user(self, inter: ApplicationCommandInteraction) -> None:
        """Retrieve information about users."""
        del inter

    @user.sub_command()
    async def id(self, inter: ApplicationCommandInteraction, member: Member = None) -> None:
        """Retrieves a user's account ID. Defaults to your own account."""

        if member is None:
            member = inter.author

        name = member.name.title()
        id = member.id

        if member is inter.author:
            return await inter.send(f"Hello **{name}**, your user ID is _{id}_.")

        await inter.send(f"The user ID for **{name}** is _{id}_.")

    @user.sub_command()
    async def age(self, inter: ApplicationCommandInteraction, member: Member = None) -> None:
        """Retrieves a user's account age. Defaults to your own account."""

        if member is None:
            member = inter.author

        name = member.name

        join_date = arrow.get(member.created_at).format("MMMM D, YYYY")
        humanized_join_date = arrow.get(member.created_at).humanize(granularity=["year", "week", "day"])

        if member is inter.author:
            return await inter.send(f"You joined Discord on {join_date}, or _{humanized_join_date}_.")

        await inter.send(f"**{name}** joined Discord on {join_date}, or _{humanized_join_date}_.")


def setup(client: Client):
    client.add_cog(User(client))
