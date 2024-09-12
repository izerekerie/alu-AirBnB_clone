import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB application."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program by typing 'quit'."""
        return True

    def do_EOF(self, arg):
        """Exit the program by typing EOF (Ctrl+D)."""
        print()  # To ensure the prompt moves to a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_help(self, arg):
        """Display help information for commands."""
        if arg:
            # If the user specifies a command, delegate to cmd's help method
            super().do_help(arg)
        else:
            # If no command is specified, provide a brief description of all commands
            print("Available commands:")
            print("  quit   - Exit the program")
            print("  EOF    - Exit the program")
            print("  help   - Show this help message")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
