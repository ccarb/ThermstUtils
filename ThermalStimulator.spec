# -*- mode: python ; coding: utf-8 -*-
# if using python 3.8 use pyinstaller development version

block_cipher = None
added_files = [
    ('json\\commands.json','json\\'),
    ('json\\status_descriptions.json','json\\'),
    ('docs\\Manual.pdf', 'docs\\'),
    ('examples\\exampleParadigm.m', 'examples\\'),
    ('examples\\lib.m', 'examples\\')
]


a = Analysis(['main.py'],
             pathex=['D:\\Users\\Wider\\Visual Studio\\ThermstUtils\\'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Thermal Stimulator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='resources\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Thermal Stimulator')
