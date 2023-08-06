# colorPrint
colorPrint is a very light weight module that enables you to print in color without having to use fstring codes and memorising complicated (or too long to write !) syntax...

I wrote it in order to save time when I'm coding scripts that generates a lot of terminal prompts which are painfull to read wthout colors !

## Basic usage
The script uses a cprint function and tags in the string starting by the `§` symbol.

```python
from colorPrint import cprint

# First Try :
cprint("Now I can use §-SUCCESSGreen color !")

cprint("The §_INFOtext§ I want to §_SUCCESSprint§ using §_WARNINGWarning background!")

# Same with shortcodes :
cprint("The §_#Itext§ I want to §_#Sprint§ using §_#WBackground colors!")
cprint("Or §-#Itext§ using §-#WForeground colors!")

# Compatibility
# use of the § symbol
cprint("colorPrint is §-#Icompatible§ with the usage of the § §§_#Scharacter§ if you need it §-#Danyway§ !")
# use of fstring
value = "Oh la la"
cprint(f"§_#I{value}§, colorPrint is §-#Icompatible§ with the usage of fStrings variables §-#Dif you need it§ !")
```

![ScreenShot ColorPrint Module](https://github.com/romaindudek/colorPrint/blob/medias/ScreenShot_colorprint.png?raw=true)

As simple as that !

## How tags works

ColorPrint tags allways starts with `§` symbol. In order to change  the text color or background color, you need to start with an ***opening tag***.

The ***closing tag*** is needed only if you wnat to end the start tag effect before the end of the string.

### Opening tag
The opening tag second char is meant to define if it is a backgound or a foreground color. it is either `-`(*foreground*) or `_`(*Background*)

Available opening tags:<br>

![ScreenShot ColorPrint Module](https://github.com/romaindudek/colorPrint/blob/medias/ScreenShot_colorprint_tags.png?raw=true)

### Closing tag
The closing tag is just `§`. As long as it comes after an opening tag, it will be considered as a closing tag.

---

## More to come...
In the next upgrade I will add the ability to change the default colors right after importing the module...