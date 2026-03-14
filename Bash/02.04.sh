#!/bin/bash

log_file="$HOME/test.log"
alert_file="$HOME/security_alerts.log"

# Check if log file exists
if [ ! -f "$log_file" ]; then
    echo "Log file not found: $log_file"
    exit 1
fi 

Count=$(grep -c "Failed password" "$log_file")
if [ $Count -gt 0 ]; then
    echo "ALERT: $Count failed login attempts detected!" >> "$alert_file"
fi

echo "Number of failed login attempts: $Count"