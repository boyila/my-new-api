question_mapping = {
        "hello": "I would like to as you some security questions to identify who you are and better assist you. Can you please give me your first Name?",
        "first name": ["what is your last name?"],
        "last name":['what is your date of birth?,please provide date of birth in mm/dd/yyyy format'],
        "date of birth":['Looks like you are existing user'],
        "new user": ["Welcome. To give you better advice and insights, it is important to get some financial information from you. This will take about 10 minutes. If you don't have 10 minutes, you can also do this in parts. Do some right now and come back and finish later. Are you ready to start?"],
        "existing user": ['can you provide your more details about your financial details'],
        "ready to start": ["What's your profession?"],
        "profession": ["Enter your profession-specific question here."],
        "collect other questions": ["Enter other relevant questions here."],
        # Add more response-question pairs as needed
    }