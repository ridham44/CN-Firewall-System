"""
Ridham Patel
22002171310092
21/12/24
"""
from src.firewall import load_rules, validate_with_route_table

def test_firewall():
    # Load firewall rules
    rules = load_rules("rules.csv")
    print("Firewall Rules Loaded.")
    
    print("Firewall Rule Management System")
    print("===============================")
    interface = input("Enter the interface to monitor (e.g., eth0): ").strip()
    print(f"Monitoring traffic on interface: {interface}")
    
    # Get user input for source and destination details
    protocol = input("Enter protocol (TCP/UDP): ").strip().lower()
    src_ip = input("Enter source IP: ")
    dst_ip = input("Enter destination IP: ")
    src_port = int(input("Enter source port: "))
    dst_port = int(input("Enter destination port: "))
    
    # Validate with the provided inputs
    result = validate_with_route_table(protocol, src_ip, dst_ip, src_port, dst_port, rules)
    action = "ALLOWED" if result else "DENIED"
    print(f"Traffic ({protocol.upper()}) from {src_ip}:{src_port} to {dst_ip}:{dst_port} is {action}.")

if __name__ == "__main__":
    test_firewall()
