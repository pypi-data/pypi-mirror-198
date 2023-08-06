class CommandPool(object):
    processes = []
    polls = []

    def run_command(self, command):
        import subprocess

        process1 = subprocess.Popen(
            [
                "C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "-c",
                "start-process cmd -Wait -ArgumentList '/C %s'" % command,
            ],
            shell=False,
            stdout=subprocess.PIPE,
        )
        self.processes.append(process1)
        self.polls.append(process1.poll())

    def poll(self):
        while True:
            wait_count = 0
            for index in range(len(self.polls)):
                if self.polls[index] == None:
                    self.polls[index] = self.processes[index].poll()
                    if self.polls[index] == None:
                        wait_count = wait_count + 1
            if wait_count == 0:
                break
            import time

            time.sleep(0.01)
