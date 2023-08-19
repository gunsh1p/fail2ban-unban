# Fail2Ban Unban

It's a simple telegram bot that can ban or unban some ip on your server with fail2ban

## Installation

```bash
git clone https://github.com/gunsh1p/fail2ban-unban.git
cd fail2ban-unban
python3 -m venv env
./env/bin/pip install aiogram
sudo cp ./fail2ban-unban.service /etc/systemd/system/fail2ban-unban.service
```

I don't recommend you to run service as root, so it's better to create a special user with special permissions for this

## Run

```bash
sudo systemctl enable fail2ban-unban
sudo systemctl start fail2ban-unban
```

Check service's status

```bash
sudo systemctl status fail2ban-unban
```
