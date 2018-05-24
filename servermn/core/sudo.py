SUDOPATH = "/usr/bin/sudo -p sudo:"
STDERR_FILE = "/dev/null"

def system(cmd):
    """Executes a shell command as root, STDOUT and STDERR won't be directed to any file
    @param command string with command to execute
    """
    sudocmd = SUDOPATH + " /bin/sh -c " + cmd + " 2> " + STDERR_FILE

    # Execute command

    pass

def command(cmd):
    """Execute a command as servermn user

    @param command string with the command to execute
    @returns Returns the output of the command in an array
    """
    pass

def root(cmds):
    """Executes the commands provided through sudo. Use this to execute priviledge comands

    @param commands strings with the command to execute
    @returns Returns the output of the command in an array
    """
    pass

def silenceRoot(cmds):
    """Executes the commands provided through sudo. Use this to execute priviledge comands
    Doesn:t throw execeptions, only returns the output and the exit status in the variable.

    @param commands strings with the command to execute
    @returns Returns the output of the command in an array
    """
    pass

def sudo(cmds, user):
    """Executes a command through sudo as a given user

    @param command string with the command to execute
    @param user user to run the command as
    """
    pass

def stat(file):
    """stat a file as root user and returns the information as stat object

    @param file file we want stat
    @return a Stat object with file system status for the file
    """
    pass