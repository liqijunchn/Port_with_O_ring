# -*- mode: python -*-

block_cipher = None


a = Analysis(['D:\\OneDrive\\GitHub\\Port_with_O_ring\\Port_with_O_ring.py'],
             pathex=['D:\\OneDrive\\GitHub\\Port_with_O_ring'],
             binaries=[],
             datas=[('threaded port with o ring.db','.'),('port.png','.'),('jci.ico','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Port_with_O_ring',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon = './jci.ico' )
