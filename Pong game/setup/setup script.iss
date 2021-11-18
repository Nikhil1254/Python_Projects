; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{04C891AA-7F8E-4C7B-8E34-05E4A987641E}
AppName=Pong
AppVersion=1.5
;AppVerName=Pong 1.5
AppPublisher=Nikhil Patil
AppPublisherURL=np52622@gmail.com
AppSupportURL=np52622@gmail.com
AppUpdatesURL=np52622@gmail.com
DefaultDirName={autopf}\Pong
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\setup
OutputBaseFilename=Pong setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\background.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\Hit_sound.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\score.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Nik\OneDrive\Desktop\Coding Stuff\Python\python projects\Pong game\time_counter.wav"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\Pong"; Filename: "{app}\main.exe"
Name: "{autodesktop}\Pong"; Filename: "{app}\main.exe"; Tasks: desktopicon   ; IconFilename:"{app}\icon.ico"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Pong}"; Flags: nowait postinstall skipifsilent

