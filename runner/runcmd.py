# ./runner/runcmd.py
"""
执行命令行命令
"""
import subprocess

from runner import Task
import config
import datas

class RunCmd(Task):
    def __init__(self, name:str, cmd:str, args:str, admin:bool, cwd:str='', maximize:bool=False, minimize:bool=False):
        super().__init__(name, 'cmd')
        self.admin = admin
        self.cwd = cwd if cwd != '' else None
        if cmd.startswith('"') and cmd.endswith('"'):
            # 去除引号
            cmd = cmd[1:-1]
        # 对于非系统或PATH环境变量软件，建议使用路径全称避免文档、卷、路径名错误
        # 毕竟都写成快捷启动方式了，在创建任务的时候耐心点没什么问题吧
        self.cmd = cmd
        self.args = args
        self.maximize = maximize
        self.minimize = minimize

    def run(self):
        cmd = []
        if self.admin and not config.settings['advanced']['disAdmin']:
            # pkexec需要使用绝对路径
            cmd.append('pkexec')
        cmd.append(self.cmd)
        if self.args:
            cmd.append(self.args)
        try:
            if self.cwd:
                subprocess.Popen(cmd, cwd=self.cwd)
            else:
                subprocess.Popen(cmd)
        except Exception as e:
            datas.root_error_message = f"任务: {self.name}\n\n"\
            f"目标: {self.cmd}\n\n"\
            f"参数: {self.args}\n\n"\
            f"错误: {e}"
            if datas.root:
                datas.root.event_generate('<<RunCmdError>>')

def run_cmd(name:str, cmd:str, args:str, admin:bool, cwd:str='', maximize:bool=False, minimize:bool=False):
    task = RunCmd(name, cmd, args, admin, cwd, maximize, minimize)
    task.run()
