"""
Requirements collection
The requirements for Facebook are defined below:

R1: Users should be able to set the privacy of their profile page. They should also be able to create their profile page and add information such as work experience, education, and place of living.
R2: Users of our system should be able to search for groups, pages, and other users.
R3: Users should be able to write a new post and set its privacy.
R4: Users should be able to send as well as respond to the friend requests of other users. Users should also be able to unfriend or block other users.
R5: Users should be able to follow other users without adding them to their friend list.
R6: Users should be able to like, share, and comment on a post. They should also be able to like or comment on an existing comment.
R7: The system should send the user a notification whenever there has been an interaction with them, such as receiving a message, a friend request, or a comment on their post.
R8: A user should be able to send messages and receive messages from other users.
R9: Users should be able to follow existing pages and join existing groups. They should also be able to unfollow or leave joined groups or followed pages.
R10: Users should be able to create their own groups and pages. Users can later set privacy or delete the groups or pages they own.
"""

class FacebookApp:
    def __init__(self):
        self.notifications = []

    class FacebookApp:
        def __init__(self):
            self.users = []
            self.groups = []
            self.pages = []
            self.notifications = []
            self.observers = []

        def attach_observer(self, observer):
            self.observers.append(observer)

        def detach_observer(self, observer):
            self.observers.remove(observer)

        def notify_observers(self, message):
            for observer in self.observers:
                observer.update(message)

    class User:
        def __init__(self, name):
            self.name = name
            self.profile = Profile()
            self.friends = []
            self.groups = []
            self.pages = []

        def set_privacy(self, privacy):
            self.profile.set_privacy(privacy)

        def create_profile(self, work_experience, education, place_of_living):
            self.profile.set_work_experience(work_experience)
            self.profile.set_education(education)
            self.profile.set_place_of_living(place_of_living)

        def send_friend_request(self, user):
            # Send a friend request to another user
            pass

        def respond_to_friend_request(self, user, accept):
            # Respond to a friend request from another user
            pass

        def unfriend(self, user):
            # Unfriend another user
            pass

        def block(self, user):
            # Block another user
            pass

    class NotificationObserver:
        def update(self, message):
            print(f"Received notification: {message}")

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users = []
            cls._instance.groups = []
            cls._instance.pages = []
        return cls._instance
    
    def __init__(self):
        self.users = []
        self.groups = []
        self.pages = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def create_group(self, name, privacy):
        group = Group(name, privacy)
        self.groups.append(group)
        return group

    def create_page(self, name, privacy):
        page = Page(name, privacy)
        self.pages.append(page)
        return page

    def delete_group(self, group):
        self.groups.remove(group)

    def delete_page(self, page):
        self.pages.remove(page)
        
    

class User:
    def __init__(self, name):
        self.name = name
        self.profile = Profile()
        self.friends = []
        self.groups = []
        self.pages = []
        self.notifications = []

    def set_privacy(self, privacy):
        self.profile.set_privacy(privacy)

    def create_profile(self, work_experience, education, place_of_living):
        self.profile.set_work_experience(work_experience)
        self.profile.set_education(education)
        self.profile.set_place_of_living(place_of_living)

    def search(self, keyword):
        # Search for groups, pages, and other users
        pass

    def write_post(self, content, privacy):
        post = Post(content, privacy)
        # Add the post to the user's profile
        self.profile.add_post(post)

    def send_friend_request(self, user):
        # Send a friend request to another user
        pass

    def respond_to_friend_request(self, user, accept):
        # Respond to a friend request from another user
        pass

    def unfriend(self, user):
        # Unfriend another user
        pass

    def block(self, user):
        # Block another user
        pass

    def follow_user(self, user):
        # Follow another user
        pass

    def like_post(self, post):
        # Like a post
        pass

    def share_post(self, post):
        # Share a post
        pass

    def comment_on_post(self, post, comment):
        # Comment on a post
        pass

    def like_comment(self, comment):
        # Like a comment
        pass

    def send_message(self, user, message):
        # Send a message to another user
        pass

    def receive_message(self, user, message):
        # Receive a message from another user
        pass

    def follow_page(self, page):
        # Follow a page
        pass

    def join_group(self, group):
        # Join a group
        pass

    def unfollow_page(self, page):
        # Unfollow a page
        pass

    def leave_group(self, group):
        # Leave a group
        pass

    def create_group(self, name, privacy):
        group = Group(name, privacy)
        # Add the group to the user's groups
        self.groups.append(group)

    def create_page(self, name, privacy):
        page = Page(name, privacy)
        # Add the page to the user's pages
        self.pages.append(page)

    def delete_group(self, group):
        # Delete a group
        pass

    def delete_page(self, page):
        # Delete a page
        pass


class Profile:
    def __init__(self):
        self.privacy = None
        self.work_experience = None
        self.education = None
        self.place_of_living = None
        self.posts = []

    def set_privacy(self, privacy):
        self.privacy = privacy

    def set_work_experience(self, work_experience):
        self.work_experience = work_experience

    def set_education(self, education):
        self.education = education

    def set_place_of_living(self, place_of_living):
        self.place_of_living = place_of_living

    def add_post(self, post):
        self.posts.append(post)


class Post:
    def __init__(self, content, privacy):
        self.content = content
        self.privacy = privacy
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, content):
        self.content = content
        self.likes = []

    def add_like(self, user):
        self.likes.append(user)


class Group:
    def __init__(self, name, privacy):
        self.name = name
        self.privacy = privacy


class Page:
    def __init__(self, name, privacy):
        self.name = name
        self.privacy = privacy


# Usage example
user1 = User("John")
user1.create_profile("Software Engineer", "Bachelor's Degree", "New York")
user1.set_privacy("Friends Only")
user1.write_post("Hello, world!", "Public")
user1.send_friend_request(user2)
user1.follow_user(user3)
user1.like_post(post1)
user1.send_message(user2, "Hi, how are you?")
user1.follow_page(page1)
user1.join_group(group1)
user1.create_group("My Group", "Private")
user1.create_page("My Page", "Public")
user1.delete_group(group1)
user1.delete_page(page1)


