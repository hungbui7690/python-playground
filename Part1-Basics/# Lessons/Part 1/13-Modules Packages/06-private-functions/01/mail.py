def send(email, message):
    print(f'Sending "{message}" to {email}')


# you can prefix a function name with an underscore (_) to make it private.
def _attach_file(filename):
    print(f"Attach {filename} to the message")
