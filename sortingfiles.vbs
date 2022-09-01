Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "Drive:/path/to/my/script.py" & Chr(34), 0
Set WshShell = Nothing