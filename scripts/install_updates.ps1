$ErrorActionPreference = 'Stop'
$bundleRoot = Split-Path -Parent $PSScriptRoot
$taskName = 'OQW-Dataset-Daily-Update'
$pythonPath = Join-Path $bundleRoot 'runtime\python.exe'
if (-not (Test-Path -LiteralPath $pythonPath)) { throw 'Missing bundled Python runtime.' }
& $pythonPath (Join-Path $bundleRoot 'launcher.py') --prepare-data
if ($LASTEXITCODE -ne 0) { throw 'Unable to initialize local database.' }
$logPath = Join-Path $bundleRoot 'logs\scheduled-sync.jsonl'
$dbPath = (Join-Path $bundleRoot 'data\oqw.sqlite3').Replace('\','/')
$arguments = '-m database.managed_sync --database-url "sqlite:///' + $dbPath + '" --due --log "' + $logPath + '"'
$action = New-ScheduledTaskAction -Execute $pythonPath -Argument $arguments -WorkingDirectory $bundleRoot
$trigger = New-ScheduledTaskTrigger -Daily -At '09:00'
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 30)
$principal = New-ScheduledTaskPrincipal -UserId ([Security.Principal.WindowsIdentity]::GetCurrent().Name) -LogonType Interactive -RunLevel Limited
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing -and $existing.Actions.Execute -ne $pythonPath) { throw 'An update task belongs to another OQW folder. Remove that old task first, then retry.' }
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description 'OQW portable dataset update: daily due checks, current logged-in user.' -Force | Select-Object TaskName,State
