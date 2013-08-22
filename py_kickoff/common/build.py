# Use cases: both test code and usage examples
from builder import rule
import os

@rule("file1.txt")
def file1():
    "File doesn't exist; run rule"
    file("file1.txt", 'w')

def touchOrCreate(f): # Ordinary function
    "Bring file up to date; creates it if it doesn't exist"
    if os.path.exists(f):
        os.utime(f, None)
    else:
        file(f, 'w')

dependencies = ["dependency1.txt", "dependency2.txt",
                "dependency3.txt", "dependency4.txt"]

targets = ["file1.txt", "target1.txt", "target2.txt"]

allFiles = targets + dependencies

@rule(allFiles)
def multipleTargets():
    "Multiple files don't exist; run rule"
    [file(f, 'w') for f in allFiles if not os.path.exists(f)]

@rule(["target1.txt", "target2.txt"], "dependency1.txt", "dependency2.txt")
def multipleBoth():
    "Multiple targets and dependencies"
    [touchOrCreate(f) for f in ["target1.txt", "target2.txt"]]

@rule("target1.txt","dependency1.txt","dependency2.txt","dependency3.txt")
def target1():
    "Brings target1.txt up to date with its dependencies"
    touchOrCreate("target1.txt")

@rule()
def updateDependency():
    "Updates the timestamp on all dependency.* files"
    [touchOrCreate(f) for f in allFiles if f.startswith("dependency")]

@rule()
def clean():
    "Remove all created files"
    [os.remove(f) for f in allFiles if os.path.exists(f)]

@rule()
def cleanTargets():
    "Remove all target files"
    [os.remove(f) for f in targets if os.path.exists(f)]

@rule("target2.txt", "dependency2.txt", "dependency4.txt")
def target2():
    "Brings target2.txt up to date with its dependencies, or creates it"
    touchOrCreate("target2.txt")

@rule(None, target1, target2)
def target3():
    "Always brings target1 and target2 up to date"
    print target3

@rule(None, clean, file1, multipleTargets, multipleBoth, target1,
      updateDependency, target2, target3)
def all():
    "Brings everything up to date"
    print all

rule.default = all
rule.main() # Does the build, handles command-line arguments
