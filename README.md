# Quant Project on Nifty and Bank Nifty  

### Z-Score Analysis wrt to the baseline model 
The base model is implemented first, followed by the analysis of the Z-Score model. A comparison of profit and loss over the test data is presented in the file **`zscore_strategy.ipynb`**.  

#### Results (No Latency in Trading)  
| Strategy                         | Final PnL  | Abs PnL     | Sharpe (Annualized) | Max Drawdown | Num Points | Approx. Trades |
|----------------------------------|------------|-------------|----------------------|--------------|------------|----------------|
| Baseline (Sign Spread)           | 24.23      | 1268.59     | 1.73                 | -3.76        | 687,013    | 310            |
| Z-Score                          | 297.95     | 924.66      | 4.35                 | -0.98        | 687,013    | 5413           |

#### Results (1-Min Latency in Trading)  
| Strategy                    | Final PnL  | Abs PnL     | Sharpe (Annualized)  | Max Drawdown | Num Points | Approx. Trades |
|-----------------------------|------------|-------------|----------------------|--------------|------------|----------------|
| Baseline (Sign Spread)      | 24.23      | 1268.59     | 1.73                 | -3.76        | 687,013    | 310            |
| Z-Score                     | 114.76     | 889.90      | 5.07                 | -2.85        | 687,013    | 5400           |  

---

### ML Strategy  
The file **`ml_strategy_2.ipynb`** contains the machine learning model, which outperformed the other strategies mentioned above.  

#### Results (No Latency in Trading)  
| Test MSE | Sharpe Ratio | Max Drawdown |      Final PnL        |
|----------|--------------|--------------|-----------------------|
| 0.0020   | 66.32        | -0.17        | 38,593.15             |

#### Results (1-Min Latency in Trading)  
| Test MSE | Sharpe Ratio | Max Drawdown |      Final PnL        |
|----------|--------------|--------------|-----------------------|
| 0.0020   | 66.32        | -0.17        | 38,592.87             |


---

##### *Ankan Kar*  
