"""
What is the proxy pattern?
As the name implies, the proxy pattern is a structural pattern that creates a proxy object.
It acts as a placeholder for another object, controlling the access to it.
Usually, an object has an interface with several properties/methods that a client can access.
However, an object might not be able to deal with the clients’ requests alone due to heavy load or constraints such as dependency on a remote source that might cause delays (e.g., network requests).
In these situations, adding a proxy helps in dividing the load with the target object.
The proxy object looks exactly like the target object.
A client might not even know that they are accessing the proxy object instead of the target object.
The proxy handles the requests from the clients and forwards them to the target object,
preventing undue pressure on the target.

when to use the proxy pattern?
The proxy pattern tries to reduce the workload on the target object.
You can use it when dealing with heavy applications that perform a lot of network requests.
Since delays could occur when responding to such requests, using a proxy pattern will allow the target object to not get overburdened with requests.
A real-life example is HTTP requests.
These are expensive operations, therefore, the proxy pattern helps in reducing the number of requests forwarded to the target.
"""

import boto3
import logging
from botocore.exceptions import NoCredentialsError, ClientError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class S3Proxy:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name='us-east-1'):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.s3 = None
        self._create_client()

    def _create_client(self):
        try:
            self.s3 = boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
                region_name=self.region_name
            )
            logger.info('Successfully authenticated with AWS S3')
        except NoCredentialsError as e:
            logger.error('Credentials not available: %s', e)
            raise

    def upload_file(self, file_name, bucket_name, object_name=None):
        if not object_name:
            object_name = file_name
        try:
            self.s3.upload_file(file_name, bucket_name, object_name)
            logger.info('Uploaded file %s to bucket %s as %s', file_name, bucket_name, object_name)
        except ClientError as e:
            logger.error('Failed to upload file: %s', e)
            return False
        return True

    def download_file(self, bucket_name, object_name, file_name):
        try:
            self.s3.download_file(bucket_name, object_name, file_name)
            logger.info('Downloaded file %s from bucket %s as %s', object_name, bucket_name, file_name)
        except ClientError as e:
            logger.error('Failed to download file: %s', e)
            return False
        return True

    def list_buckets(self):
        try:
            response = self.s3.list_buckets()
            buckets = [bucket['Name'] for bucket in response['Buckets']]
            logger.info('Available buckets: %s', buckets)
            return buckets
        except ClientError as e:
            logger.error('Failed to list buckets: %s', e)
            return []

# Usage Example
if __name__ == '__main__':
    # Replace these with your actual AWS credentials
    AWS_ACCESS_KEY_ID = 'your-access-key-id'
    AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'

    s3_proxy = S3Proxy(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

    # List all S3 buckets
    print('Buckets:', s3_proxy.list_buckets())

    # Upload a file to a specific bucket
    s3_proxy.upload_file('test.txt', 'your-bucket-name', 'test.txt')

    # Download a file from a specific bucket
    s3_proxy.download_file('your-bucket-name', 'test.txt', 'downloaded_test.txt')



# """
# Example: Lazy Initialization (Virtual Proxy)
# Scenario:
# Imagine you have a database connection that is expensive to establish, and you want to establish it only when needed.
# """


# import time


# class DatabaseConnection:
#     def connect(self):
#         print("Establishing connection to the database...")
#         # Simulate expensive connection setup
#         time.sleep(2)
#         print("Database connection established.")

#     def execute_query(self, query):
#         print(f"Executing query: {query}")


# class DatabaseProxy:
#     def __init__(self):
#         self._database_connection = None

#     def _ensure_connection(self):
#         if self._database_connection is None:
#             self._database_connection = DatabaseConnection()
#             self._database_connection.connect()

#     def execute_query(self, query):
#         self._ensure_connection()
#         self._database_connection.execute_query(query)


# # Client Code
# if __name__ == '__main__':
#     proxy = DatabaseProxy()
#     print("Proxy object created, but no connection yet.")

#     # Lazy initialization: the connection is only established now
#     proxy.execute_query("SELECT * FROM users")
#     proxy.execute_query("SELECT * FROM orders")

# """
# Example: Access Control (Protection Proxy)
# Scenario:
# Restrict access to methods based on user roles.
# """


# class USERROLE:
#     ADMIN = 'admin'
#     USER = 'user'
    
# class Document:
#     def read(self):
#         return "Reading the document content..."

#     def write(self, content):
#         print(f"Writing content: {content}")


# class DocumentProxy:
#     def __init__(self, user_role):
#         self._document = Document()
#         self._user_role = user_role

#     def read(self):
#         return self._document.read()

#     def write(self, content):
#         if self._user_role == 'admin':
#             self._document.write(content)
#         else:
#             print("Access Denied: Only admin can write to the document.")


    
# # Client Code
# if __name__ == '__main__':

#     admin_proxy = DocumentProxy(user_role=USERROLE.ADMIN)
#     user_proxy = DocumentProxy(user_role=USERROLE.USER)

#     print("Admin trying to read and write:")
#     print(admin_proxy.read())
#     admin_proxy.write("New document content.")

#     print("\nUser trying to read and write:")
#     print(user_proxy.read())
#     user_proxy.write("Unauthorized content.")