if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/shukurenai007/auto-pro.git /auto-pro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /auto-pro
fi
cd /auto-pro
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
