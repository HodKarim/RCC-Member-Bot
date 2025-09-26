
import discord
import gspread
from discord.utils import get

# google Sheets setup 
gc = gspread.service_account(filename='credentials.json')

print("Sheets I can access:")
for sheet in gc.openall():
    print(" -", sheet.title)

def find_sheet(keyword):
    """Find the first spreadsheet with keyword in the title (case-insensitive)."""
    for sheet in gc.openall():
        if keyword.lower() in sheet.title.lower():
            print(f"Found sheet: {sheet.title} !!")
            return sheet.sheet1
    raise ValueError(f" (!! No spreadsheet found with keyword: {keyword}")

# open the sheets by keywords
social_sheet = find_sheet("social")
nonsocial_sheet = find_sheet("non-social")

# collect names from both sheets
social_records = social_sheet.get_all_records()
nonsocial_records = nonsocial_sheet.get_all_records()

# ensuring headers match sheet
social_names = {row['Name:'].strip().lower() for row in social_records if row['Name:']}
nonsocial_names = {row['Name:'].strip().lower() for row in nonsocial_records if row['Name:']}

active_names = social_names & nonsocial_names
print("Active Members (by name):", active_names)

# discord bot setup
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} !')
    guild = client.get_guild('ommiting for safety')
    role = get(guild.roles, name="Active Member")

    if not role:
        print("!! 'Active Member' role not found in this server.")
        return

    for member in guild.members:
        member_name = member.display_name.strip().lower()
        if member_name in active_names:
            if role not in member.roles:
                await member.add_roles(role)
                print(f"Added role to {member.display_name}")
        else:
            if role in member.roles:
                await member.remove_roles(role)
                print(f"!! Removed role from {member.display_name}")


token = "ommiting for safety!!!!"
client.run(token)

