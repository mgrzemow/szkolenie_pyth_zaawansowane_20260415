# Uruchamianie Pytest

Najczęstsze komendy:

```bash
pytest
pytest -q
pytest -vv
pytest tests/pytest_przyklady/test_pesel.py
pytest -k pesel
pytest --cov=moj_pakiet --cov-report=term-missing
pytest --html=reports/pytest/report.html --self-contained-html
pytest --html=reports/pytest/report.html --self-contained-html --cov=moj_pakiet --cov-report=html:reports/coverage
```

Przydatne opcje:
- `-q` daje krótszy raport,
- `-vv` pokazuje więcej szczegółów,
- `-k fragment` uruchamia tylko testy pasujące do nazwy,
- podanie ścieżki pozwala uruchomić jeden plik,
- `--cov=moj_pakiet` włącza pomiar pokrycia kodu,
- `--cov-report=term-missing` pokazuje, których linii testy nie pokryły,
- `--cov-report=html:reports/coverage` zapisuje raport coverage do HTML,
- `--html=...` zapisuje raport HTML,
- `--self-contained-html` tworzy pojedynczy plik łatwy do wysłania dalej.

Typowy sposób pracy:
1. uruchamiasz test,
2. patrzysz, który przypadek nie przeszedł,
3. poprawiasz kod albo test,
4. uruchamiasz ponownie tylko wybrany fragment.

W tym projekcie dodatkowe narzędzia testowe można doinstalować przez:

```bash
pip install -e .[test]
```

Gotowa komenda raportu HTML dla tego projektu:

```bash
venv\Scripts\python.exe -m pytest --html=reports/pytest/report.html --self-contained-html --cov=moj_pakiet --cov-report=term-missing --cov-report=html:reports/coverage -q
```

Jeśli chcesz użyć gotowego skryptu PowerShell, uruchom:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\uruchom_pytest_html.ps1
```

Po uruchomieniu dostajesz dwa osobne raporty:
- `reports/pytest/report.html` dla wyników testów,
- `reports/coverage/index.html` dla pokrycia kodu.
