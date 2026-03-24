class UserManager:

    def __init__(self):
        self.users = {}

    # Add user 
    def add_user(self,username,age):
        if username in self.users:
            raise ValueError("User already Exists")
        if age < 0:
            raise ValueError("Invalid Age")
        
        self.users[username] = age 
        
        return True 
    
    def get_user(self,username):
        if username not in self.users:
            raise KeyError("User not Found")
        
        return {"username": username, "age": self.users[username]}
    
    def delete_user(self,username):
        if username not in self.users:
            raise KeyError("Username Not Found")
        del self.users[username]
        return True 
    
    def get_users(self):
        return self.users