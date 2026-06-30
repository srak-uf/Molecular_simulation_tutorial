# Linuxチュートリアル
- 参考: [TSUBAME講習会](https://www.t4.gsic.titech.ac.jp/sites/default/files/2024-04/T4_seminar_Linux_0.pdf)
- Linux基礎
  - 基礎コマンド
    - cd
    - ls
      - -l , -lah
      - permission
    - rm
    - mv
    - pwd
    - cat
    - vim, vi
    - history
  - vim : vim -p
    - i
    - y
    - p
    - esc
    - :q, :q!, :qa
    - :w
    - :wq 
  - alias
  - .bashrc
  - PATH
  - 改行コード

<br>
</br>  

## 最低限のコマンドを学ぶチュートリアル
### やること
- toolsフォルダの中にある解析コード（*.py）を~/analysisに入れる
- コマンドとして実行できるように権限設定する
- ~/analysisのPATHを通す、./bashrcで環境変数のPATHをupdateする
### 嬉しいこと
- 自作のスクリプトをどこのディレクトリにいても実行できるようになる
### 実施手順
1. Terminal (WSL) を起動
2. 現在のディレクトリの位置を知る
    ```
    pwd
    ```
    - pwd: 自分が今何処にいるのかを表示するコマンド
    - 出力例: /Users/srak/ : ディレクトリの階層を示す
    - TerminalにUser名の横に`~`と表示されている。
      - `~`: ホームディレクトリ = 今回pwdで示された階層
3. 解析コード`view.py`と`aseconvert.py`を入れるanalysisフォルダを作る
   - ダウンロード: {download}`view.py <codes/view.py>`, {download}`aseconvert.py <codes/aseconvert.py>`
    ```
    mkdir analysis
    ```
4. analysisフォルダにファイルをコピーする  
    - linuxコマンドを利用
      ```
      cp [ファイルのPATH]  ./analysis
      ```
      - `cp` : copyコマンド  
         `cp [コピーしたいファイル] [コピーしたいディレクトリ or コピー後のファイル名]`
      - `mv` : moveコマンド, cpはコピーペーストだが、mvはファイル or ディレクトリ移動
      - `. ` : 現在のディレクトリを意味, i.e., ./analysis = [現在のディレクトリ]/analysis
      - `..` : 一つ上の階層のディレクトリ
      - ファイルのPATHの知り方
          1. ファイルのあるディレクトリでTerminalを開く  
             - Windows  
                Shift + 右クリック → Terminalを開く or Linuxシェルを開く（環境によっては自分の開きたいWSL環境が起動できないかも）  
             - Mac  
                Finderの下に表示されているPath Barからスクリプトが入っているフォルダを右クリック → New Terminal at Folder
          2. 以下のコマンドを実行してフルパス（ex. /Users/username/hoge/fuga/view.py）をコピー
              ```
              ls `pwd`/*  
              ```
              - \` `command` \`: `command`の実行結果を文字列として出力
              - ls: ファイルの一覧を表示
              - \*: 全ての文字列に対応  
              &rarr; 以上まとめて、`ls [現在のディレクトリのPATH]/[全てのファイル]`のように処理されている
              > `ls *py`だとファイル名が「py」で終わるもののみ表示される  
              > `ls view*`だとファイル名が「view」から始まるもののみ表示される
    - 他のやり方：Windows → `explorer.exe .`, Mac → `open .`でそれぞれExplorer, Finderを開きファイルをコピペ
5. コピペできたかlsコマンドで確認
   ```
   ls ./analysis
   ```
   - view.py と aseconvert.pyが表示されていればOK
6. Terminalでanalysisディレクトリに移動
   ```
   cd ./analysis
   pwd  #確認
   ```
   - `cd`: Change directory, `cd [hoge]`でhogeディレクトリに移動する
7. ファイルを実行してみる
   ```
   ./view.py -h
   ```
   - ファイルPATHを最初に打つことで実行される（-hはview.pyでヘルプ表示するコマンド）
   - **"permission denied"と表示されたら以下を実行。権限の設定を変更する必要あり。**
8. ファイルの読み書き実行権限をチェック
   ```
   ls -lh *
   ```
   ![alt text](./images/chmod.png)  
   - 少なくとも所有ユーザーが実行権限を持っていることが必要
9. 実行権限の変更
   ```
   chmod 755 *
   ```
   - 755は、所有者 (7) 、グループ (5) 、その他のユーザー (5) に対するアクセス権を表現する
      0 – (権限なし)  
      1 x (実行可)  
      2 w (書き込み可)  
      3 1+2  
      4 r (読み込み可)  
      5 1+4  
      6 2+4  
      7 1+2+4  
10. 気を取り直して実行
    ```
    ./view.py -h
    ```
    これでも以下のようなエラーが出るはず  
    > ./view.py: line 1: from: command not found  
    > ./view.py: line 2: from: command not found ...   

    原因はpythonで実行して欲しいのに、Terminal用のプログラミング言語（bash or zsh）が実行されているから。  
    &rarr; Pythonで実行してもらえるようにおまじないをスクリプトに追加する必要がある。
11. おまじないをvim（テキストをLinux上で編集するツール）で追加  
    基本的にはVSCodeで十分だが、Terminal上でさくっと編集したいときのために最低限覚えること推奨  
    ```
    vim view.py
    ```
    - `esc` : 待機モードに切替
    - `i` or `a` : **（待機モード時）入力モードに切替**
    - `:q!` : （待機モード時）廃棄終了
    - `:w` : （待機モード時）上書き保存
    - `:wq` : **（待機モード時）保存して終了** 
    - `yy` : （待機モード時）行コピー
    - `dd` : （待機モード時）行切り取り
    - `p` : （待機モード時）ペースト

    上記コマンドを用いて以下が先頭行になるように編集  
    > #!/usr/bin/env python
    上記の太字コマンドを使えば編集・保存できる。  
12. ファイルがちゃんと編集されたか確認  
    ```
    cat ./view.py
    ```
    - `cat` : ファイルの中身を表示
13. 満を持して実行  
    ```
    ./view.py -h
    ```
    help表示がされたらOK  
    - 注意：今回作成したconda仮想環境mdで実行していること
14. 他のディレクトリで`view.py`コマンドだけで実行できるようにする  
    現在のままだと、view.pyを実行するときにフルパスを明記する必要がある`/Users/srak/analysis/view.py ....`
    1. analysisフォルダにPATHを通す
       1. 環境変数**PATH**に設定する。
          ```
          export PATH=$PATH:[type full path of analysis directory]
          # ex. export PATH=$PATH:/Users/srak/analysis
          ```
          - `export` で 上記のように指定すると環境変数PATHにanalysisディレクトリが追加される  
          - $PATH のように $を先頭につけることで、変数という意になる
          - 変数PATHに書かれたディレクトリがコマンドを探すときの対象となる
       2. 別のディレクトリにcdで移動しても以下のようにview.pyを実行できるようになる
          ```
          view.py -h
          ```
    2.  Terminal起動時に自動でPATHが通るようにする  
        毎回PATHを指定するのは面倒なので、自動で~/analysisディレクトリがPATHに追加されるようにする  
        1. Terminalのシェル言語がbashのときは~/.bashrc, zshのときは~/.zshrcがTerminal起動時に読み込まれる。  
           ここに上記で行った`export PATH=$PATH:[type full path of analysis directory]`を追記する。
        2. Terminalを再起動して、`view.py -h`が使えるかチェック

### 実行チェック
- 02_Linux演習/practiceでTerminalを起動（Finderの下に表示されているPath Barからスクリプトが入っているフォルダを右クリック→ New Terminal at Folderが楽）し、view.pyを以下のように実行。 
  ```
  view.py -pos argon.xyz
  ```
  - -pos の後ろに開きたいファイルを指定する。（これはview.py -hでHelpを表示すれば書いてある）  
- 02_Linux演習ディレクトリのaseconvert.pyについても同様に設定する。  
  計算化学の構造ファイルをASEを用いて変換するツール。  
  ```
  # example
  aseconvert.py -pos argon.xyz -o argon.cif
  ```  
  のようにxyzファイル &rarr; cifファイルを変換できる。VASP用のPOSCARなどなども対応。
## おまけTips
- 長いコマンドを省略したいとき &rarr; `alias`
- OSごとにテキストファイルの改行の取り扱いが異なる。
  - Windowsで編集したファイルがWindows仕様の改行コードになっているとLinuxで使えない場合がある。
  - VSCodeの右下にCRLF (Linux), CR (Mac), LF (CRLF) のいずれかが表示されているはず。VSCodeから変更できる。
- bash/zshではfor, if, arrayも使える
