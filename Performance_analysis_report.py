'''Brief Report: Portfolio Analysis

1. Methodology

   a. Data Processing:

      Loaded trade data from TRADES_CopyTr_90D_ROI.csv.

      Parsed raw trade history into structured format.

      Categorized trades into long_open, long_close, short_open, short_close.

    b. Metrics Calculation:

       ROI: Total profit divided by total investment.

       PnL: Sum of realized profits.

       Sharpe Ratio: Mean return divided by standard deviation (0 if constant returns).

       MDD: Worst percentage decline from peak returns.

       Win Rate: Percentage of profitable trades.

    c. Ranking:

       Normalized metrics to [0, 1] range (higher MDD = penalized).
       Refereed weighted score:
       Score = ROI*0.3 + PnL*0.2 + Sharpe*0.25 + MDD*0.15 + WinRate*0.1.
       Ranked portfolios by score, top 20.

2.  Key Findings

    a. Top Portfolios: Identified top 20 portfolios with highest composite scores (top_20_portfolios.csv).

    b. Performance Trends:
        Top performers valued high ROI and risk-adjusted returns (Sharpe Ratio).
        Portfolios with less drawdowns performed better because of MDD normalization.

3.   Output files: 

    portfolio_metrics.csv: Contains all portfolios with computed metrics.
    top_20_portfolios.csv: Rankings of top 20 portfolios.'''
