# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main_gui.py'],
             pathex=['.'],
             binaries=[],
             # 将 config.json 和图标文件作为数据文件包含进来
             datas=[('config.json', '.'), ('document-import-16-svgrepo-com.ico', '.')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='文档内容抓取器',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          # 对于GUI应用，设置为 True 来隐藏控制台窗口
          console=False,
          # 设置应用程序的图标
          icon='document-import-16-svgrepo-com.ico'
          )