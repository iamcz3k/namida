from pathlib import Path
import os
import re

root = Path(os.environ.get("LACZEK_SOURCE", "."))
p = root / "pubspec.yaml"
s = p.read_text()
s = re.sub(r"^version:\s*.*$", "version: 1.0.0+1", s, flags=re.M)
s = s.replace("  name: Namida\n", "  name: LACZEK Player\n")
s = s.replace("  publisher_display_name: namidaco", "  publisher_display_name: LACZEK")
s = s.replace("  identity_name: com.msob7y.namida", "  identity_name: com.v3x.laczekplayer")
s = s.replace("  name: Namida\n  publisher: MSOB7Y", "  name: LACZEK Player\n  publisher: LACZEK")
p.write_text(s)

p = root / "android/app/build.gradle.kts"
s = p.read_text()
s = s.replace('namespace = "com.msob7y.namida"', 'namespace = "com.v3x.laczekplayer"')
s = s.replace('applicationId = "com.msob7y.namida"', 'applicationId = "com.v3x.laczekplayer"')
s = s.replace('output.outputFileName = "namida-v\${versionName}\${abiText}.apk"', 'output.outputFileName = "LACZEKPlayer-\${versionName}\${abiText}.apk"')
p.write_text(s)

for p in [
    root / "android/app/src/main/AndroidManifest.xml",
    root / "android/app/src/debug/AndroidManifest.xml",
    root / "android/app/src/profile/AndroidManifest.xml",
]:
    s = p.read_text()
    s = s.replace('package="com.msob7y.namida"', 'package="com.v3x.laczekplayer"')
    s = s.replace('android:label="Namida Shuffle"', 'android:label="LACZEK Player Shuffle"')
    s = s.replace('android:label="Namida"', 'android:label="LACZEK Player"')
    s = s.replace('com.msob7y.namida.', 'com.v3x.laczekplayer.')
    p.write_text(s)

for p in (root / "android").rglob("*.kt"):
    s = p.read_text()
    s = s.replace("package com.msob7y.namida", "package com.v3x.laczekplayer")
    p.write_text(s)

for p in root.rglob("*.dart"):
    if any(x in p.parts for x in [".git", "build"]):
        continue
    s = p.read_text()
    s = s.replace("androidNotificationChannelName: 'Namida'", "androidNotificationChannelName: 'LACZEK Player'")
    s = s.replace("androidNotificationChannelDescription: 'Namida Media Notification'", "androidNotificationChannelDescription: 'LACZEK Player Media Notification'")
    s = s.replace("https://github.com/namidaco/namida", "https://github.com/iamcz3k")
    s = s.replace("https://github.com/namidaco", "https://github.com/iamcz3k")
    s = s.replace("https://x.com/namidaco", "https://x.com/iam_czek")
    s = s.replace("https://twitter.com/namidaco", "https://x.com/iam_czek")
    s = s.replace("'namida.coo@gmail.com'", "'laczekrsa@proton.me'")
    p.write_text(s)

for p in (root / "android").rglob("*.xml"):
    s = p.read_text()
    s = s.replace(">Namida Shuffle<", ">LACZEK Player Shuffle<")
    s = s.replace(">Namida<", ">LACZEK Player<")
    p.write_text(s)
