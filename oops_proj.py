class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook || How would you like to proceed?
                           1. Press 1 to Signup
                           2. Press 2 to Signin
                           3. Press 3 to Write a Post
                           4. Press 4 to Message a Friend
                           5. Press any key to Exit
                           
                           ->""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please Signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter the Email/username here -> ")
            pwd = input("Enter the password here -> ")
            if self.username == uname and self.password == pwd:
                print("You have Signed in Successfully !!")
                self.loggedin = True
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to Signin First to post something")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            friend = input("Whom to send message -> ")
            print(f"Your message has been sent to {friend}")
        else:
            print("You need to Signin First")
        print("\n")
        self.menu()
obj = chatbook()