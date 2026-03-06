#!/bin/bash
+
Name="Brytany"

echo "Hello, $name"

if [ -f /var/log/syslog ]; then
    echo "syslog found!"
else
    echo "syslog missing!"
fi