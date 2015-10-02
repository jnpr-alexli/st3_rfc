import os.path
import sublime_plugin
import re

class RFCHighlighter(sublime_plugin.EventListener):
    def on_load(self, view):
        if (re.match("rfc\d+\.txt", os.path.basename(view.file_name()))):
            view.set_syntax_file("Packages/RFC/rfc.tmLanguage")