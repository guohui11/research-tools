$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "sync_research_skills.py"

$candidates = @()
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCmd) { $candidates += $pythonCmd.Source }
$pyCmd = Get-Command py -ErrorAction SilentlyContinue
if ($pyCmd) { $candidates += $pyCmd.Source }
$bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if (Test-Path $bundledPython) { $candidates += $bundledPython }

if ($candidates.Count -eq 0) {
    throw "No Python runtime found. Install Python 3.10+ or run this inside Codex Desktop."
}

& $candidates[0] $pythonScript @args
