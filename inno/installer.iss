[Setup]
AppName=BASIC Wrangler
AppVersion={#MyAppVersion}
DefaultDirName={userpf}\basicwrangler
DefaultGroupName=BASIC Wrangler
UninstallDisplayIcon={app}\bw.exe
Compression=lzma/ultra64
LZMAUseSeparateProcess=yes
LZMANumFastBytes=128
LZMADictionarySize=102400
SolidCompression=true
OutputDir=..\dist
InternalCompressLevel=ultra64
OutputBaseFilename=BASIC-Wrangler-{#MyAppVersion}-setup
VersionInfoVersion={#MyAppVersion}
VersionInfoTextVersion={#MyAppVersion}
VersionInfoCopyright=2020, pahandav
VersionInfoProductName={#MyAppVersion}
VersionInfoProductVersion={#MyAppVersion}
AppCopyright=2019, pahandav
AppVerName={#MyAppVersion}
LicenseFile=..\LICENSE
AppPublisher=pahandav
UninstallDisplayName=BASIC Wrangler
SetupIconFile=..\src\basicwrangler\icon\program_icon.ico

[Files]
Source: ..\dist\bw\*.*; DestDir: {app}; Flags: recursesubdirs
Source: ..\README.pdf; DestDir: {app}; Flags: isreadme; Tasks: 
Source: ..\CHANGELOG.pdf; DestDir: {app}
Source: ..\docs\Manual.pdf; DestDir: {app}\docs

[Icons]
Name: {group}\BASIC Wrangler; Filename: {app}\bw.exe
Name: {group}\Readme; Filename: {app}\README.pdf
Name: {group}\Changelog; Filename: {app}\CHANGELOG.pdf
Name: {group}\Manual; Filename: {app}\docs\Manual.pdf
Name: {commondesktop}\BASIC Wrangler; Filename: {app}\bw.exe; Tasks: 

[UninstallDelete]
Name: {app}\logs; Type: filesandordirs

[Tasks]
Name: modifypath; Description: Add application directory to your environmental path

[Code]
const
    ModPathName = 'modifypath';
    ModPathType = 'user';

function ModPathDir(): TArrayOfString;
begin
    setArrayLength(Result, 1)
    Result[0] := ExpandConstant('{app}');
end;
#include "modpath.iss"

[Run]
Filename: {sys}\compact.exe; Parameters: /c /s /a /i /exe:lzx *.*; WorkingDir: {app}; Flags: postinstall runhidden runascurrentuser; MinVersion: 0,10.0; Description: Compress application directory with NTFS Compression
Filename: {sys}\compact.exe; Parameters: /c /s /a /i *.*; WorkingDir: {app}; Flags: postinstall runhidden runascurrentuser; Description: Compress application directory with NTFS Compression; OnlyBelowVersion: 0,10.0
