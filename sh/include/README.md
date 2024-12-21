# About

`include` is a Bash function that uses local sources to conditionally source another Bash function. It can be used in `.bashrc` to source scripts that define functions, improving the shell load speed.

# Install

Just clone the repository and source the `include` script in your `.bashrc`:
```bash
git clone https://github.com/ximenesyuri/include /your/favorite/location
echo "source /your/favorite/location/include" >> $HOME/.bashrc
```

# Usage

In your `.bashrc`

1. below the sourcing of the `include` script, declare an associative array `INCLUDES` withe the `name` of the functions to be locally sourced and the `path`s to the script containing them:
```bash
source /your/favorite/location/include

declare -A INCLUDES
INCLUDES[name1]="path1"
INCLUDES[name2]="path2"
...
```
2. call the function `include` passing the name of the functions you want to locally source:
```bash
include name1
include name2
...
# single command, multiple includes:
include name1 name2 ...
```

> **OBS.** You can also call `include "*"` to locally include all functions defined in the `INCLUDES` associative array.

# Example

Suppose you have completion scripts for commands `command1`, `command2`, etc. If you directly source them in your `.bashrc` you will have to load them every time you open a new terminal session: even if you will not use the commands `command1`, `command2`, etc.

Alternatively, you can use `include` to only source the completion script when the corresponding command to be completed is called:

```bash
source /your/favorite/location/include

declare -A INCLUDES
INCLUDES[command1]="path/to/completion1.sh"
INCLUDES[command2]="path/to/completion2.sh"
...
include "*"
```
