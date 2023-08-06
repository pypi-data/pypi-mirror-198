@echo off
call run-cli.cmd
REM Reimplements "make test"

call release\test-unittest.cmd
call release\test-flake8.cmd

echo:
echo # Test Process Completed!
echo:
pause
REM TODO: Use timeout -T 30
