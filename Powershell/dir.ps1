#find the desktop directory if it exists
$path=[Environment]::GetFolderPath("Desktopdirectory")
echo $path
if (Test-Path $path -PathType Container) {
    Write-Output "Home directory exists: $HOME"
} else {
    Write-Output "Home directory does not exist."
}