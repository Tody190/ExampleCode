::��ȡ�û���������
set user_path=
::��ע����ȡ�û���������
for /f "skip=2 tokens=3*" %%a in ('reg query HKCU\Environment /v PATH') do if [%%b]==[] ( set user_path="%%~a" ) else ( set user_path="%%~a %%~b")
::������������ӵ��û���������
set want_added_var=
echo %user_path%| findstr  %want_added_var%>nul && (
    echo %want_added_var% has been added to the user PATH
) || (
    ::��ӻ�������
    ::ʹ��setx /M ���ϵͳ������������Ҫ����ԱȨ�ޣ�
    setx PATH %want_added_var%;%user_path%
    echo Added %want_added_var% to user PATH
)