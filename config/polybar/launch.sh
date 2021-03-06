#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar
# MONITOR=$(polybar -m|tail -1|sed -e 's/:.*$//g')
# monitor = ${env:MONITOR:fallback-value}
# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

if type "xrandr"; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload example &
  done
else
  polybar --reload example &
fi

echo "Bars launched..."
