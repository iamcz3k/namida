from pathlib import Path
import os, re
root = Path(os.environ['LACZEK_SOURCE'])
def rw(rel, fn):
    p = root / rel
    if p.exists():
        s = p.read_text(encoding='utf-8')
        p.write_text(fn(s), encoding='utf-8')
rw('pubspec.yaml', lambda s: re.sub(r'^version:\s*.*$', 'version: 1.0.0+1', s, flags=re.M).replace('name: namida', 'name: laczek_player'))
rw('android/app/build.gradle.kts', lambda s: s.replace('namespace = "com.msob7y.namida"', 'namespace = "com.v3x.laczekplayer"').replace('applicationId = "com.msob7y.namida"', 'applicationId = "com.v3x.laczekplayer"').replace('namida-v${versionName}${abiText}.apk','LACZEKPlayer-${versionName}${abiText}.apk'))
for rel in ['android/app/src/main/AndroidManifest.xml','android/app/src/debug/AndroidManifest.xml','android/app/src/profile/AndroidManifest.xml']:
    rw(rel, lambda s: s.replace('package="com.msob7y.namida"','package="com.v3x.laczekplayer"').replace('android:label="Namida Shuffle"','android:label="LACZEK Player Shuffle"').replace('android:label="Namida"','android:label="LACZEK Player"').replace('com.msob7y.namida.','com.v3x.laczekplayer.'))
for p in (root/'android').rglob('*.kt'):
    p.write_text(p.read_text(encoding='utf-8').replace('package com.msob7y.namida','package com.v3x.laczekplayer'),encoding='utf-8')
for p in root.rglob('*.dart'):
    if '.git' in p.parts or 'build' in p.parts: continue
    s=p.read_text(encoding='utf-8').replace('Namida Media Notification','LACZEK Player Media Notification').replace("androidNotificationChannelName: 'Namida'","androidNotificationChannelName: 'LACZEK Player'").replace('https://github.com/namidaco/namida','https://github.com/iamcz3k').replace('https://github.com/namidaco','https://github.com/iamcz3k').replace('https://x.com/namidaco','https://x.com/iam_czek').replace('https://twitter.com/namidaco','https://x.com/iam_czek').replace('namida.coo@gmail.com','laczekrsa@proton.me')
    p.write_text(s,encoding='utf-8')
