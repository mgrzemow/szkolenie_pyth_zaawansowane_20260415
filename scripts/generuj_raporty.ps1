Param()

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$reportsRoot = Join-Path $projectRoot "reports"
$pdocReportDir = Join-Path $reportsRoot "pdoc"
$pytestReportDir = Join-Path $reportsRoot "pytest"
$pytestReportFile = Join-Path $pytestReportDir "report.html"
$pytestCacheDir = Join-Path $pytestReportDir ".pytest_cache"
$coverageReportDir = Join-Path $reportsRoot "coverage"
$coverageReportFile = Join-Path $coverageReportDir "index.html"
$coverageDataFile = Join-Path $env:TEMP ("moj_pakiet_coverage_{0}_{1}" -f $PID, [guid]::NewGuid().ToString("N"))
$pdocIndexFile = Join-Path $pdocReportDir "moj_pakiet\index.html"
$venvPython = Join-Path $projectRoot "venv\Scripts\python.exe"

if (Test-Path -LiteralPath $venvPython) {
    $pythonExe = $venvPython
} else {
    $pythonCommand = Get-Command python -ErrorAction SilentlyContinue
    if ($null -eq $pythonCommand) {
        throw "Nie znaleziono interpretera Python ani w venv, ani w PATH."
    }
    $pythonExe = $pythonCommand.Source
}

if ([string]::IsNullOrWhiteSpace($env:PYTHONPATH)) {
    $env:PYTHONPATH = Join-Path $projectRoot "src"
} else {
    $env:PYTHONPATH = "$(Join-Path $projectRoot "src");$env:PYTHONPATH"
}

New-Item -ItemType Directory -Force -Path $pdocReportDir | Out-Null
New-Item -ItemType Directory -Force -Path $pytestReportDir | Out-Null
New-Item -ItemType Directory -Force -Path $pytestCacheDir | Out-Null
New-Item -ItemType Directory -Force -Path $coverageReportDir | Out-Null

$env:COVERAGE_FILE = $coverageDataFile

& $pythonExe -m pdoc `
    --html `
    --force `
    --output-dir $pdocReportDir `
    moj_pakiet
if ($LASTEXITCODE -ne 0) {
    throw "Generowanie dokumentacji pdoc zakonczone bledem."
}

& $pythonExe -m coverage run `
    --branch `
    --source=moj_pakiet `
    -m pytest `
    --html=$pytestReportFile `
    --self-contained-html `
    -o cache_dir=$pytestCacheDir `
    -q
if ($LASTEXITCODE -ne 0) {
    throw "Generowanie raportow pytest/coverage zakonczone bledem."
}

& $pythonExe -m coverage html -d $coverageReportDir
if ($LASTEXITCODE -ne 0) {
    throw "Generowanie raportu coverage HTML zakonczone bledem."
}

& $pythonExe -m coverage report
if ($LASTEXITCODE -ne 0) {
    throw "Generowanie raportu coverage w terminalu zakonczone bledem."
}

Remove-Item -LiteralPath $coverageDataFile -Force -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "Dokumentacja pdoc zapisana w:"
Write-Host $pdocIndexFile
Write-Host ""
Write-Host "Raport testow HTML zapisany w:"
Write-Host $pytestReportFile
Write-Host ""
Write-Host "Raport coverage HTML zapisany w:"
Write-Host $coverageReportFile
