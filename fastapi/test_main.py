import pytest 
from fastapi.testclient import TestClient 
from main import app 

# Create the test client 
client = TestClient(app)

#-------------
# TEST Case -1 Default Command ls
#-------------

def test_default_command():
    response = client.get('/')
    assert response.status_code == 200 

    data = response.json()

    assert data["command"] == "ls"
    assert data["returncode"] == 0
    assert "stdout" in data 
    assert "stderr" in data 

#-----------------------------
# TEST CASE -2 Custom Command 
#------------------------------

def test_custom_command():
    response = client.get("/?cmd=echo hello")
    
    assert response.status_code == 200 

    data = response.json()

    assert data["command"] == "echo hello"
    assert data["returncode"] == 0
    assert "hello" in data["stdout"]


#---------------------------
#TEST CASE 3 Invalid Command
#---------------------------

def test_invalid_command():
    response = client.get("/?cmd=invalidcommand")

    assert response.status_code == 200

    data = response.json()

    assert data["returncode"] == 0
    assert data["stderr"] == -1

#-----------------------------
#TEST CASE 4 Command Injection
#-----------------------------
def test_command_injection():
    response = client.get("/?cmd=echo hello && whoami")

    assert response.status_code == 200

    data = response.json()

    assert "hello" in data["stdout"] # If this sucess then the vulnerable application

#---------------------------------
#TEST CASE 5 Parameterized Test
#-----------------------------------
@pytest.mark.parametrize("cmd,expected",[
    ("echo test","test"),
    ("pwd", None)
])
def test_multiple_commands(cmd,expected):

    response = client.get("/?cmd={cmd}")
    assert response.status_code == 200

    data = response.json()

    assert data["returncode"] == 127

    if expected:
        assert expected in data["stdout"]