# Build My Own Blockchain

Tutorial URL: [Learn Blockchains by Building One](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)

## 比特幣介紹

比特幣的技術基於區塊鏈和去中心化網絡的概念，這些技術共同確保了比特幣的安全性、透明性和抗篡改性。以下是比特幣技術的幾個關鍵組成部分：

1. **區塊鏈（Blockchain）**：
   - 區塊鏈是一種分佈式帳本技術，所有比特幣交易都被記錄在一串連續的區塊中。每個區塊包含一組交易數據、時間戳和前一個區塊的哈希值，這樣每個區塊都依賴於前一個區塊，形成鏈式結構。
   - 這種結構確保了數據的不可篡改性，因為如果有人試圖修改某個區塊的內容，必須同時修改後續所有區塊，這在計算上是幾乎不可能的。

2. **去中心化網絡**：
   - 比特幣運行在一個分佈式的點對點網絡中，這意味著沒有中央伺服器或管理機構。所有的用戶（或節點）都可以參與區塊鏈的維護，並且每個節點都持有完整的區塊鏈副本。
   - 當有新交易發生時，這些交易會被廣播到整個網絡，並由網絡中的礦工進行驗證。

3. **挖礦（Mining）**：
   - 挖礦是比特幣創造和交易驗證的過程。礦工使用專門的計算機硬體來解決複雜的數學問題（例如SHA-256哈希函數）。
   - 成功解決問題的礦工會將新交易打包到一個新的區塊中，然後將其添加到區塊鏈上。作為獎勵，他們會獲得新生成的比特幣和交易手續費。

4. **共識機制（Consensus Mechanism）**：
   - 比特幣使用工作量證明（Proof of Work, PoW）作為其共識機制。這要求礦工在挖礦過程中投入計算能力，以確保只有經過驗證的交易才能被添加到區塊鏈上。
   - 這種機制能防止雙重支付和其他欺詐行為，因為攻擊者需要控制超過50%的計算能力才能影響網絡。

5. **私鑰和公鑰加密**：
   - 每個比特幣用戶都有一對密鑰：公鑰和私鑰。公鑰可以被用作比特幣地址，其他人可以用它來向你發送比特幣。私鑰則用於簽署交易，證明你對該比特幣的所有權。
   - 私鑰必須保密，因為擁有私鑰的人可以控制與該私鑰相關聯的比特幣。

6. **交易流程**：
   - 用戶發起交易時，會將交易資訊（如發送者的公鑰、接收者的公鑰和轉賬的比特幣數量）簽名並廣播到網絡中。
   - 礦工驗證這些交易的有效性，確保發送者有足夠的比特幣並且交易未被重複使用。有效的交易將被打包到區塊中並添加到區塊鏈上。

