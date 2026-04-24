@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
for %%I in ("%SCRIPT_DIR%..") do set "PROJECT_ROOT=%%~fI"

set "REPORTS_ROOT=%PROJECT_ROOT%\reports"
set "PDOC_REPORT_DIR=%REPORTS_ROOT%\pdoc"
set "PYTEST_REPORT_DIR=%REPORTS_ROOT%\pytest"
set "PYTEST_REPORT_FILE=%PYTEST_REPORT_DIR%\report.html"
set "PYTEST_CACHE_DIR=%PYTEST_REPORT_DIR%\.pytest_cache"
set "COVERAGE_REPORT_DIR=%REPORTS_ROOT%\coverage"
set "COVERAGE_REPORT_FILE=%COVERAGE_REPORT_DIR%\index.html"
set "COVERAGE_DATA_FILE=%TEMP%\moj_pakiet_coverage_%RANDOM%_%RANDOM%"
set "PDOC_INDEX_FILE=%PDOC_REPORT_DIR%\moj_pakiet\index.html"
set "VENV_PYTHON=%PROJECT_ROOT%\venv\Scripts\python.exe"

if exist "%VENV_PYTHON%" (
    set "PYTHON_EXE=%VENV_PYTHON%"
) else (
    set "PYTHON_EXE=python"
)

if defined PYTHONPATH (
    set "PYTHONPATH=%PROJECT_ROOT%\src;%PYTHONPATH%"
) else (
    set "PYTHONPATH=%PROJECT_ROOT%\src"
)

if not exist "%PDOC_REPORT_DIR%" mkdir "%PDOC_REPORT_DIR%"
if not exist "%PYTEST_REPORT_DIR%" mkdir "%PYTEST_REPORT_DIR%"
if not exist "%PYTEST_CACHE_DIR%" mkdir "%PYTEST_CACHE_DIR%"
if not exist "%COVERAGE_REPORT_DIR%" mkdir "%COVERAGE_REPORT_DIR%"

set "COVERAGE_FILE=%COVERAGE_DATA_FILE%"

"%PYTHON_EXE%" -m pdoc --html --force --output-dir "%PDOC_REPORT_DIR%" moj_pakiet
if errorlevel 1 goto :error

"%PYTHON_EXE%" -m coverage run --branch --source=moj_pakiet -m pytest --html="%PYTEST_REPORT_FILE%" --self-contained-html -o cache_dir="%PYTEST_CACHE_DIR%" -q
if errorlevel 1 goto :error

"%PYTHON_EXE%" -m coverage html -d "%COVERAGE_REPORT_DIR%"
if errorlevel 1 goto :error

"%PYTHON_EXE%" -m coverage report
if errorlevel 1 goto :error

if exist "%COVERAGE_DATA_FILE%" del /q "%COVERAGE_DATA_FILE%" >nul 2>nul

echo.
echo Dokumentacja pdoc zapisana w:
echo %PDOC_INDEX_FILE%
echo.
echo Raport testow HTML zapisany w:
echo %PYTEST_REPORT_FILE%
echo.
echo Raport coverage HTML zapisany w:
echo %COVERAGE_REPORT_FILE%
goto :eof

:error
echo.
echo Generowanie raportow zakonczone bledem.
exit /b 1
