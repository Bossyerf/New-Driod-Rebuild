param()
$ErrorActionPreference = 'Stop'
Write-Host "Setting up venv and installing requirements..."
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
Write-Host "Done."
