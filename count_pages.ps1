param(
    [string]$DocName = "test_siwes_report.docx"
)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$docPath = Resolve-Path $DocName
$doc = $word.Documents.Open($docPath.Path)
$pages = $doc.ComputeStatistics(2)
Write-Host "WORD_EXACT_PAGE_COUNT: $pages ($DocName)"
$doc.Close([ref]$false)
$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
