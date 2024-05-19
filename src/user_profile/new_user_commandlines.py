from pathlib import Path
import sys
PARENT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0,PARENT_DIR)

from db_utils import DbUtils

class CommandHandler:
    def __init__(self):
        self.fname = None
        self.lname=None
        self.dob = None
        pass

    def collect_first_name(self,fname):
        self.fname = fname
        
    def collect_last_name(self, lname):
        self.lname =lname

    def handle_profession_input(self):
        print("Handling profession input...")

    def collect_dob(self,dob):
        self.dob = dob

    def process_user_input(self, user_input):
        user_input = user_input.lower()
        if user_input == "new user":
            self.handle_new_user()
        elif user_input == "ready to start":
            self.start_conversation()
        elif user_input == "profession":
            self.handle_profession_input()
        elif user_input == "collect other questions":
            self.collect_other_questions()
        else:
            print("Could not determine appropriate action based on input.")

# Example usage:
command_handler = CommandHandler()

while True:
    user_input = input("Enter your response (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    command_handler.process_user_input(user_input)
