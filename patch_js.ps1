$snippet = @"
  // Desktop dropdown interactive toggle
  const dropdownParent = document.querySelector('.nav-has-dropdown') || document.querySelector('.nav-dropdown');
  const dropdownToggle = document.querySelector('.nav-dropdown-toggle') || (dropdownParent ? dropdownParent.querySelector('a') : null);
  
  if (dropdownToggle && dropdownParent) {
    dropdownToggle.addEventListener('click', (e) => {
      e.preventDefault();
      dropdownParent.classList.toggle('is-active');
    });
    document.addEventListener('click', (e) => {
      if (!dropdownParent.contains(e.target)) {
        dropdownParent.classList.remove('is-active');
      }
    });
  }
</script>
"@

$files = Get-ChildItem -Path '.' -Filter *.html -File
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    if (-not $content.Contains("Desktop dropdown interactive toggle")) {
        $lastScriptTag = $content.LastIndexOf("</script>")
        if ($lastScriptTag -ge 0) {
            $newContent = $content.Substring(0, $lastScriptTag) + $snippet + $content.Substring($lastScriptTag + 9)
            Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
            Write-Host "Patched $($file.Name)"
        }
    }
}
