:
: Usage: apk_launcher.bat <apk file>
:
: *.apk ‚ÉŠÖ˜A•t‚¯‚ð‚µ‚Ä‚¨‚­‚Æ•Ö—˜‚Å‚·
:

: command line arguments
@IF "%~1" == "" (
    echo Usage: apk_launcher.bat ^<apk file^> >&2
    goto end
)

: check python command existence
@where python 1>nul 2>nul
@IF %ERRORLEVEL% NEQ 0 (
    echo Error: python command not found.
    goto end
)

: launch python script
@set BATCH_DIR=%~dp0
@python %BATCH_DIR%src\apk_launcher.py "%~f1"

:end
pause
