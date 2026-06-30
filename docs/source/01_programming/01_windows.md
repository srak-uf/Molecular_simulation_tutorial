# Windows設定
## WSLのインストール
1. Open "Windows Power Shell" or "Terminal" as Administrator.
2. Type `wsl --set-default-version 2` (for safe)
3. Type `wsl --install -d Ubuntu`.
4. After installation is done, open `Ubuntu` in Application.
Windows Terminalがおすすめ
## WSL Tips
- Windows側のディレクトリ `/mnt/c/` は、ファイルの入出力が**非常に遅い**
  - 計算はLinux側のDirectoryで実行する
- Windows Terminalの活用
- Ctrl + Shift + C でコピペ、Ctrl + Shift + Vでペーストできるように設定可
- WSLからExploreを開くときは、`explorer.exe .`で現在のディレクトリをExplorerで開ける
- Ubuntu側のディレクトリのショートカットを作っておくと楽
  - `explorer.exe .`でExplorerを開いて、ショートカットを作りましょう
