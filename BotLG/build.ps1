$exclude = @("venv", "BotLG.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotLG.zip" -Force