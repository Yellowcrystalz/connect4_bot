import discord

class BoardButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=str(label), style=discord.ButtonStyle.grey)
    
    async def callback(self, interaction: discord.Interaction):
        if await self.view.check_turn(interaction):
            return

        self.view.place(int(self.label), 'X' if self.view.turn % 2 == 1 else 'O')
        self.view.turn += 1

        if not self.view.valid_move(int(self.label)):
            self.view.remove_item(self)

        embedded_msg = discord.Embed(title="Yellow's Connect 4", color=discord.Color.yellow())
        embedded_msg.add_field(name="", value=self.view.to_string())
        await interaction.response.edit_message(embed=embedded_msg, view=self.view)