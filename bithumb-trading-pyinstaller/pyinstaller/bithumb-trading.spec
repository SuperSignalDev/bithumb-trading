# This is the PyInstaller specification file for the Bithumb trading executable.

block_cipher = None

a = Analysis(['../src/bithumb-trading.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=['jwt', 'requests', 'uuid', 'hashlib', 'time', 'json', 'urllib.parse'],
             hookspath=[],
             hooksconfig={},
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
          name='bithumb-trading',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name='bithumb-trading')