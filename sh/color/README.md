# About

`color` is CLI tool for displaying and styling terminal colors using ANSI escape codes. It supports color visualization and manipulation in various formats like color names, RGB values, and hexadecimal codes. The script also allows users to copy ANSI codes directly to their clipboard for easy use elsewhere.

# Features

1. Display colors in both foreground and background formats.
2. Group terminal colors according to their base shades.
3. Style text with various attributes like bold, italic, or underline.
4. Generate ANSI escape codes for color styling, optionally copying them to the clipboard.

# Install

1. Clone the repository:
```bash
git clone https://github.com/ximenesyuri/color /your/favorite/location/color
```
2. Source the `color` script in your `.bashrc`:
```bash
echo "source /your/favorite/locatation/color/color" >> $HOME/.bashrc
```

# Dependencies

1. `bash` (mandatory)
2. `xclip` or `xsel` (optional)

# Usage

```
USAGE 
   color [color] [syle]
   color all [number] [fg/bg]
   color ansi [color] [text]

OPTIONS
    [color] [style] ........... Prints the [color] in the given [style] in fg and bg
    all  [number] [fg/bg] ..... Displays the first [number] of the 256 colors fg/bg
    ansi [color] [text] ....... Show ANSI code for [text] in [color] and copy to clipboard
    help, --help .............. Print this help message

VALUES
    [color] ................... Hexadecimal ["#color"] or RGB ["(r,g,b)"]
    [style] ................... bold, italic, underline

EXAMPLES
    color red bold      
    color "(255,0,0)" bold
    color r=255 bold
    color "#123456"
    color 123456
    color all 50 bg             
    color ansi "#123456" "some text"
```
