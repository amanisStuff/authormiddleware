import subprocess
from typing import Pattern
class search:
    @staticmethod
    def search_file_using_regex(file_name:str, expression:Pattern):
        """
        Purpose: allow the agent/user to search their own regex expression
        """
        result = subprocess.run("git grep -Ein '"+expression+"' "+file_name+"", stdout=subprocess.PIPE, shell=True)
        print(result.stdout.decode())
        pass
    @staticmethod
    def search_project_using_regex(expression:Pattern):
        """
        Purpose: allow the agent/user to search their own regex expression
        """
        result = subprocess.run("git grep -Ein '"+expression+"' *", stdout=subprocess.PIPE, shell=True)
        print(result.stdout.decode())
        pass
    # end def
    pass