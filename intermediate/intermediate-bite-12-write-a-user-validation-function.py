"""
Create a function that takes a username and checks for a valid user:

The username is in USERS,
the user is not expired, and
the user has the ADMIN role.
If those 3 conditions are met return SECRET.

If one of the conditions is not True raise an exception you define yourself: UserDoesNotExist,
UserAccessExpired and UserNoPermission respectively. Check out the tests for more detail.
"""

from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here
class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass

### My solution

def get_secret_token(username):
    for user in USERS:
        if user.name == username:
            if user.expired == False:
                if user.role == ADMIN:
                    return SECRET
                else:
                    raise UserNoPermission
            else:
                raise UserAccessExpired
    raise UserDoesNotExist

### PyBites original solution

def pyb_get_user(username):
    # This constructs a dictionary from USERS namedtuples
    users = {user.name: user for user in USERS}
    # Q: Is there any difference in accessing nonexisting key when using d[crap] vs d.get(crap)?
    # A: Yes, there is.
    # https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey
    # So if user does not exist, None is returned
    # https://stackoverflow.com/questions/9494404/use-of-true-false-and-none-as-return-values-in-python-functions
    return users.get(username)

def pyb_get_secret_token(username):
    user = pyb_get_user(username)
    print(type(user))
    print(user)
    # Big question here how to test for None: if not x vs if x is None
    # https://stackoverflow.com/questions/24270344/is-there-a-difference-between-if-not-x-and-if-x-is-none
    if not user:
        raise UserDoesNotExist

    if user.expired:
        raise UserAccessExpired

    if user.role != ADMIN:
        raise UserNoPermission

    return SECRET




try:
    print(pyb_get_secret_token('Tim'))
except UserAccessExpired as e:
    print("Caught exception UserAccessExpired")
except UserNoPermission as e:
    print("Caught exception UserNoPermission")
except UserDoesNotExist as e:
    print("Caught exception UserDoesNotExist")
