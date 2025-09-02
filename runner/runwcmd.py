# ./runner/runwcmd.py
"""
执行单线命令
"""
import subprocess

from runner import Task
import config
import datas


class RunWCmd(Task):
    def __init__(self, name:str, cmd:str, args:str, admin:bool, cwd:str='', maximize:bool=False, minimize:bool=False):
        super().__init__(name, 'wcmd')
        self.cwd = cwd
        if cmd.startswith('"') and cmd.endswith('"'):
            self.cmd = cmd[1:-1]
        self.cmd = cmd
        self.args = args
        self.admin = admin
        self.maximize = maximize
        self.minimize = minimize
    
    def run(self):
        cmd = []
        if self.admin and not config.settings['advanced']['disAdmin']:
            cmd.append('pkexec')
        cmd.append(self.cmd)
        if self.args:
            cmd.append(self.args)
        try:
            if self.cwd:
                p = subprocess.Popen(cmd, cwd=self.cwd)
            else:
                p = subprocess.Popen(cmd)
            p.wait()
        except Exception as e:
            datas.root_error_message = f"任务: {self.name}\n\n"\
            f"目标: {self.cmd}\n\n"\
            f"参数: {self.args}\n\n"\
            f"错误: {e}"
            if datas.root:
                datas.root.event_generate('<<RunCmdError>>')


def run_wcmd(name:str, cmd:str, args:str, admin:bool=False, cwd:str='None', maximize:bool=False, minimize:bool=False):
    task = RunWCmd(name, cmd, args, admin, cwd, maximize, minimize)
    task.run()
