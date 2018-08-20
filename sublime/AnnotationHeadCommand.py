import sublime, sublime_plugin
import datetime
import os

class AnnotationHeadCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = os.path.basename(self.view.file_name())
        self.view.run_command("insert_snippet",
            {
                "contents" : self.annotation_for_file(file_name)
            }
        )
        
    def annotation_for_file(self, file_name):
        annotations = {
            "py" :  "#!/usr/bin/python\n"
                    "# -*- coding:utf-8 -*- "
                    "\n\n"
                    "'''"
                    "\n"
                    " @Author      : Simon Chen\n"
                    " @Email       : bafelem@gmail.com\n"
                    " @datetime    : ""%s" %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                    " @Description : Description\n"
                    " @FileName    : ""%s" % file_name +"\n"
                    "'''"
                    "\n"
        }
        return annotations[file_name[file_name.rfind('.') + 1:]]
