::获取用户环境变量
set user_path=
::从注册表获取用户环境变量
for /f "skip=2 tokens=3*" %%a in ('reg query HKCU\Environment /v PATH') do if [%%b]==[] ( set user_path="%%~a" ) else ( set user_path="%%~a %%~b")
::将环境变量添加到用户环境变量
set want_added_var=
echo %user_path%| findstr  %want_added_var%>nul && (
    echo %want_added_var% has been added to the user PATH
) || (
    ::添加环境变量
    ::使用setx /M 添加系统环境变量（需要管理员权限）
    setx PATH %want_added_var%;%user_path%
    echo Added %want_added_var% to user PATH
)