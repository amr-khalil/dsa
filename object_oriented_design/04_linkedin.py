"""
The requirements for LinkedIn are defined below:

R1: Users should be able to add information to their profile including education, experiences, achievements, and skills.

R2: Users should be able to search for, and also view, pages, groups, and other users.

R3: Users should be able to send and cancel connection requests. They should also be able to respond to the connection requests of other users by either accepting or ignoring them.

R4: Users should be able to follow other users without adding them as their connection.

R5: Users should be able to view their number of connections, profile views, post impressions, and search appearances.

R6: Users should be able to request and give recommendations to other users.

R7: Users should be able to write a new post.

R8: Users should be able to react, share, and comment on a post. They should also be able to react or comment on an existing comment.

R9: A user should be able to send and receive messages from other users.

R10: The system should send a notification to the user to inform them about messages, connection requests, or comments on their post.

R11: Users should be able to create company pages. Users should be able to follow other company pages.

R12: Company pages should have a list of job openings that users can apply for.

R13: A user should be able to create and join groups.
"""

from __future__ import annotations
from datetime import datetime

class UsernameExistsError(Exception):
    """User name already exits"""
class ConnectionRequest:
    def __init__(self, sender: User, receiver: User):
        self.sender = sender
        self.receiver = receiver
        self.status = "pending"

    def accept(self):
        self.sender.connections.append(self.receiver)
        self.receiver.connections.append(self.sender)
        self.status = "accepted"

    def ignore(self):
        self.status = "ignored"


class Message:
    def __init__(self, sender: User, receiver: User, content: str):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now()


class CompanyPage:
    def __init__(self, name: str, admin: User):
        self.name = name
        self.admin = admin
        self.followers = []
        self.job_openings: list[JobOpening] = []
        self.observers: list[User] = []  # List of observers (users)

    def add_follower(self, user: User):
        self.followers.append(user)
        self.observers.append(user)

    def remove_follower(self, user: User):
        self.followers.remove(user)
        self.observers.remove(user)

    def notify_followers(self, message: str):
        for observer in self.observers:
            observer.receive_notification(message)

    def add_job_opening(self, job_opening: JobOpening):
        self.job_openings.append(job_opening)
        message = f"New job opening posted on {self.name}: {job_opening.title}"
        self.notify_followers(message)

class JobOpening:
    def __init__(self, title: str, description: str, company: CompanyPage):
        self.title = title
        self.description = description
        self.company = company
        
        
class Notification:
    def __init__(self, message):
        self.message = message

class Request:
    def __init__(self):
        ...
        
