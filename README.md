# DjangoForFun

## 注意事項
1. 請pull dev的branch然後去開發, 若要commit或merge也都到這一條branch, 若碰到merge有衝突, 請在local去pull另一條最新版的dev再去做merge
2. 在commit時, 請先確認commit的是自己有編輯過的程式或設定檔, 有些自動產生的設定檔, 盡量不要commit到dev裡
3. 在Cloud9上編輯程式, 可先參考此文件環境之建置https://docs.google.com/document/d/10XK_oW1Z59JqAtlvjy7bSivf1SGepqcr8QM6v2o-LbQ/edit?usp=sharing
4. 若Cloud9在docker相關操作有發生no space left on device, 可透過docker rmi -f IMAGE_ID, 刪掉一些不必要的docker image
5. 執行src資料夾內mange.py檔, 透過以下command => python mange.py runserver 0.0.0.0:8000, 就可以運行此Web application
6. src為web application的root
7. 循序圖
8. 在寫view.py裡的function時, 可以想一下如何寫個單元測試, 驗證一下輸入/輸出參數
9. 目前先這樣, 之後會再補充

```seq
User->urls.py: Tap button
Note right of urls.py: Mapping action's name\nand url
urls.py->view.py: Find the specific function
view.py-->>User: Return value
```
