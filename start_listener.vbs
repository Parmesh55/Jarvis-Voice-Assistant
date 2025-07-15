Set fso = CreateObject("Scripting.FileSystemObject")
fso.CreateTextFile "C:\Users\acer\AppData\Roaming\Jarvis\boot_flag.txt", True
Set shell = CreateObject("WScript.Shell")
shell.Run "pythonw.exe D:\Jarvis\listener\wake_word_listener.py", 0
