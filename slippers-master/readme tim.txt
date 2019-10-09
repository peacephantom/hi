open powershell admin
type that
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
may need to reopen
type choco install python
open cmd
type pip install -r C:\Users\tbros\Desktop\slippers-master\requirements.txt