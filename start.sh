if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/shukurenai007/Auto-pro.git /Auto-pro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-pro
fi
cd /Auto-pro

pip3 install -U -r requirements.txt

echo "Starting Bot...."

python3 bot.py
