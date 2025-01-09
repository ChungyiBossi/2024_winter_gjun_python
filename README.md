## CMD 指令
### 第一次讓本地與雲端連線
> git remote add origin https://github.com/ChungyiBossi/202024_winter_gjun_python.git

> git branch -M main

### 後續本地與雲端同步
* 本地同步至雲端
    > git push -u origin main
* 雲端檔案下載並同步至本地
    > git pull

### 其他主機下載雲端檔案
> git clone 你的雲端repository網址
如果是用clone下載，本地存檔將預設remote為此github repo。