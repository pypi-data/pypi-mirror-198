#! /usr/bin/python3

class Arguement:
    def __init__(self, args):
        self.command = []
        self.options = []
        self.optionValues = {} # Dict / Set = Unique No Repeating Values
        self.args = args
        # print("args: ", self.args)

        for arg in self.args:
            if "-" in arg:
               if "=" in arg:
                   pair = arg.split("=")
                   self.options.append(pair[0]) # Appending the Key to the List
                   self.optionValues[pair[0]] = pair[1] # Appending the Key and Value to the Dict
               else:
                   self.options.append(arg)
            else:
                self.command.append(arg)
        # ===========================================================================================================================================================
        # Coding Here is not good, I can make a function to check if the option is there or not and if it is there then I can add it to the list
        # If I want to integrate all options like help, opt.., etc in oops concept I can keep it here (after parsing args we can check if help is there or not)
        # to generate help for every options and to autogenerate we can use self.options list and generate help for each option and if h is there na just print help and starts exit
        # if "-h" in self.options: # or "--help" in self.options:
        #     print("Help")
        #     exit(-1)
        # if "-v" in self.options: # or "--version" in self.options:
        #     print("Version")
        #     exit(-1)
        # if "-o" in self.options: # or "--output" in self.options:
        #     print("Output")
        #     exit(-1)
        # if "-f" in self.options: # or "--file" in self.options:
        #     print("File")
        #     exit(-1)
        # if "-t" in self.options: # or "--type" in self.options:
        #     print("Type")
        #     exit(-1)
        # if "-l" in self.options: # or "--list-keys" in self.options:
        #     print("List Keys")
        #     exit(-1)
        # ===========================================================================================================================================================
        # Check if the command and options are correct
        # print(f"command: {self.command}")
        # print(f"options: {self.options}")
        # print(f"optionValues: {self.optionValues}")
    # ------------------------------------------------------------
    # Commands End 
    # arg.hasOptions(["-l", "-h"])
    def hasOptions(self, options: list):
        userOptions = set(self.options)
        requiredOptions = set(options)
        return len(list(requiredOptions & userOptions)) >= 1
    
    def hasOption(self, option, default=False):
        if option in self.hasOptions([option]):
            return True
        return default
    
    def hasOptionValue(self, option):
        if option in self.optionValues:
            return option in self.optionValues
        return False
    # ------------------------------------------------------------
    def hasCommands(self, command):
        # if command in self.command:
        #     return True
        # return default
        userCommand = set(self.command)
        requiredCommand = set([command])
        return list(requiredCommand & userCommand)

    def hasCommand(self, command, default=False):
        if command in self.hasCommands(command):
            return True
        return default
    # ------------------------------------------------------------
    def getOptionValue(self, option, default=None):
        if option in self.optionValues:
            # print("option: ", option)
            # print("optionValues: ", self.optionValues[option])
            return self.optionValues[option]
        return default
    # ------------------------------------------------------------





    