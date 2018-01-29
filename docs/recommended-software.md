BZS/Python: Recommended Development Software
===


Atom
---

* **Who needs it**: scriptwriters who don't have another IDE or programming editor.
* **What is it**: a fantastic text editor by GitHub, which has wonderful plugins available.
* **Where is it**: https://atom.io/
* **Why is it needed**: having a good programming interface is helpful, and Atom is among the most popular out there. Editing code in a text editor doesn't highlight syntax, debug, or allow you to actually test your script. Atom can do all of this, with plugins to enhance your experience!
* **Notes**: in addition to Atom's core editor, the following plugins are recommended:
    * highlight-selected: https://atom.io/packages/highlight-selected
    * language-vbscript: https://atom.io/packages/language-vbscript
    * minimap: https://atom.io/packages/minimap
        * minimap-find-and-replace: https://atom.io/packages/minimap-find-and-replace
        * minimap-highlight-selected: https://atom.io/packages/minimap-highlight-selected
    * script: https://atom.io/packages/script
    * todo-show: https://atom.io/packages/todo-show
    * atom-ide-ui: https://atom.io/packages/atom-ide-ui
        * ide-python: https://atom.io/packages/ide-python


GitHub Desktop
---

* **Who needs it**: Scriptwriters who plan to share their code with the collaborative.
* **What is it**: A version control system which allows scriptwriters to sync their code with others.
* **Where is it**: https://desktop.github.com/
* **Why is it needed**: emailing script files is cumbersome and challenging! Using GitHub allows users to sync their work with their partners in other counties.
* **Notes**: There is also a web application, which may work for casual scriptwriters, however, GitHub Desktop is recommended to scriptwriters who work on and test scripts outside of hackathon.


Python
---

* **Who needs it**: every scriptwriter!
* **What is it**: the programming language we're using!
* **Where is it**: https://www.python.org/ftp/python/3.6.4/python-3.6.4.exe (v3.6.4 x86)
* **Why is it needed**: because scriptwriters need access to a programming language!
* **Notes**:
    * We use the x86 version, instead of the default x64 version, because BlueZone typically registers bzwhll.dll in 32 bit mode, and it's easier to maintain compatibility with this. Some scripts might not test well in x64 bit mode.
    * It's recommended that Python be installed with administrative privileges. *This way you can easily add Python to PATH by checking the box in the installer.*


wxFormBuilder
---

* **Who needs it**: Scriptwriters who want to build their own custom dialogs.
* **What is it**: A drag-and-drop dialog editor capable of exporting Python dialog code.
* **Where is it**: https://sourceforge.net/projects/wxformbuilder/
* **Why is it needed**: BlueZone Script Host includes its own dialog editor (dlgedit.exe), and we need to provide a similar function.
* **Notes**: Over time, we may rely on helper functions to declare most dialogs, so this might not be necessary for most scriptwriters after a while. This document will be updated if that happens!
