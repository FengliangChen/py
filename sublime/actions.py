import sublime, sublime_plugin

class MygodCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("select_all")
        self.window.run_command("replacer")
       