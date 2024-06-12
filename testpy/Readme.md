## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup Instructions

### Step 1: Update and Upgrade the System


```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Python and pip

```bash
sudo apt install python3 python3-pip -y
```

### Step 3: Install virtualenv

```bash
pip3 install virtualenv
```

### Step 4: Clone the Repository

```bash
git clone https://github.com/0xGery/Malicious/blob/main/testpy.git
cd testpy
```

### Step 5: Set Up the Virtual Environment

```bash
virtualenv venv
source venv/bin/activate
```

### Step 6: Install Required Python Packages

```bash
pip install -r requirements.txt
```

### Step 7: Create a `.env` File

Create a `.env` file in the project root directory and add your private key:

```plaintext
PRIVATE_KEY=your_private_key_here
```

### Step 8: Install `screen`

```bash
sudo apt install screen -y
```

### Step 9: Run the Script Inside a `screen` Session

1. Start a new `screen` session:

    ```bash
    screen -S taiko-tx
    ```

2. Run the script:

    ```bash
    python taiko.py
    ```

3. To detach from the `screen` session and leave the script running:

    ```bash
    Ctrl + A, then D
    ```

4. To reattach to the `screen` session later:

    ```bash
    screen -r taiko-tx
    ```

### Script Overview

The script will run continuously, sending up to 5 transactions per day and resetting at 1 AM UTC.

## Troubleshooting

If you encounter any issues, check the following:

1. Ensure you have correctly set up your `.env` file with the proper private key.
2. Verify that you have sufficient funds in your wallet.
3. Make sure the script has the necessary permissions to execute.

Feel free to contribute or raise issues on the repository if you find any bugs or have suggestions for improvements.
