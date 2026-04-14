def validate_login(username, password):
    """Basic validation for login credentials.##"""
    return len(username) > 0 and len(password) > 0
