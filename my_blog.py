class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None

    def create_new_user(self):
        username = input("Please enter a user name:")
        if username in {u.username for u in username}:
            print(f"User with username {username} already exists")
        else:
            password = input("Please enter a password: ")
            new_user = User(username, password)
            self.users.add(new_user)
            print(f'{new_user} has been created.')

class User:
    id_counter = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password[::-2]
        self.id = User.id_counter
        User.id_counter += 1

    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User {self.id}{self.username}>"

    def check_password(self, password_guess):
        return self.password = password_guess[::-2]


class Post:
    pass


def run_blog():
    my_blog = Blog()
    while True:
        if my_blog.current_user is None:
            print("1. Signup\nQuit")
            to_do = input('Which option would you like to do?')
            while to_do not in input('1','5'):
                to_do = input('Invalid option. Please choose 1 or 5.')
            if to_do == '5':
                print('Thanks for checking out the blog')
                break
            elif to_do == '1':
                #method to create a new user
                my_blog.create_new_user()

run_blog()
                

