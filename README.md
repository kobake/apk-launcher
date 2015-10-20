# apk-launcher
Force install and execute apk file on Android device by one command from PC.

## Usage
### Windows
```
apk_launcher.bat <apk file>
```

### Mac OS X
```
apk_launcher.sh <apk file>
```

## Demo
![demo](https://raw.githubusercontent.com/kobake/apk-launcher/master/screenshots/movie.gif)

## Requirements
- [JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
- [Android SDK](http://developer.android.com/sdk/index.html#Other) ... Install 2 packages below by SDK Manager.
  - Android SDK Platform-tools (adb command)
  - Android SDK Build-tools (aapt command)
- [Python 2.7](https://www.python.org/)

## [Appendix] Internal command usage
### Get package name of apk file
```
python apk_packagename.py <apk file>
```

### Get activity name of apk file
```
python apk_activityname.py <apk file>
```
