> [!NOTE]  
> [Click here for the Portuguese version.](https://github.com/JleoDev/AFSBot/blob/main/README_PTBR.md)

<h1 align="center">Advanced File Stream Bot (AFSBot)</h1>  
AFSBot is a continuation of the project <a href='https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python'>TG-FileStreamBot</a>, specifically the Python version by user <a href='https://github.com/EverythingSuckz'>EverythingSuckz</a>, where I will modify and add functions to the bot while maintaining its core purpose of creating streaming links for files.

## How to Set Up

<details open="open">  
	<summary><h3>Environment Variables</h3></summary>  

Create an <em>.env</em> file like the example below:

```
API_ID=452525
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=55838383:yourtbottokenhere
BIN_CHANNEL=-100
```

<details>  
	<summary><h4>Required</h4></summary>  

For the bot to work, it requires at least these four variables:

- `API_ID`: This is the Telegram API ID linked to your account. Note: This ID can be obtained by accessing <a href='https://my.telegram.org/auth'>https://my.telegram.org/auth</a>

- `API_HASH`: This is the Telegram API hash linked to your account. Note: This hash can be obtained by accessing <a href='https://my.telegram.org/auth'>https://my.telegram.org/auth</a>

- `BOT_TOKEN`: This is the token for your bot. Note: This token can be obtained by chatting with <a href='https://t.me/BotFather'>@BotFather</a>

- `BIN_CHANNEL`: This is the ID of the channel or group that will be used to store messages with files that the bot receives. Note: This ID can be obtained by forwarding a message from the channel to <a href='https://t.me/MissRose_bot'>@missrose_bot</a> and then replying to the message with the command /id.

> **Warning**  
> Don't forget to add the bot to `BIN_CHANNEL` for proper functioning.

</details>

<details>  
	<summary><h4>Optional</h4></summary>  

- `ALLOWED_USERS`: These are the Telegram user IDs to which the bot should respond.

> **Note**  
> Leave this field empty to allow anyone to use the bot. Note: You can also add multiple users by separating their IDs with a comma (,).

- `HASH_LENGTH`: This is the custom length for generated URL hashes. The hash length must be greater than 5 and less than 64.

- `SLEEP_THRESHOLD`: Sets the wait limit for flood wait exceptions that occur globally on the bot instance. Requests that generate flood wait exceptions below this limit will automatically retry after the required wait time. Exceptions requiring longer wait times will be displayed in the terminal. The default value is 60 seconds. It is recommended to leave this field empty.

- `WORKERS`: Sets the maximum number of concurrent workers to handle received updates. The default value is 3.

- `PORT`: Sets the port your web application will receive requests on. The default is 8080.

- `WEB_SERVER_BIND_ADDRESS`: Sets the server bind address. The default is 0.0.0.0.

- `NO_PORT`: Can be `True` or `False`. If set to `True`, the port will not be displayed.
> **Note**  
> To use this setting, set `PORT` to 80 for HTTP protocol or 443 for HTTPS protocol for the generated links to work.

- `FQDN`: A Fully Qualified Domain Name, if present. The default is `WEB_SERVER_BIND_ADDRESS`.

- `HAS_SSL`: Can be `True` or `False`. If set to `True`, the generated links will be in HTTPS format.

- `KEEP_ALIVE`: If you want the server to ping itself automatically every `PING_INTERVAL` seconds to prevent inactivity. Useful in free PaaS tiers. The default is `False`.

- `PING_INTERVAL`: The time in ms for the server to ping itself each time to prevent inactivity (if on a PaaS). The default is `1200`, or 20 minutes.

- `USE_SESSION_FILE`: Uses session files for clients, rather than storing the Pyrogram SQLite database in memory.

</details>

<details>  
	<summary><h5>Multi-Client Support</h5></summary>  

> **Note**  
> What is the multi-client feature and what does it do? <br>  
> This feature shares Telegram API requests between other bots to avoid flood wait (a type of rate limiting applied by Telegram to prevent server overload) and to enable the server to handle more requests. <br>  

To enable multi-client, generate new bot tokens and add them as environment variables with the following key names.

`MULTI_TOKEN1`: Add your first bot token here.  

`MULTI_TOKEN2`: Add your second bot token here.  

You may also add as many bots as you like. (The maximum limit has not yet been tested)  
`MULTI_TOKEN3`, `MULTI_TOKEN4`, etc.

> **Warning**  
> Don't forget to add all these bots to `BIN_CHANNEL` for proper functioning.

</details>

</details>

<details>  
	<summary><h3>Host it on VPS or Locally</h3></summary>  

```
git clone https://github.com/JleoDev/AFSBot.git
cd AFSBot
python3 -m venv ./venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m WebStreamer
```

and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

</details>

## How to Use the Bot  

> **Warning**  
> Before using the bot, don't forget to add all bots (including multi-client) as admins in `BIN_CHANNEL`.

`/start`: To check if the bot is active.

To get an instant streaming link, simply forward any media to the bot, and it will instantly reply with a direct link to that media message on Telegram.

## Contribution  

Feel free to contribute to this project if you have more ideas. You can create an issue to inform what you want or what you are modifying.

## Credits  

- [Me](https://github.com/JleoDev) as the organizer of AFSBot.  
- [EverythingSuckz](https://github.com/EverythingSuckz) for the [base code](https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python) for the current project.  
- [BlackStone](https://github.com/eyMarv) for adding multi-client support to the [base code](https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python) for the current project.  
- [TheHamkerCat](https://github.com/TheHamkerCat)
- [Dan](https://github.com/delivrance) for the libraries [pyrogram](https://github.com/pyrogram/pyrogram) and [tgcrypto](https://github.com/pyrogram/tgcrypto)
- [Saurabh Kumar](https://github.com/theskumar) for the library [python-dotenv](https://github.com/theskumar/python-dotenv)
- [aio-libs](https://github.com/aio-libs) by library [aiohttp](https://github.com/aio-libs/aiohttp)

> **Note**  
> A copy of the licenses for the codes used in this project can also be found in the licenses folder of this repository.

## License  

Copyright (C) 2024 [JleoDev](https://github.com/JleoDev) under the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html).

AFSBot is Free Software: you can use, study, share, and improve it at your will. Specifically, you can redistribute and/or modify it under the terms of the [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html), as published by the Free Software Foundation, either version 3 of the License or (at your option) any later version.