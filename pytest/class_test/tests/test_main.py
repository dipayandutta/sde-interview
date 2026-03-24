import pytest 
from src.user_manager import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

#--------------------
# TEST = Add user
#---------------------

def test_add_user(user_manager):
    result = user_manager.add_user("dip",30)

    assert result is True 
    assert user_manager.users["dip"] == 30 

#-------------------
# TEST -Duplicate users
#---------------------
def test_add_duplicate_user(user_manager):
    user_manager.add_user("dip",30)

    with pytest.raises(ValueError):
        user_manager.add_user("dip",30)

#-------------
#TEST invalid age
#----------------
def test_invalid_age(user_manager):
    with pytest.raises(ValueError):
        user_manager.add_user("dip",-5)

#------------------
#TEST Get users
#--------------------
def test_get_user(user_manager):
    user_manager.add_user("dip",25)

    user = user_manager.get_user("dip")

    assert user["username"] == "dip"
    assert user["age"] == 25 

#------- 
#TEST USER not found
#----------
def test_get_user_not_found(user_manager):
    with pytest.raises(KeyError):
        user_manager.get_user("User not Found")

#-------------
#TEST Delete User
#------------

def test_delete_user(user_manager):
    user_manager.add_user("dip",25)

    result = user_manager.delete_user("dip")

    assert result is True 
    assert "dip" not in user_manager.users 

#---------
#TEST List all Users
#---------

def test_list_users(user_manager):
    user_manager.add_user("dip",30)
    user_manager.add_user("alex",32)

    users = user_manager.get_users()

    assert len(users) == 2
    assert users["dip"] ==30
    assert users["alex"] == 32 
