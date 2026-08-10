def welcome_user(name):
    return f"👋 Welcome {name}!"


def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


def membership_status(status):
    if status == "Active":
        return "🟢 Active Member"
    else:
        return "🔴 Inactive Member"