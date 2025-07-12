sudo apt-get install python3
sudo apt-get install python3-venv
cd API_WebKlipperConfigure
python3 -m venv venv
chmod +x ./venv/bin/activate
source ./venv/bin/activate
pip install -r requrements.txt
chmod +x console_version.py
deactivate
