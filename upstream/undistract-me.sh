# Copyright (c) 2008-2012 undistract-me developers. See LICENSE for details.
#
# Check for interactive bash and that we haven't already been sourced.
[ -z "$BASH_VERSION" -o -z "$PS1" -o -n "$last_command_started_cache" ] && return

. /usr/share/undistract-me/long-running.bash

# pre-populate the ignore list
export LONG_RUNNING_IGNORE_LIST=$( ( awk '/Exec=/ { match($1,"=(.*)",a); sub(/^.*\//, "", a[1]); print a[1] }' /usr/share/applications/*.desktop;
  [ -f "/etc/undistract-me/ignore" ] && awk '/^[^# ]/' /etc/undistract-me/ignore;
  [ -f "~/.config/undistract-me/ignore" ] && awk '/^[^# ]/' ~/.config/undistract-me/ignore ) | sort | uniq | tr '\n' ' ');


notify_when_long_running_commands_finish_install
