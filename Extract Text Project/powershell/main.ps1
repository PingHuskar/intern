$f = Get-ChildItem tbl_T*.txt

$outputFile = (Get-Location).Path + '\output.txt'
Remove-Item $outputFile
New-Item $outputFile -ItemType file

try {
	$writer = [System.IO.Streamwriter] $outputFile
	#$writer.writeline($f)
	foreach ($e in $f) {

	#$writer.writeline($e)

	$lines = (Get-Content $e).Length

	#Write-Output $lines

	#$writer.writeline($lines)

	#$writer.writeline($e)
	
	if ($lines -eq 0) {
		continue
	} else {
		$writer.writeline($e)
		$writer.writeline('< '+ ($lines-3)*1000+ ' rows')
		$openfile = (Get-Content $e)
		$line = $openfile[$lines-1]
		$writer.writeline($line.substring(26,5))
	}
	
	#$length = $e.length
	#$w = $e.substring($length-6)
	#$writer.writeline('$f.length '+$f.length)
	#$writer.writeline((Get-Location).Path)
<#
	
#>
	#$writer.writeline($lines + $lines-)

	}

	<#
	$writer.writeline('Hello ' + $name + '!!!')
	$writer.writeline('Hello ' + $prop[2] + '!!!')
	$writer.writeline('Hello ' + $prop[2][3] + '!!!')#>

	$writer.close()
}
finally {
	
}