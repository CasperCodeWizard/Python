# List of users
users = [
    "User_1", "User_2"
]

# Function to generate random passwords
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

# Dictionary to store users and their new passwords
user_passwords = {user: generate_password() for user in users}

# Generate SQL script using IF statements
sql_script = "DO\n$$\nBEGIN\n"

for user, password in user_passwords.items():
    sql_script += f"""
    IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '{user}') THEN
        EXECUTE 'ALTER ROLE {user} WITH PASSWORD ''{password}''';
    ELSE
        EXECUTE 'CREATE ROLE {user} WITH LOGIN PASSWORD ''{password}''';
    END IF;
    """

sql_script += "\nEND;\n$$;"

# Display the generated SQL script
sql_script
