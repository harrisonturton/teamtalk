import os
import sys
from dotenv import load_dotenv

# load .env config variables
load_dotenv()

def getenv(env_variable_key):
    """
    Tries to read an environment variable from the local
    .env file. If it does not exist, then it terminates
    the running program.
    """
    env = os.environ.get(env_variable_key, None)
    if not env:
        print("Error: environment variable ", env_variable_key, " is not set in the .env file.")
        sys.exit(1)
    return env
