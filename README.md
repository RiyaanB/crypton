# crypton
Our attempt of forecasting Bitcoin Prices for the Ultimate Cryptocurrency Challenge by Unifynd
Authors: Adhyyan Sekhsaria and Riyaan Bakhda

Our idea was supposed to extend the idea of sentimental analysis. Sentimental analysis is the analysis of tweets, articles, online posts and other such factor which could have a impact on BTC prices. However, this analysis only provides infomration about the direciton and magnitude of the sentiments of the factor. With many different factors with each having impacts on different levels it would be inaccurate to choose the weightages by hand. 

Our algorithm:
1) Reduce noise and approximate price/time graph of BTC into linear segments
2) Make a system of linear equations for each line segment depending on the number and type of factors on that segment. Accounting for time lag. (Assuming that each factor has a impact linearly additive impact)
3) Use gradient descent to give each factor a weightage. Solving for least squares error.
4) Calculate prediction of the BTC in the short term.
