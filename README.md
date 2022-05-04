# 台大資訊系統訓練班 356期 Python 機器學習課程(IMLP356)

> IMLP356_repository

## github環境
### 1. Markdown語法
[Markdown Cheatsheet 中文版](https://gist.github.com/billy3321/1001749662c370887c63bb30f26c9e6e#links)
### 2.Git 用法
[初始設定](https://ithelp.ithome.com.tw/articles/10240965)

[Git bash 基本操作](http://yhhuang1966.blogspot.com/2020/01/git-git-bash.html)
| Git常用指令	| 說明 |
|----|---|
| git init | 將目前的目錄初始化為 Git 目錄, 建立本地儲存庫|
| git config	| 設定或檢視 Git 設定檔資訊|
| git add |	 將檔案加入 Git 暫存區|
| git rm	| 將檔案移出 Git 暫存區|
| git status |	 顯示 Git 狀態|
| git commit 	| 將暫存區的檔案提交至儲存庫納入版本控制|
| git log	| 顯示過去歷次的版本異動|
| git reflog	| 顯示完整的版本異動歷史紀錄|
| git show	| 顯示指定版本的異動內容|
| git branch	| 建立一個新分支 (branch)|
| git checkout	| 取出分支內容還原為工作目錄|
| git merge	| 合併分支|
| git reset	| 重設某一版本|
| git clone	|從遠端儲存庫 (GitHub 或 Bitbucket) 複製副本至本地儲存庫|
| git push	| 將本地儲存庫內容推送到遠端儲存庫|
| git pull	| 將遠端儲存庫拉回合併更新到本地儲存庫|

Git Bash 是 Windows 版的 Git 模擬器, 可使用 Linux 指令操作 Window 的檔案系統, 常用的 Linux 與 Windows 檔案管理指令對照如下表 :

 |Linux 命令	| Windows 命令	| 說明|
 |----|----|----|
 |pwd	| cd	| 顯示幕前目錄|
 |ls -al	| dir	| 顯示目前目錄下的檔案與子目錄列表|
 |mkdir tmp	| md tmp	| 建立子目錄 tmp|
 |rm -r tmp	 |rd tmp	| 刪除子目錄 tmp|
 |cd tmp	| cd tmp	| 切換至子目錄 tmp|
 |cd ..|	 cd .. 	| 切換至上一層目錄|
 |touch test.txt	| copy nul > test.txt	| 建立空白文字檔案|
 |cat |file/more	| type file	| 顯示檔案內容|
 |rm file	| del file	| 刪除檔案 file|
 |mv file1 file2	| ren file1 file2	| 將檔案 file1 更名為 file2|
 |cp  file1 file2	| copy file1 file2	| 複製檔案 file1 為 file2|
 |date	| date	| 顯示日期 (Linux 含時間)|
 |clear	| cls	| 清除螢幕|


>注意, 在 Git Bash 視窗中存取檔案系統時, 路徑分隔字元必須照 Linux 用法使用右斜線  (slash) "/", 不可用 Windows 的倒斜線 "\"
