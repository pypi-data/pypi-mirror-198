class UserDetails:
    user_id = None
    name = None
    email = None
    phone_number = None
    role = None
    device_id = None

    def __init__(self, user_details):
        self.user_id = user_details.get("user_id")
        self.name = user_details.get("name")
        self.email = user_details.get("email")
        self.phone_number = user_details.get("phone_number")
        self.role = user_details.get("role")
        self.device_id = user_details.get("device_id")