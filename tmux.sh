#!/bin/bash
source ~/.bashrc

# Check if ALSA 'default' device is available
if ! aplay -l | grep -q 'card 0'; then
    echo "Error: No sound card detected. Exiting."
    aplay -l
    exit 1
fi

ensure_tmux_session() {
    # echo $1 $2 $3
    # https://unix.stackexchange.com/questions/443569/start-tmux-and-execute-a-set-of-commands-on-boot
    if tmux has-session -t $1 > /dev/null 2>&1; then
        :
    else
        tmux new-session -d -s $1 
        tmux send-keys -t $1 "cd $2" C-m
        tmux send-keys -t $1 "$3" C-m
    fi
}

ensure_tmux_session "sound-on-motion-act" "/opt/sound-on-motion" "/opt/sound-on-motion/start.sh"
