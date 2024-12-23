def compare_rules(primary_rule, secondary_rules):
    """Compares a rule with a list of secondary rules."""
    result = []
    for rule in secondary_rules:
        if str(primary_rule).strip() == str(rule).strip():
            result.append(True)
        else:
            result.append(False)
    return any(result)
