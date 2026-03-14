#!/bin/bash

check_ports() {
    local host= "127.0.0.1"
    local ports=(80 443 22)  # List of ports to check
    
    for port in "${ports[@]}"; do
        nc -zv "$host" "$port" &> /dev/null
        if [ $? -eq 0 ]; then
            echo "Port $port is open on $host"
        else
            echo "Port $port is closed on $host"
        fi
    done
}
check_ports