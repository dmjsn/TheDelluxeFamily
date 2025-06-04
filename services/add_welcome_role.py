class AddWelcomeRole:
    def __init__(self, bot):
        self.bot = bot

    async def addRole(self, member, roleId):
        role = member.guild.get_role(roleId)

        if not role:
            return

        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)
