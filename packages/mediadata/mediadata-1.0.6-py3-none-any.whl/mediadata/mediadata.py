#! /usr/bin/python3

import sys
from .lib.Arguement import Arguement
import os
import json

def printHelp():
    print("Usage: "+sys.argv[0]+" [track --type=<query>] --file=<filename>")
    exit(-1)

def main():
    print("Media Data Tool")
    argsObj = Arguement(sys.argv)
    if argsObj.hasOptions(['--help', '-h']) :
        printHelp()

    if argsObj.hasOptionValue("--file"):
        data = json.loads(os.popen('mediainfo --Output=JSON "'+argsObj.getOptionValue("--file")+'"').read())
        # print(json.dumps(data, indent=4))
        # print("-=-=-=-=-=-=-=-=-=")
        print('Checking file data: ')
        if argsObj.hasCommand("track") and argsObj.hasOptionValue("--type") :
            print("Checking for track of type " + argsObj.getOptionValue("--type") + " in " + argsObj.getOptionValue("--file") + "....")
            error = False
            for track in data['media']['track']:
                if (track['@type']) == (argsObj.getOptionValue('--type')) :
                    data = json.dumps(track, indent=4)
                    if argsObj.hasOptions(['--list-keys', '-l']):
                        # print('Available keys for track of type ' + argsObj.getOptionValue("--type") + ' in ' + argsObj.getOptionValue("--file") + ' are: ')
                        print(track.keys())
                        error = False
                        break
                    elif argsObj.hasOptionValue('--key'):
                        print(track[argsObj.getOptionValue("--key")])
                    else :
                        print(data)
                    error = False
                    break
                else :
                    error = True
            if error:
                print("No track of type " + argsObj.getOptionValue("--type"))
        else : 
            print(json.dumps(data, indent=4))
    else:
        printHelp()


if __name__ == "__main__":
    main()
else:
    print("This module is not intended to be imported")