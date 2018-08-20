import sublime, sublime_plugin
import re


class ReplacerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            selected_text = self.view.substr(region)
            new_text = re.sub("(\.pdf)", '', selected_text)
            self.view.replace(edit, region, new_text)