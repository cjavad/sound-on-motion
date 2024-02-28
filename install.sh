#!/bin/bash

# Symlink this directory to /opt/sound-on-motion
ln -s $(pwd) /opt/sound-on-motion

# Install systemd services
cp sound-on-motion-app.service /etc/systemd/system/sound-on-motion-app.service
cp sound-on-motion-act.service /etc/systemd/system/sound-on-motion-act.service

sudo systemctl daemon-reload

# Enable now
sudo systemctl enable --now sound-on-motion-app
sudo systemctl enable --now sound-on-motion-act