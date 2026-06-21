$ErrorActionPreference = 'Stop'

Write-Host 'Running Django system check...'
python manage.py check
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'Running migration plan check...'
python manage.py migrate --check
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'Running pytest...'
pytest
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'Running flake8...'
flake8 .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'Running mypy...'
mypy .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host 'Validation finished successfully.'
