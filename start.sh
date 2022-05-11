if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/surabhichinnu1/File-To-Link-1.git /File-To-Link     
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /File-To-Link
fi
cd /File-To-Link
pip3 install -U -r requirements.txt
echo "-----FILE TO LINK BOT IS STARTING-----"
python -m Adarsh
