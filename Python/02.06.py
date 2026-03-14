# log_filter.py

def get_unique_ips(ip_list):
    return sorted (list(set(ip_list)))

ips = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "10.0.0.1"]
unique_ips = get_unique_ips(ips)
print("Unique IPs:", unique_ips)