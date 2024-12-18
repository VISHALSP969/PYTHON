class User:
    def __init__(self,first_name,last_name,username,email,location):
        self.first_name=first_name.title()
        self.last_name=last_name.title()
        self.username=username
        self.email=email
        self.location=location.title()
        self.login_attempts=0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Username : {self.username}")
        print(f"Email : {self.email}")
        print(f"Location : {self.location}")

    def greet_user(self):
        print(f"Welcome back, {self.username}")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges=[]

    def show_privileges(self):
        print("\nprivileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")

eric=Admin('eric','matthes','e_matthes','e_matthes@example.com','alaska')
eric.describe_user()

eric.privileges=['can reset passwords','can moderate discussions','can suspend accounts']
eric.show_privileges()