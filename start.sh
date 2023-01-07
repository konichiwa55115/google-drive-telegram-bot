echo "Cloning Repo...."
git clone https://github.com/konichiwa55115/google-drive-telegram-bot /LazyDeveloper
cd /LazyDeveloper
pip3 install -r requirements.txt
echo "Starting Bot...."
python -m bot
