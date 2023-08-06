## Telegram-Bot-GPT

A simple interface for OpenAI ChatGPT ver 3.5 using Telegram bots.

**DISCLAIMER**

This open-source module is only intended to provide an interface between bot and AI on top of the following services:
- Bot provided for free by Telegram FZ-LLC
- GPT AI capabilities as paid services from OpenAI LP

The creator of this library is _not in any way responsible_ for any misuse of the module, including but not limited to _any costs that may occur_ due to calls to the GPT AI.

Using this library states that you are agree with this disclaimer.

---

**Installation**
```
pip install telegram-bot-gpt
```

**Usage**
```
import bot_gpt as bot

mybot = bot.Engine("<YOUR_TELEGRAM_TOKEN>")
mybot.set_openai_key("<YOUR_OPENAI_KEY>")

mybot.run()     # currently only polling methode is provided
```

**That's it!!**

---

## What's new?

- Using cipher mechanism for storing memory
- Database is kept in compact form as the default

---

## Dev Functions

- Settings

  The variable `bot.DEFAULT_SETTING` contains a dict of the initial values of accessible configurations:

  ```
  {
    "memory_length": 3,        # the number of previous lines involved
    "max_token": 500,          # for prompt and response for each line
    "ai_temperature": 85,      # 0.75 in the API input
    "bot_active": 1,           # 0 is deactivated
    "daily_limit": 50,         # usage limit for each day, server time
    "admin_limit": 50,         # usage limit for each day, server time
    "password": ""             # will be set automatically by the bot
  }
  ```
  
  There are multiple ways available to access those variables:

  1. `mybot.set_max_token(300)` using the provided function 
  2. `mybot.set("max_token", 300)` save directly to database
  3. `mybot.reset_max_token()` reset to default
  4. `current_max_token = mybot.get("max_token")` to obtain the value
  5. `mybot.reset_settings()` resetting all values to the default

  Albeit mostly giving identical effect, the command shown in (1) and (3) are safer than (2) due to an additional checking mechanism.
  <br><br>


- Bot name
  ```
  mybot.set_botname("My Bot")
  mybot.reset_botname()        # default is "Bot-GPT"
  ```
  <br>

- OpenAI key
  ```
  mybot.set_openai_key("<YOUR_OPENAI_KEY>")
  mybot.del_openai_key()       # AI capabilities will be deactivated
  ```
  <br>

- Memory length, only used when the input is short
  ```
  mybot.set_memory_length(5)   # more value leads to a more expensive cost
  mybot.reset_memory_length()  # default is 3
  memory_length = mybot.get_memory_length()
  ```

---

## Bot Usage

- Admin<br>
  The first user is automatically set as the bot admin which is equipped with a list of commands such as password regulations and bot activations.
  <br><br>

- Password<br>
  New users should enter a randomized code (password) created by the bot which can only be accessed by admin with these commands:

  - `/get_password` displays the current password
  - `/new_passowrd` changes the password without affecting current users
  - `/reset_password` force all users to enter the new password to continue using the bot
  <br><br>

- Deactivation<br>
  The default setting for bot is **active**, whereas only admin has the right to modify it.
  - `/deactivate_bot` bot is off for all users, while **admin still can use it**
  - `/activate_bot` reactivates the bot for all users

  All users can check the bot status using `/is_bot_active`.


---

## How To Get

**Telegram Bot**<br>
Open Telegram app, chat with [@BotFather](https://t.me/BotFather) and send the command /newbot.

**OpenAI key**<br>
Login to [OpenAI](https://platform.openai.com/account/api-keys) and follow the instructions there.
