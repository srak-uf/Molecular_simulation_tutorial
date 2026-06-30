# Python環境構築（condaのインストール）
> Windows用のcondaでは最新のMI・MD用Pythonライブラリが対応していないことが多い。  
> そのため、WindowsのCondaは用いずにWSLからLinux用のcondaを使えた方が良い。    
> \+ 商用ライセンスの回避
1. [Miniforge](https://github.com/conda-forge/miniforge)のインストーラーをダウンロード  
    基本的にはgithubのページに飛べばやり方は書いてあるはず。  
    Windows -> WSL, Mac -> Terminal.appを起動。   
    ```
    # Download some apps in apl folder 
    cd ~
    mkdir apl
    cd apl
    # download the installer
    # In pdf file, unintended space and line break is inserted!!! Be careful!!!
    # If some problems happen, please use the original .md file. 
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    # install
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```
    指示に従いEnterを押す, yes/noで回答
    > **注意点：ライセンス問題**  
    ライセンスの問題上、[Anacondaリポジトリ（defaultチャネル）](https://anaconda.org/anaconda)の商用利用は禁止されている。  
    そのため持続的な環境構築という点で、Anacondaは用いずにMiniconda（ミニマルなAnaconda, CLIベース）でdefaultチャネルを使わないことが推奨される。  
    Miniforgeは、デフォルトのチャネルがコミュニティベースの[conda-forgeリポジトリ](https://anaconda.org/conda-forge)（商用利用可能）のため、ライセンス面で安心して使える。  
    \+ 通常のconda（パッケージ管理ツール）に比べて、高速なmambaコマンドを使うことができる。

2. 仮想環境の構築
    無事にMiniforgeのインストールが済んだら、MD計算用の仮想環境をつくる。  
    インストールしたcondaが起動されて、Terminal上に(base)が表示されているかチェック。  
    （baseが表示されていなかったらTerminal開き直す）
    配布されたmd_***.ymlがあるディレクトリで以下のコマンドを実行。
    - Intel Mac user
        ```
        mamba env create -f md_intelmac.yml
        ```
    - Arm Mac user
        ```
        mamba env create -f md_osxarm64.yml
        ```
    - Linux or WSL user
        ```
        mamba env create -f md_linux.yml
        ```
    最後の方にdoneと表示されていたら無事仮想環境構築完了。

3. 仮想環境へ入る
    以下のコマンドを実行することで、今回構築した仮想環境（デフォルトの名前: md）を起動できる。  
    ```
    conda activate md
    ```

4. 動作確認
   配布されたview.py（toolsディレクトリ）とArgon.xyz（structuresディレクトリ）を同じディレクトリに入れて以下を実行。  
   ASEライブラリの分子構造描画が立ち上がることを確認。  
   Linux操作になれてなくてこのやり方が分からない人は02_Linuxで確認。  
   ```
   python3 view.py -pos Argon.xyz
   ```

5. 補足・注意事項
- 研究プロジェクトごとに仮想環境を構築して、プロジェクト-仮想環境を紐づけておくことを推奨
- ライブラリを追加する時は `conda install -c [channel名] [ライブラリ名]` よりも、`mamba install -c [channel名] [ライブラリ名]` の方が高速
- 一度立てたconda仮想環境にpipを使うのは出来るだけ避けた方がいい
