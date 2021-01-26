import os

EXCLUDE_DIRS = ["dev", "proc", "sys"]
UID = os.getuid()
GIDS = os.getgroups()

def check_file(filename):
    file_stat = os.stat(filename)

    # World write permission
    if file_stat.st_mode & 0o002 != 0:
        return True

    # Group write permission
    if file_stat.st_gid in GIDS and file_stat.st_mode & 0o020 != 0:
        return True

    # User write permission
    if file_stat.st_uid == UID and file_stat.st_mode & 0o200 != 0:
        return True

    return False

def handler(event, context):
    retval = []

    for root, dirs, files in os.walk("/"):
        if root == "/":
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        # Checking folders
        for d in dirs:
            dir = os.path.join(root, d)
            try:
                if check_file(dir):
                    retval.append(dir)
            except:
                pass

        # Checking files
        for f in files:
            file = os.path.join(root, f)
            try:
                if check_file(file):
                    retval.append(file)
            except:
                pass

    return retval