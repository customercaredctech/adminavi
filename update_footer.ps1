$files = Get-ChildItem -Filter *.html
foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    $target = '<div>&copy; <span id="year"></span> Admission Navigate Consultancy. All rights reserved.</div>'
    $replacement = '<div>&copy; <span id="year"></span> Admission Navigate Consultancy. All rights reserved. Designed and developed by dctechoffial <a href="https://instagram.com" target="_blank" style="margin-left:10px;"><i class="fab fa-instagram"></i></a></div>'
    
    $newContent = $content.Replace($target, $replacement)
    
    if ($newContent -cne $content) {
        Set-Content -Path $f.FullName -Value $newContent
        Write-Host "Updated footer in $($f.Name)"
    }
}
