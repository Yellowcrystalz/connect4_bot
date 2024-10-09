import discord


class QuitButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Quit", style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction):

        if await self.check_in_game(interaction):
            return

        string = (
            f"**{interaction.user.name}** has forfeited\n" +
            f"**{self.view.player1 if interaction.user == self.view.player2 else self.view.player2}** has won!"
        )

        self.view.create_embed(string)
        await self.view.shutdown(interaction)
        await interaction.response.edit_message(embed=self.view.get_embed(), view=self.view)

    async def check_in_game(self, interaction):
        if interaction.user != self.view.player1 and interaction.user != self.view.player2:
            await interaction.response.send_message(
                f"{interaction.user.mention}, you aren't in this game!",
                ephemeral=True
            )
            return True

        return False
