# FriendTech Toolkit (friendtech-toolkit-py)

The FriendTech Toolkit (friendtech-toolkit-py) is a Python command line interface (CLI) designed to automate the process of searching for new FriendTech accounts based on their Twitter username and purchasing shares as soon as they become available.

## Features

- **Automated Account Search:** Provide a Twitter username and the toolkit will monitor FriendTech for the corresponding account.
- **Automated Share Purchase:** Optionally enable the toolkit to purchase shares in new accounts as they are discovered.
- **Multi-Factor Authentication (MFA):** Handles MFA to secure your FriendTech sessions.
- **Wallet Key Retrieval:** Automated retrieval of your FriendTech wallet key for transactions.
- **Bulk Sell Keys:** Automated Bulk Sale of All Account Keys.

## Getting Started

1. **Installation:**
   - Ensure you have Python 3.7 or above installed on your machine.
   - Clone this repository to your local machine.

```bash
git clone https://github.com/your-repo/friendtech-toolkit-py.git
cd friendtech-toolkit-py
```

## Setup:

```bash
pip install -r requirements.txt
```

## Running the Hunter

This program is designed to run get your account details for you. It will store those values locally on your computer for later use.

If you set enable*buy to \_True* this script will look for your private key. If it is not present, it will attempt to extract it from an automated browser session.

DO NOT INTERACT WITH THE BROWSER SESSION! (The script will have to be re-run if you do.) When prompted, enter your MFA code into the Python terminal ONLY.

```
    python friend_sniper.py save_account_data <phone_number> <ft_wallet_addr> --enable_buy=True
    ex: python friend_sniper.py save_account_data 5551235555 0xWALLETADDRESS018923 --enable_buy=True
```

_You have the option to input your private key manually if you do not want to have it automatically get the keys from a browser session._

### Just searching

```
    python friend_sniper.py hunt_account <phone_number> <ft_wallet_addr> --enable_buy=False
```

### Searching + Buying

```
    python friend_sniper.py hunt_account <phone_number> <ft_wallet_addr> --enable_buy=True
```

### Searching + Buying + Telegram Posting

```
    python friend_sniper.py hunt_account <phone_number> <ft_wallet_addr> --enable_buy=True --bot_father_token="BOT_TOKEN" -channel_name="@FT_ALERTS"
```

### Searching + Buying Multiple Keys

```
    python friend_sniper.py hunt_account <phone_number> <ft_wallet_addr> --enable_buy=True --keys2buy=5
```

### Searching + Buying TURBO EDITION: \*Note will cost slightly more during the purchase for speed

I haven't run into rate limits YET, but I suspect they may show up over time.

```
    python friend_sniper.py hunt_account <phone_number> <ft_wallet_addr> --enable_buy=True --top_of_block=True --check_interval=0.3 --keys2buy=3
```

## Rate Limiting Notice

Be aware that more than 5 MFA attempts within an hour will trigger a rate limit, blocking further attempts for 1 hour.

## Troubleshooting

Refer to the log files for detailed information if you encounter any issues while using the toolkit. Or DM on Twitter @Leyens_OS

## Contributing

To contribute to this project, please fork the repository, make your changes, and submit a pull request.

## Disclaimer

This CLI is a tool for interacting with the FriendTech platform and is not affiliated with FriendTech. Users are responsible for understanding and complying with FriendTech's terms of service while using this script.
