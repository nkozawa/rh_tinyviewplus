# rh_tinyviewplus

[RotorHazard]:https://github.com/RotorHazard/RotorHazard
[TinyViewPlus]:https://github.com/t-asano/tinyviewplus
rh_tinyviewplus is one of [RotorHazard] plugin to support [TinyViewPlus].
This plugin adds TinyViewPlus LAP from RotorHazard when Tinyviewplus fails to read AR markers!

## Install
- Make directory "rh_tinyviewplus" under "plugins" directory. Typical sample command is like this `mkdir RotorHazard/src/server/plugins/rh_tinyviewplus`.
- Copy files __init__.py and manufest to under the directory.
- Install python-osc package to python virtual environment. Typical commands example are:
```
cd
source ./.venv/bin/activate
pip3 install python-osc
```
> If you are not sure which virtual environment is used to your RotorHazard, please try `systemctl cat rotorhazard`.

## TinyViewPlus IP Address
You need to tell IP Address of TinyViewPlus to rh_tinyviewplus plugin. There two methods.
1. Modify `__init__.py` file. Just edit `ipAddress = "127.0.0.1"`.
2. Create "tvpIPAddress.ini" file to under user home directy. It might be '/home/pi'. 'tvpIPAddress.ini' just need to contain IP Address, nothing else.

After modify IP Address, you need to restart RotorHazard.

## Test
Run Rotorhazard and TinyViewPlus. Both must be in race mode. If add a lap on RotorHazrd (either manually or VTX sensing), TinyViewPlus would also recognizes the lap.
