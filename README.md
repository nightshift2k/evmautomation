# 🦾 EVMAutomation 🦾 - a command line tool performing automated tasks on smart contracts

In DeFi there is constant pressure to perform different tasks, like compound, hydrate, roll, etc.

This tool was written to enable automation of those tasks to ensure you don't have to do it manually ;-)

It was build to support EVM based blockchains but works currently with 4 contracts on the Binance Smart chain.

As it is build in a modular way, one can expand it quite easily to other projects or even other EVM-based chains.

Currently supported projects are:

- DRIP Faucet - Hydrating & Claiming
- DRIP Garden - Planting Seeds
- TRUNK Native Staking - Rolling (reinvesting)
- TRUNK Stampede - Rolling (reinvesting)

## 🔒 Disclaimer on Security and Encryption

This code was specifically written to be as secure as possible, since signing transactions requires the use of a wallet's private key. It's imparative you use the encryption outlined in the code to best protect yourself in the event your computer is ever compomised. 

For every contract you will need to save 1-n wallets via the build in encryption function. 

The workflow is simple:
1. create a wallet.csv file with wallet_address;private_key - one per line
2. use the build in encryption to encrypt the wallet with an encryption key
3. write down or store this encryption key (per project)
4. IMPORTANT: delete the source.csv file

The tool will display an encryption code (AES-128) which is used to encrypt the wallet address and the private key. Every time you start the tool, you will need to enter the encryption key per contract. So currently if you are in DRIP, GARDEN and STAMPEDE you'll need to enter 3 keys which you have previously noted down.

## ℹ️ Installation

### Prerequisies

- Preferrably run this on Linux or MacOS, yes Windows can and probably will work but is not tested
- Install Python 3.8 or 3.9 - refer to Google, there are gazillions of docs for that most *nix systems comes with preinstalled packages
- Install the Package Installer for Python, again most distros come with preinstalled, refer to the [official installation documentation](https://pip.pypa.io/en/stable/installation/)

### Download code from repository

The code is open-source and hostet on `github.com` so you need to checkout the sources:

```bash
# Download the current code of EMVAutomation
git clone https://github.com/nightshift2k/evmautomation.git

# Enter downloaded directory
cd evmautomation
```
### Setup Python virtual environment (virtualenv)

You should run evmautomation in a separated `virtual environment` this is optional but highly recommended.

```bash
# create virtualenv in directory /freqtrade/.env
python3 -m venv .env

# run virtualenv
source .env/bin/activate
```

### Install the package and its dependencies

```bash
python3 -m pip install --upgrade pip # upgrades pip 
python3 -m pip install -e . # installs the package and its dependencies
```

### Done

You can use the tool by entering `evma` on the commandline, the output should look like this:

```
vscode ➜ /workspaces/evmautomation $ evma
usage: evma [-h] [-c CONFIG] [-r] [-e INFILE OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        path to the config file
  -r, --run             Run evm automation workflows configured in config.yaml or custom config file (specify with -c)
  -e INFILE OUTFILE, --encrypt INFILE OUTFILE
                        encrypts infile.csv to outfile.json and displays the encryption key
```

## ⚙️ Configuration

The configuration consists of two steps:
1. encrypt wallets and private keys
2. configure via `config.yaml` or any alternate config file that can be specified via `--config`

###  💬 Setting up a Telegram Bot

EVMAutomation can notify you about everything it does via Telegram.

Below we explain how to create your Telegram Bot, and how to get your Telegram user id.

#### 1. Create your Telegram bot

Start a chat with the [Telegram BotFather](https://telegram.me/BotFather)

Send the message `/newbot`.

*BotFather response:*

> Alright, a new bot. How are we going to call it? Please choose a name for your bot.

Choose the public name of your bot (e.x. `evmautomation bot`)

*BotFather response:*

> Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

Choose the name id of your bot and send it to the BotFather (e.g. "`my_own_evmautomation_bot`")

*BotFather response:*

> Done! Congratulations on your new bot. You will find it at `t.me/yourbots_name_bot`. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

> Use this token to access the HTTP API: `22222222:APITOKEN`

> For a description of the Bot API, see this page: https://core.telegram.org/bots/api Father bot will return you the token (API key)

Copy the API Token (`22222222:APITOKEN` in the above example) and keep use it for the config parameter `telegram.bot_token`.

Don't forget to start the conversation with your bot, by clicking `/START` button

#### 2. Get your Telegram user_id

Talk to the [userinfobot](https://telegram.me/userinfobot)

Get your "Id", you will use it for the config parameter `telegram.chat_id`.

#### 3. Save the data to your `config.yaml`

Edit your `config.yaml` or `config-yourcustomname.yaml` (in case you have multiple custom configs) and save the data you have retrieved from Telegram to the telegram section of the config.

```yaml
telegram: 
    disabled: false
    bot_token: 22222222:APITOKEN
    chat_id: 12345678
```

You will retrieve notifications from now on, if some workflow action happens or errors occur.

### Encrypting wallets

The tool uses the `cryptography.fernet` module and encrypts wallets with an AES-128 key.

To encrypt the wallets:
- create a `wallets-projectname.csv`, e.g. `wallets-drip.csv`
- run `evma -e wallets-projectname.csv wallets-projectsname.json`
- store the shown key in a password manager or write it down
- delete `wallets-projectname.csv`

Remember, when running the automation the tool will ask you for that encryption key again. If you lose it, you'll need to reencrypt the files over again.

Repeat this for every project (e.g. DRIP, GARDEN, STAMPEDE)

### create/adjust config.yaml

The parameters are all described in the `config.yaml.example`, the simplest way is to copy this file to `config.yaml` and adjust.

## 🏃 Running

The goal is to run the tool in unattended mode and recieve notifications via telegram (if enabled) or periodically checking the log file.

To do so without being connected to your linux machine via console or ssh, its advised to use a terminal multiplexer like `screen`.

A very good explanation how to use screen for such an use case can be found [here](https://linuxize.com/post/how-to-use-linux-screen/)

## 🐞 Bug / Feature Request

If you find a bug, kindly open an issue [here](https://github.com/nightshift2k/evmautomation/issues/new) by including a **logfile** and a **meaningful description** of the problem.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nightshift2k/evmautomation/issues/new). 

## 💻 Development
Want to contribute? **Great!🥳**

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

## ⚠️ License

`evmautomation` is free and open-source software licensed under the [MIT License](https://github.com/nightshift2k/evmautomation/blob/main/LICENSE). 

By submitting a pull request to this project, you agree to license your contribution under the MIT license to this project.