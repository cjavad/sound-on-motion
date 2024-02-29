#!/bin/bash
# Cleanup old installation
sudo systemctl stop sound-on-motion-app
sudo systemctl stop sound-on-motion-act



rm -f /opt/sound-on-motion
# Symlink this directory to /opt/sound-on-motion
ln -s $(pwd) /opt/sound-on-motion

# Add crontab for /opt/sound-on-motion/tmux.sh if not exists
if ! crontab -l | grep -q '/opt/sound-on-motion/tmux.sh'; then
    (crontab -l ; echo "@reboot /opt/sound-on-motion/tmux.sh") | crontab -
    # Run it every
fi

# Install systemd services
cp sound-on-motion-app.service /etc/systemd/system/sound-on-motion-app.service
sudo systemctl daemon-reload

# Enable now
sudo systemctl enable --now sound-on-motion-app

pipenv install