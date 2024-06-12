### 1. Install Necessary Packages

First, ensure your system is updated and necessary packages are installed.

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install git python3 python3-pip python3-venv screen -y
```

### 2. Clone the Repository

Clone your GitHub repository containing the script.

```bash
git clone https://github.com/0xGery/Malicious.git
cd Malicious/testpy
```

### 3. Set Up Virtual Environment

Create a virtual environment and activate it.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Install the necessary Python packages using `pip`.

```bash
pip install web3 eth-account python-dotenv
```

### 5. Set Up Environment Variables

Create a `.env` file in the same directory as your script and add your private key.

```bash
echo "PRIVATE_KEY=your_private_key_here" > .env
```

Replace `your_private_key_here` with your actual private key.

### 6. Start a `screen` Session

Start a `screen` session to run your script.

```bash
screen -S taiko-bot
```

### 7. Run the Script

Within the `screen` session, run your Python script.

```bash
python taiko.py
```

### 8. Detach from `screen` Session

Detach from the `screen` session without stopping the script.

```bash
Ctrl + A, then D
```

### 9. Reattach to `screen` Session (Optional)

If you want to reattach to the `screen` session later, use:

```bash
screen -r taiko-bot
```
