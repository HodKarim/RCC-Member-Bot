RCC Membership Bot

A Discord bot for the Responsible Computing Club that automates Active Member role assignments based on event attendance.

Features  ݁₊ ⊹ . ݁˖ . ݁·ꕤ

Connects to Google Sheets attendance data (from Google Form responses).

Checks whether members have attended at least 1 social event and 1 professional event.

Automatically assigns or removes the “Active Member” role in Discord.

Reduces manual work for the Secretary and ensures accurate membership tracking.

Tech Stack  ݁₊ ⊹ . ݁˖ . ݁·ꕤ

Python 3.11+

discord.py
 – Discord API wrapper

gspread
 – Google Sheets API client

Google Cloud Service Account for secure authentication

Setup  ݁₊ ⊹ . ݁˖ . ݁·ꕤ

Clone the repository:

git clone https://github.com/yourusername/rcc-membership-bot.git
cd rcc-membership-bot


Install dependencies:

pip install -r requirements.txt


Create a Google Cloud Service Account and download credentials.json.

Share your attendance response sheets with the service account email.

Add your Discord Bot Token to the code.

Run the bot:

python main.py

Future Improvements  ݁₊ ⊹ . ݁˖ . ݁·ꕤ

Match members by Student ID instead of nickname for reliability.

Deploy to Google Cloud Run / AWS / Heroku for 24/7 hosting.

Add command (!update_roles) to refresh roles without restarting the bot.

Add real-time updates via Google Apps Script webhooks.

License  ݁₊ ⊹ . ݁˖ . ݁·ꕤ

MIT License
