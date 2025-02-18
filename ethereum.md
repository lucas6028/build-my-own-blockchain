## 以太坊 Ethereum

### **什麼是以太坊？**  
以太坊是一個**去中心化、開源的區塊鏈平台**，使開發者能夠建立和部署**智能合約**以及**去中心化應用程式 (DApp)**。它由**Vitalik Buterin**於2013年提出，並於2015年啟動。與主要作為**數位貨幣**的比特幣不同，以太坊是一個**可編程區塊鏈**，它支持比單純的金融交易更為複雜的應用。

以太坊的原生加密貨幣是**以太幣 (ETH)**，用於支付以太坊網絡中的交易費用和計算能力。

---

### **以太坊與比特幣：主要區別**  

| 特徵          | 以太坊      | 比特幣     |
|--------------|------------|---------|
| **主要用途**   | 智能合約和DApp | 數位貨幣（儲值） |
| **推出年份**   | 2015年     | 2009年   |
| **創始人**     | Vitalik Buterin 及其他人 | 中本聰    |
| **共識機制**   | 權益證明 (PoS)（自合併以來） | 工作量證明 (PoW) |
| **區塊時間**   | 約12秒     | 約10分鐘 |
| **總供應量**   | 沒有固定上限 | 最多2100萬BTC |
| **智能合約**   | 是        | 否      |
| **應用案例**   | 去中心化金融 (DeFi)、NFT、DAO、遊戲等 | 數位貨幣、儲值、支付 |

--- 

## 智能合約 Smart Contracts

### **什麼是智能合約？**  
智能合約是一種**自我執行的合約**，存儲在區塊鏈上，合約的條款以**電腦程式碼**形式編寫。當預定的條件滿足時，這些合約會自動執行動作，無需像銀行或法律系統等中介機構的介入。

智能合約最早是在**以太坊**上引入的，但現在其他區塊鏈（例如，幣安智能鏈、Solana 和 Cardano）也支援智能合約。

---

### **智能合約如何運作**
1. **編寫合約**：開發者使用像是**Solidity（以太坊）**或**Rust（Solana）**等程式語言編寫智能合約。
2. **部署到區塊鏈**：智能合約部署到區塊鏈，這樣它就變得**不可更改**（不能修改）。
3. **執行合約**：當用戶與合約互動（例如，發送ETH）時，合約會自動檢查條件是否滿足。
4. **記錄結果**：如果條件符合，合約會執行並將交易記錄到區塊鏈上。

範例：  
想像一台**自動販賣機**：
- 你插入錢（ETH）。
- 自動販賣機（智能合約）驗證金額。
- 如果金額正確，它會自動發放你選擇的商品。

---

### **智能合約的優點**
✅ **自動化** – 無需人工干預。  
✅ **去信任化** – 無需信任第三方（區塊鏈強制執行合約）。  
✅ **安全性** – 數據是不可更改且加密的。  
✅ **透明性** – 任何人都可以在區塊鏈上驗證合約邏輯。  
✅ **效率** – 比傳統法律合約更快且更便宜。

---

### **現實世界應用案例**
🔹 **去中心化金融 (DeFi)** – 不通過銀行進行借貸、交易。  
🔹 **NFT（非同質化代幣）** – 擁有數位藝術、音樂和收藏品。  
🔹 **DAO（去中心化自治組織）** – 基於區塊鏈的治理。  
🔹 **遊戲** – 像Axie Infinity這樣的「玩賺遊戲」。  
🔹 **供應鏈** – 自動化物流和支付。

--- 

## 以太坊的區塊鏈

### **以太坊的區塊鏈與比特幣的區塊鏈**

| 特徵            | **以太坊區塊鏈**         | **比特幣區塊鏈**       |
|---------------|-----------------|-----------------|
| **用途**        | 支援**智能合約與DApp**    | 主要聚焦於**安全交易與儲值** |
| **共識機制**     | **權益證明 (PoS)**（自2022年合併以來） | **工作量證明 (PoW)** |
| **區塊時間**     | 約12秒             | 約10分鐘           |
| **擴展性**       | 正在研究**Layer-2 解決方案**（樂觀滾動、zk滾動） | **有限**，無離鏈解決方案（例如，閃電網絡） |
| **交易費用**     | **Gas費用**，依據網絡需求波動 | **固定區塊大小與費用隨擁擠程度波動** |
| **供應上限**     | 沒有固定上限（但EIP-1559會燒毀ETH以減少供應） | 最大供應量為**2100萬BTC** |
| **靈活性**       | **圖靈完備**（能執行複雜的計算） | **有限的腳本語言**（僅限於交易） |

---

### **主要區別與運作方式**

1. **以太坊是可編程的**  
   - 比特幣的區塊鏈主要用於**安全支付**，並作為**數位黃金**。  
   - 以太坊則允許開發者構建**智能合約與DApp**，並支持**DeFi、NFT和DAO**等應用。  

2. **共識機制**  
   - 比特幣**使用工作量證明（PoW）**，需要礦工解決複雜的難題，消耗大量能源。  
   - 以太坊則**於2022年轉向權益證明（PoS）**，使其變得更加**節能且可擴展**。  

3. **以太坊擁有智能合約與Gas費用**  
   - 以太坊的**Gas費用**以**ETH**支付，並根據網絡需求變動。  
   - 比特幣則有**固定區塊大小**，這使得它在執行複雜應用時更慢且不太靈活。  

