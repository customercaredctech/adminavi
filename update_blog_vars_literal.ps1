$files = @("blog.html", "blog-sds-visa.html", "blog-canada-permit.html")

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw
        
        $content = $content.Replace('var(--primary)', 'var(--c-navy)')
        $content = $content.Replace('var(--primary-light)', 'var(--c-navy-dark)')
        $content = $content.Replace('var(--secondary)', '#F4F7F6')
        $content = $content.Replace('var(--accent)', 'var(--c-gold)')
        $content = $content.Replace('var(--accent-hover)', '#B8962E')
        $content = $content.Replace('var(--text-dark)', 'var(--c-navy)')
        $content = $content.Replace('var(--text-body)', 'var(--c-text-light)')
        $content = $content.Replace('var(--text-muted)', 'var(--c-text-light)')
        $content = $content.Replace('var(--bg-page)', '#F4F7F6')
        $content = $content.Replace('var(--radius-lg)', 'var(--rad-lg)')
        $content = $content.Replace('var(--radius-md)', 'var(--rad-md)')
        $content = $content.Replace('Outfit', 'Poppins')
        
        $content = $content.Replace('btn-secondary', 'btn-navy')
        $content = $content.Replace('btn-accent', 'btn-gold')
        $content = $content.Replace('<script src="main.js"></script>', '')
        
        Set-Content -Path $file -Value $content
        Write-Host "Updated variables in $file"
    }
}
