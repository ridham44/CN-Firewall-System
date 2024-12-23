import csv
from .utils.rule_validator import compare_rules

def load_rules(file_path="rules.csv"):
    """Loads firewall rules from a CSV file."""
    rules = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                rules.append(row)
    except FileNotFoundError:
        print(f"[ERROR] The file {file_path} does not exist.")
    return rules

def validate_with_route_table(protocol, src_addr, dst_addr, src_port, dst_port, rules):
    """Validates the rule based on the route table."""
    for rule in rules:
        # Compare rules based on the protocol, source IP, source port, destination IP, and destination port
        if (
            str(rule[1]).strip().lower() == protocol.lower() and
            compare_rules(rule[2], [src_addr, dst_addr, "any"]) and
            compare_rules(rule[4], [dst_addr, src_addr, "any"]) and
            compare_rules(rule[3], [src_port, "any", 0]) and
            compare_rules(rule[5], [dst_port, "any", 0])
        ):
            if str(rule[0]).lower() == "allow":
                return True
            elif str(rule[0]).lower() in ["deny", "disable"]:
                continue
    return False
