import os

def shutdown(time):
    return os.system(f"shutdown -s -t {time}")

shutdown(3600)

