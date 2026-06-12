[app]
title = Factorial Premium
package.name = factorialpremium
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0

requirements = python3,kivy

icon.filename = %(source.dir)s/icon.jpg

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license = True
