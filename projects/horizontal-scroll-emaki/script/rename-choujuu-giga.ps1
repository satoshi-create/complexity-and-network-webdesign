# rename-choujuu-giga.ps1
# 鳥獣人物戯画の画像を連番でリネーム（例：cyoujyuu_yamazaki_kou_01.jpg）

# 画像のあるディレクトリに移動（このスクリプトが scripts/ にある想定）
Set-Location "..\public\images\"

# .jpgファイルを取得
$files = Get-ChildItem *.jpg | Sort-Object Name
$i = 1

# 連番で名前を変更
foreach ($file in $files) {
    $newName = "cyoujyuu_yamazaki_kou_{0:D2}.jpg" -f $i
    Rename-Item $file.FullName $newName
    $i++
}

Write-Host "✅ Renamed $($i - 1) files in public/images/"
