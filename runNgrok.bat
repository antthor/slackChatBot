:: Run ngrok to expose localhost to the internet
@echo off
set ngrokPath=%~dp0ngrok.exe
set downloadUrl=https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip
set tempZip=%TEMP%\ngrok.zip

if exist "%ngrok.exe%" (
    echo ngrok.exe found
    "%ngrokPath%" http 3000
) else (
    echo ngrok.exe not found
    echo Downloading ngrok...
    powershell -Command "Invoke-WebRequest -Uri '%downloadUrl%' -OutFile '%tempZip%'"
    echo Unzipping ngrok...
    powershell -Command "Expand-Archive -Path '%tempZip%' -DestinationPath '%~dp0' -Force"
    if exist "%ngrokPath%" (
        echo ngrok.exe downloaded successfully
        "%ngrokPath%" http 3000
    ) else (
        echo Failed to download ngrok.exe
    )
)