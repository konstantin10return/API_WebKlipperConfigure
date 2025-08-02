#!/bin/bash

sudo apt-get install python3
sudo apt-get install python3-venv
cd API_WebKlipperConfigure
python3 -m venv ~/wkc-env/venv
chmod +x ~/wkc-env/venv/bin/activate
source ~/wkc-env/venv/bin/activate
pip install -r requrements.txt
chmod +x console_version.sh
deactivate