class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def update_name(self, new_name):
        self.name = new_name

    def update_email(self, new_email):
        self.email = new_email