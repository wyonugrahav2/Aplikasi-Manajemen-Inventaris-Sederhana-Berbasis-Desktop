; Inno Setup Script untuk Aplikasi Manajemen Inventaris
; File ini digunakan untuk membuat installer Windows (.exe)
;
; Cara menggunakan:
; 1. Install Inno Setup dari https://jrsoftware.org/isinfo.php
; 2. Buka file ini dengan Inno Setup Compiler
; 3. Klik "Compile" untuk membuat installer
;
; Author: Proyek Akhir - Teknik Informatika

#define MyAppName "Aplikasi Manajemen Inventaris"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Teknik Informatika"
#define MyAppURL "https://github.com/yourusername/inventory-app"
#define MyAppExeName "InventarisApp.exe"

[Setup]
; NOTE: Ganti AppId dengan GUID unik Anda
; Generate GUID di: https://www.guidgenerator.com/
AppId={{12345678-1234-1234-1234-123456789012}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=LICENSE
InfoBeforeFile=README.md
OutputDir=installer_output
OutputBaseFilename=InventarisApp_Setup_v{#MyAppVersion}
SetupIconFile=
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "indonesian"; MessagesFile: "compiler:Languages\Indonesian.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 6.1; Check: not IsAdminInstallMode

[Files]
; File executable utama
Source: "dist\InventarisApp\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
; Semua file di folder dist\InventarisApp
Source: "dist\InventarisApp\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Dokumentasi
Source: "README.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "USER_GUIDE.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "LICENSE"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\User Guide"; Filename: "{app}\USER_GUIDE.md"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
// Custom code untuk installer (optional)
procedure InitializeWizard();
begin
  // Kode inisialisasi wizard
end;
