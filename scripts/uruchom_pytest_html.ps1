Param()

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$pytestReportDir = Join-Path $projectRoot "reports\pytest"
$pytestReportFile = Join-Path $pytestReportDir "report.html"
$coverageReportDir = Join-Path $projectRoot "reports\coverage"
$coverageReportFile = Join-Path $coverageReportDir "index.html"
$pythonExe = Join-Path $projectRoot "venv\Scripts\python.exe"

if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Nie znaleziono interpretera: $pythonExe"
}

New-Item -ItemType Directory -Force -Path $pytestReportDir | Out-Null
New-Item -ItemType Directory -Force -Path $coverageReportDir | Out-Null

& $pythonExe -m pytest `
    --html=$pytestReportFile `
    --self-contained-html `
    --cov=moj_pakiet `
    --cov-report=term-missing `
    --cov-report=html:$coverageReportDir `
    -q

Write-Host ""
Write-Host "Raport testów HTML zapisany w:"
Write-Host $pytestReportFile
Write-Host ""
Write-Host "Raport coverage HTML zapisany w:"
Write-Host $coverageReportFile
