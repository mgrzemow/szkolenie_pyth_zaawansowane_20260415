#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
project_root="$(cd "$script_dir/.." && pwd)"

reports_root="$project_root/reports"
pdoc_report_dir="$reports_root/pdoc"
pytest_report_dir="$reports_root/pytest"
pytest_report_file="$pytest_report_dir/report.html"
pytest_cache_dir="$pytest_report_dir/.pytest_cache"
coverage_report_dir="$reports_root/coverage"
coverage_report_file="$coverage_report_dir/index.html"
coverage_data_file="$(mktemp "${TMPDIR:-/tmp}/moj_pakiet_coverage.XXXXXX")"
pdoc_index_file="$pdoc_report_dir/moj_pakiet/index.html"

if [[ -x "$project_root/venv/bin/python" ]]; then
    python_exe="$project_root/venv/bin/python"
elif [[ -x "$project_root/venv/Scripts/python.exe" ]]; then
    python_exe="$project_root/venv/Scripts/python.exe"
elif command -v python3 >/dev/null 2>&1; then
    python_exe="$(command -v python3)"
elif command -v python >/dev/null 2>&1; then
    python_exe="$(command -v python)"
else
    echo "Nie znaleziono interpretera Python ani w venv, ani w PATH." >&2
    exit 1
fi

if [[ -n "${PYTHONPATH:-}" ]]; then
    export PYTHONPATH="$project_root/src:$PYTHONPATH"
else
    export PYTHONPATH="$project_root/src"
fi

export COVERAGE_FILE="$coverage_data_file"

mkdir -p "$pdoc_report_dir" "$pytest_report_dir" "$pytest_cache_dir" "$coverage_report_dir"

"$python_exe" -m pdoc \
    --html \
    --force \
    --output-dir "$pdoc_report_dir" \
    moj_pakiet

"$python_exe" -m coverage run \
    --branch \
    --source=moj_pakiet \
    -m pytest \
    --html="$pytest_report_file" \
    --self-contained-html \
    -o "cache_dir=$pytest_cache_dir" \
    -q

"$python_exe" -m coverage html -d "$coverage_report_dir"
"$python_exe" -m coverage report

rm -f "$coverage_data_file"

printf '\nDokumentacja pdoc zapisana w:\n%s\n' "$pdoc_index_file"
printf '\nRaport testow HTML zapisany w:\n%s\n' "$pytest_report_file"
printf '\nRaport coverage HTML zapisany w:\n%s\n' "$coverage_report_file"
