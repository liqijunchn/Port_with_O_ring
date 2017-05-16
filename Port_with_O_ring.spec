# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\OneDrive\\Port_with_O_ring-master\\Port_with_O_ring.py'],
             pathex=['C:\\OneDrive\\Port_with_O_ring-master'],
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
          console=False ,
          icon = './jci.ico' )
