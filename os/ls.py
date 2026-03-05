import os        # provides OS-level functions like listdir, stat, path joining
import stat      # provides constants and helpers to interpret st_mode permission bits
import pwd       # lets us look up username from a numeric user ID (UID)
import grp       # lets us look up group name from a numeric group ID (GID)
import time      # used to format timestamps and get the current time
import sys       # gives access to command-line arguments via sys.argv

def get_permissions(st_mode):
    """Convert st_mode to rwxrwxrwx string like ls -l."""
    is_dir = 'd' if stat.S_ISDIR(st_mode) else '-'   # prefix 'd' if it's a directory, '-' otherwise
    perms = [                                          # list of (character, bitmask) pairs for each permission bit
        ('r', stat.S_IRUSR), ('w', stat.S_IWUSR), ('x', stat.S_IXUSR),  # owner: read, write, execute
        ('r', stat.S_IRGRP), ('w', stat.S_IWGRP), ('x', stat.S_IXGRP),  # group: read, write, execute
        ('r', stat.S_IROTH), ('w', stat.S_IWOTH), ('x', stat.S_IXOTH),  # others: read, write, execute
    ]
    perm_str = ''.join(c if st_mode & mask else '-' for c, mask in perms)  # if bit is set use the char, else '-'
    return is_dir + perm_str  # combine the type char with the 9-character permission string e.g. 'drwxr-xr-x'

def format_time(ts):
    """Format mtime like ls: 'Jan  1 12:00' or 'Jan  1  2023'."""
    t = time.localtime(ts)   # convert Unix timestamp (seconds since epoch) to local time struct
    now = time.time()        # get current time as Unix timestamp for comparison
    # If modified within ~6 months, show time; otherwise show year
    if abs(now - ts) < 15552000:              # 15552000 seconds = 180 days (~6 months)
        return time.strftime('%b %e %H:%M', t)  # recent file: show month, day, and HH:MM e.g. 'Mar  4 12:30'
    else:
        return time.strftime('%b %e  %Y', t)    # older file: show month, day, and full year e.g. 'Jan  1  2023'

def colorize(name, st_mode):
    """Add ANSI color codes like ls --color."""
    RESET  = '\033[0m'    # ANSI escape code to reset color back to terminal default
    BLUE   = '\033[1;34m' # bold blue — used for directories
    GREEN  = '\033[1;32m' # bold green — used for executable files
    CYAN   = '\033[1;36m' # bold cyan — used for symbolic links

    if stat.S_ISLNK(st_mode):                              # check if this entry is a symbolic link
        return CYAN + name + RESET                         # wrap name in cyan color codes
    elif stat.S_ISDIR(st_mode):                            # check if this entry is a directory
        return BLUE + name + RESET                         # wrap name in blue color codes
    elif st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):  # check if any execute bit is set
        return GREEN + name + RESET                        # wrap name in green color codes
    return name  # regular file with no special type — return name without any color

def ls(path='.', show_hidden=False):
    try:
        entries = os.listdir(path)    # get list of all filenames in the target directory
    except PermissionError:           # catch the case where we don't have read access to the directory
        print(f"ls.py: cannot open directory '{path}': Permission denied")  # print friendly error message
        return                        # exit the function early since we can't proceed

    if not show_hidden:                                          # if the -a flag was NOT passed
        entries = [e for e in entries if not e.startswith('.')]  # filter out hidden files (those starting with '.')

    entries.sort(key=str.lower)   # sort entries alphabetically, case-insensitively (so 'Z' comes after 'a')

    # --- Collect stat info & compute column widths ---
    rows = []          # will hold one tuple of formatted strings per directory entry
    total_blocks = 0   # accumulates total disk usage in 1K blocks (shown in the 'total N' header line)

    for name in entries:                              # iterate over each filename in the directory
        full_path = os.path.join(path, name)          # build the full path e.g. './myfile.txt'
        try:
            st = os.lstat(full_path)                  # lstat gets file info WITHOUT following symlinks (unlike os.stat)
        except FileNotFoundError:                     # file may have been deleted between listdir and lstat
            continue                                  # skip this entry and move on to the next

        total_blocks += st.st_blocks // 2   # st_blocks is in 512-byte units; divide by 2 to get 1K blocks

        perm  = get_permissions(st.st_mode)  # get the formatted permission string e.g. '-rw-r--r--'
        nlink = str(st.st_nlink)             # number of hard links to this file/directory, as a string for formatting
        try:
            user  = pwd.getpwuid(st.st_uid).pw_name   # look up the username that owns this file by UID
        except KeyError:                               # UID has no matching user (e.g. deleted user)
            user  = str(st.st_uid)                     # fall back to showing the raw numeric UID
        try:
            group = grp.getgrgid(st.st_gid).gr_name   # look up the group name that owns this file by GID
        except KeyError:                               # GID has no matching group
            group = str(st.st_gid)                     # fall back to showing the raw numeric GID
        size  = str(st.st_size)              # file size in bytes, as a string for column-width calculation
        mtime = format_time(st.st_mtime)    # format the last-modified timestamp into a human-readable string

        # Symlink target
        display_name = name                     # default display name is just the filename
        if stat.S_ISLNK(st.st_mode):            # if this entry is a symbolic link
            try:
                target = os.readlink(full_path)              # read where the symlink points to
                display_name = f"{name} -> {target}"         # append the target path e.g. 'link -> /etc/hosts'
            except OSError:                                  # couldn't read the symlink target (broken link etc.)
                pass                                         # keep display_name as just the name

        rows.append((perm, nlink, user, group, size, mtime, display_name, st.st_mode))  # store all formatted fields as a tuple

    if not rows:   # if after filtering there are no entries to display
        return     # exit early — nothing to print

    # --- Determine field widths ---
    w_nlink = max(len(r[1]) for r in rows)   # widest hard-link count string, for right-aligned column
    w_user  = max(len(r[2]) for r in rows)   # widest username string, for left-aligned column
    w_group = max(len(r[3]) for r in rows)   # widest group name string, for left-aligned column
    w_size  = max(len(r[4]) for r in rows)   # widest file size string, for right-aligned column

    print(f"total {total_blocks}")   # print total disk usage header, just like real 'ls -l' does

    for perm, nlink, user, group, size, mtime, name, st_mode in rows:  # unpack each row tuple for printing
        colored_name = colorize(name, st_mode)   # apply ANSI color codes based on the file type
        print(
            f"{perm} "               # permission string e.g. '-rw-r--r--'
            f"{nlink:>{w_nlink}} "   # hard link count, right-aligned to widest value
            f"{user:<{w_user}} "     # owner username, left-aligned to widest value
            f"{group:<{w_group}} "   # group name, left-aligned to widest value
            f"{size:>{w_size}} "     # file size in bytes, right-aligned to widest value
            f"{mtime} "              # last modified timestamp e.g. 'Mar  4 12:30'
            f"{colored_name}"        # filename with ANSI color applied (no trailing space needed)
        )

if __name__ == '__main__':           # only run the code below if this script is executed directly (not imported)
    # Basic arg parsing: support a path and -a flag
    args = sys.argv[1:]              # grab all command-line arguments, skipping the script name itself
    show_hidden = '-a' in args       # True if the user passed '-a' flag to show hidden files
    args = [a for a in args if not a.startswith('-')]  # remove all flags so only the path argument remains
    target = args[0] if args else '.'  # use provided path if given, otherwise default to current directory '.'
    ls(target, show_hidden)            # call the main ls function with the resolved path and hidden-file flag
