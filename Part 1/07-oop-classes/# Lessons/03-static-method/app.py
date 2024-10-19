class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def post_status(self, status):
        print(f"{self.username} posted: {status}")

    # static method
    @staticmethod
    def validate_email(email):
        return "@" in email and len(email) > 3


def main():
    user_one = User("leo", "leo@netninja.dev")
    user_two = User("raph", "raph@netninja.dev")

    # call static method
    print(User.validate_email('leo@netninja.dev'))


if __name__ == "__main__":
    main()
