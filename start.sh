echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/shukurenai007/auto-pro.git /auto-pro
cd /auto-pro
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
