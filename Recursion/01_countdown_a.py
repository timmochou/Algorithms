def countdown(i):
    print(i)
    if i <= 1: # Base Case: 當i 小於等於1時就結束遞迴
        return
    else: # Recursive Case
        countdown(i-1) # 否則用i-1呼叫countdown 
## 沒有設置結束會發生recursion error
countdown(3)
