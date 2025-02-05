try {
    $check = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principle = New-Object Security.Principal.WindowsPrincipal($check)
    $is_admin = $principle.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
    if ($is_admin) {
        "You are an administrator"
        <# Action to perform if the condition is true #>
    }
    else {
        "dont have admin rights"
        <# Action when all if and elseif conditions are false #>
    }
}
catch {
    "error in linr number: $($_.InvocationInfo.ScriptLineNumber):$($Error[0])"
    
}