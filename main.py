class teacher:
    def __init__(self):
        print("I am a teacher")
    
    def __del__(self):
        print("I am an employee")

obj = teacher()
del obj