#!/bin/bash
source ~/.bashrc

# Check if ALSA 'default' device is available
if ! aplay -l | grep -q 'card 0'; then
    echo "Error: No sound card detected. Exiting."
    aplay -l
    exit 1
fi

# Start tmux server if not already running
if command -v tmux &> /dev/null && [ -n "$PS1" ] && [[ ! "$TERM" =~ screen ]] && [[ ! "$TERM" =~ tmux ]] && [ -z "$TMUX" ]; then
  exec tmux
fi

if tmux has-session -t auto-session > /dev/null 2>&1; then
    :
else
    tmux new-session -d -s auto-session -n foo bar
    tmux new-window -d -t auto-session /opt/sound-on-motion/start.sh
fi
