# ./runner/runcmds.py
"""
指令多条命令
"""
import subprocess

from runner import Task

class RunCmds(Task):
    def __init__(self, name:str, cmds:list, cmd:str, wait:bool, cwd:str):
        super().__init__(name, 'cmds')
        self.cmds = cmds
        self.cmd = cmd# bash or sh
        self.wait = wait
        self.cwd = cwd if cwd != '' else None

    def run(self):
        p = subprocess.Popen(self.cmd, stdin=subprocess.PIPE, cwd=self.cwd)
        for cmd in self.cmds:
            p.stdin.write(cmd.encode('utf-8'))
            p.stdin.write(b'\n')
            p.stdin.flush()
        if self.wait:
            p.communicate(b'exit\n')
        else:
            p.stdin.write(b'exit\n')
            p.stdin.flush()
            p.stdin.close()

def run_cmds(name:str, cmds:list, cmd:str="cmd", wait:bool=True, cwd:str=None):
    task = RunCmds(name, cmds, cmd, wait, cwd)
    task.run()