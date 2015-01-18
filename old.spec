import sys

a = Analysis(['repl.py'],
             hiddenimports=[])
from kivy.tools.packaging.pyinstaller_hooks import install_hooks
install_hooks(globals())
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          # Static link the Visual C++ Redistributable DLLs if on Windows
          a.binaries + [('msvcp100.dll', 'C:\\Windows\\System32\\msvcp100.dll', 'BINARY'),
                        ('msvcr100.dll', 'C:\\Windows\\System32\\msvcr100.dll', 'BINARY')]
          if sys.platform == 'win32' else a.binaries,
          a.zipfiles,
          a.datas + [('elements.json',      'elements.json', 'DATA')],
          a.datas + [('calc.kv',      'calc.kv', 'DATA')],
          a.datas + [('up.png',      'up.png', 'DATA')],
          a.datas + [('down.png',      'down.png', 'DATA')],
          name=os.path.join('dist', 'calc' + ('.exe' if sys.platform == 'win32' else '')),
          debug=False,
          strip=None,
          upx=True,
          console=True,
          icon=None)
