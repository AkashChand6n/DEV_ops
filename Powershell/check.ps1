try {
    $path=[Environment]::GetFolderPath("Desktopdirectory")
    Write-Output $path
    if (Test-Path $path -PathType Container) {
        Write-Output "Home directory exists: $HOME"
    } else {
        Write-Output "Home directory does not exist."
    }
    
}
catch {
    write-host "An error occurred: $($_.InvocationInfo.ScriptLineNumber):$($Error[0])"
    <#Do this if a terminating exception happens#>
}