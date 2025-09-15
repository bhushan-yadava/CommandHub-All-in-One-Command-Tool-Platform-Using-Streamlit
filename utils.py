def log_command(cmd):
    with open("commands.log", "a") as f:
        f.write(f"{cmd}\n")
