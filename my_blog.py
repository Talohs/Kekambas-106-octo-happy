class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None

    def create_new_user(self):
        username = input("Please enter a user name:")
        if username in {u.username for u in self.users}:
            print(f"User with username {username} already exists")
        else:
            password = input("Please enter a password: ")
            new_user = User(username, password)
            self.users.add(new_user)
            print(f'{new_user} has been created.')

    def log_user_in(self):
        username = input("What is your user name?")
        password = input("What is your password?")
        for user in self.users:
            if user.username == username and user.check_password(password):
                self.current_user = user
                print(f'{user} has been logged in')
                break
        else:
            print("Username and/or Password is incorrect")

    def log_user_out(self):
        self.current_user = None
        print('You have successfully logged out')

    def create_post(self):
        if self.current_user is not None:
            title = input("Enter the title of your post: ")
            body = input('Enter the body of your post ')
            new_post = Post(title, body, self.current_user)
            self.posts.append(new_post)
            print(f"{new_post.title()} has been created!")
        else:
            print("You must be logged in to perform this action")

    def view_posts(self):
        if self.posts:
            for post in self.posts:
                print(post)
        else:
            print("There are currently no posts for this blog")

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
        self.password = password_guess[::-2]
        

class Post:
    id_counter = 1

    def __init__(self, title, body, author):
        """
        title:str
        body: str
        author: User
        """
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1

    def __str__(self) -> str:
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post

    def __repr__(self) -> str:
        return f"Post {self.id}|{self.title}"


def run_blog():
    my_blog = Blog()
    while True:
        if my_blog.current_user is None:
            print("1. Signup\n2. Sign in\n3. View all posts\n5.Quit")
            to_do = input('Which option would you like to do?')
            while to_do not in {'1', '2', '3', '5'}:
                to_do = input('Invalid option. Please choose 1 or 5.')
            if to_do == '5':
                print('Thanks for checking out the blog')
                break
            elif to_do == '1':
                #method to create a new user
                my_blog.create_new_user()
            elif to_do == '2':
                my_blog.log_user_in()
            elif to_do == '3':
                my_blog.view_posts()
        else:
            print("1. Log Out\n2. Logout")
            to_do = input("Which option would you like to choose?")
            while to_do not in {'1', '2', '3'}:
                to_do = input('Invalid option. Please choose 1. 2. or 3.')
            if to_do == '1':
                my_blog.log_user_out()
            elif to_do == '2':
                my_blog.create_post()
            elif to_do == '3':
                my_blog.view_posts()

run_blog()
                

