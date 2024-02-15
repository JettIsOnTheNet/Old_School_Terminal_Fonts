#/bin/sh
for i in $(ls ttf/*.ttf); do
    fontforge --script font-patcher --complete --progress --out patched/ $i
done
