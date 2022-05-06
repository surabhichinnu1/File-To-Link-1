if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MrMKN/File-To-Link.git /File-To-Link     
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /File-To-Link
fi
cd /File-To-Link
pip3 install -U -r requirements.txt
echo "-----FILE TO LINK BOT IS STARTING-----"
python3 bot.py
