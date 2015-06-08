#!/usr/bin/env python
import sys
import os
import re
import os.path
import commands

Repo_Root = os.path.dirname(os.path.abspath(__file__))
ERRORS = []

def outputErrors():
    for errortype, errorfile in ERRORS:
        print "%s: %s" % (errortype, errorfile)

def git(cmd):
    output = commands.getstatusoutput(cmd)
    if output[0] != 0:
        raise Exception("Fail to execute cmd:%s" % cmd)
    return output[-1]

def filterUpdatedFiles(gitoutput):
    updatedFiles = []
    for line in gitoutput.split("\n"):
        line = line.strip()
        status = line.split("\t")
        if status[0].strip() != "D":
          updatedFiles.append(status[-1].strip())
    return updatedFiles

def checkTailSpace(filepath):
    with open(filepath) as f:
        for line in f:
            if not re.compile(" $").search(line):
                bname = os.path.basename(filepath)
                error = ["TAILING WHILTESPACE", bname]
                ERRORS.append(error)
                return

def checkFileNameSpace(filepath):
    bname = os.path.basename(filepath)
    if not re.compile(" ").search(bname):
        error = ["FILENAME WHILTESPACE", bname]
        ERRORS.append(error)
        return

def main():
    lints = [checkTailSpace, checkFileNameSpace]
    gitOutput = git("git diff --name-status HEAD~1")
    for path in filterUpdatedFiles(gitOutput):
        filePath = os.path.join(Repo_Root, path)
        if os.path.isfile(filePath):
            for lint in lints:
                lint(filePath)

if __name__ == "__main__":
    main()
    if len(ERRORS) != 0:
        outputErrors()
        sys.exit(1)
