[Setup]
AppName=BASIC Wrangler
AppVersion=0.05.0
DefaultDirName={userpf}\basicwrangler
DefaultGroupName=BASIC Wrangler
UninstallDisplayIcon={app}\bw.exe
Compression=lzma/ultra64
LZMAUseSeparateProcess=yes
LZMANumFastBytes=128
LZMADictionarySize=102400
SolidCompression=true
OutputDir=..\dist
; "ArchitecturesAllowed=x64" specifies that Setup cannot run on
; anything but x64.
ArchitecturesAllowed=x64
; "ArchitecturesInstallIn64BitMode=x64" requests that the install be
; done in "64-bit mode" on x64, meaning it should use the native
; 64-bit Program Files directory and the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64
InternalCompressLevel=ultra64
OutputBaseFilename=BASIC-Wrangler-0.05.0-setup
VersionInfoVersion=0.05.0
VersionInfoTextVersion=0.05.0
VersionInfoCopyright=2020, pahandav
VersionInfoProductName=0.05.0
VersionInfoProductVersion=0.05.0
AppCopyright=2019, pahandav
AppVerName=0.05.0
LicenseFile=..\LICENSE
AppPublisher=pahandav
UninstallDisplayName=BASIC Wrangler
SetupIconFile=..\icon\program_icon.ico

[Files]
Source: ..\dist\bw\*.*; DestDir: {app}; Flags: recursesubdirs
Source: ..\README-PDF.pdf; DestDir: {app}; DestName: README.pdf; Flags: isreadme; Tasks: 
Source: ..\CHANGELOG.pdf; DestDir: {app}
Source: ..\docs\Manual.pdf; DestDir: {app}\docs

[Icons]
Name: {group}\BASIC Wrangler; Filename: {app}\bw.exe
Name: {group}\Readme; Filename: {app}\README.pdf
Name: {group}\Changelog; Filename: {app}\CHANGELOG.pdf
Name: {group}\Manual; Filename: {app}\docs\Manual.pdf
Name: {commondesktop}\BASIC Wrangler; Filename: {app}\bw.exe; Tasks: 

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
