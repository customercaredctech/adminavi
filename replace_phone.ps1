$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    Write-Host "Processing $($file.Name)"
    $content = [System.IO.File]::ReadAllText($file.FullName)
    $updated = $content.Replace("+1 (555) 123-4567", "+1 (778) 889-7490")
    $updated = $updated.Replace("15551234567", "17788897490")
    $updated = $updated.Replace("+1 (555) 123 - 4567", "+1 (778) 889-7490")
    $updated = $updated.Replace("+1(555)123-4567", "+1 (778) 889-7490")
    $updated = $updated.Replace("555-123-4567", "778-889-7490")
    if ($content -ne $updated) {
        if ($file.IsReadOnly) {
            $file.IsReadOnly = $false
        }
        [System.IO.File]::WriteAllText($file.FullName, $updated)
        Write-Host "Updated $($file.Name)"
    }
}
