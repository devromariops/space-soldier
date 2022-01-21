# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

import os
import sys


explosions_files = os.path.join('assets', 'sprites', 'enemy-explosion', '*.png')
explosions_path = os.path.join('assets', 'sprites', 'enemy-explosion')

aim_files = os.path.join('assets', 'sprites', 'aim', '*.png')
aim_path = os.path.join('assets', 'sprites', 'aim')

font_files = os.path.join('assets', 'fonts', 'Alien-Eclipse.ttf')
fonts_path = os.path.join('assets', 'fonts')

stars_nebulae_files =  os.path.join('assets', 'sprites', 'stars-nebulae', '*.png')
stars_nebulae_path = os.path.join('assets', 'sprites', 'stars-nebulae')

space_ships_files = os.path.join('assets', 'sprites', 'space-ships', '*.png')
space_ships_path = os.path.join('assets', 'sprites', 'space-ships')

sounds_files = os.path.join('assets', 'sounds', '*.mp3')
sounds_path = os.path.join('assets', 'sounds')

space_bullets_files = os.path.join('assets', 'sprites', 'space-bullets', '*.png')
space_bullets_path = os.path.join('assets', 'sprites', 'space-bullets')


add_files = [(aim_files, aim_path),
             (font_files, fonts_path),
             (stars_nebulae_files, stars_nebulae_path),
             (space_ships_files, space_ships_path),
             (sounds_files, sounds_path),
             (space_bullets_files, space_bullets_path),
             (explosions_files, explosions_path),
             ('icone.ico', '.')]


a = Analysis(['space_soldier.py'],
             pathex=[],
             binaries=[],
             datas=add_files,
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='SPACE SOLDIER',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='icone.ico')
