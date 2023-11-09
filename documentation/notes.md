Notes
-- For Cells 91-94 we found that between 74-77% of trading days have a spread of 200 points in either direction. When we really  start to dive deeper into this we will want to examine a few more things
    * We know the additional 30% comes from expaning from (-100,100) to (-200,200) but what we want to know is if more of them go to the negative or positive direction and the reason is this means we would have to make a bet in 4 bands in order to fulfill our ~75% probability bet, however the prices for those bands would total to over definitely over $0.50 meaning we would take a risk and over $1 for sure depending on time of day the bets are placed meaning if we evenly distribute our bets, even if we did win on one we would lose on the other 3 and the losses in this case would result in a negative trading. So knowing direction would help us eliminate one trading band and only bet 3 as long as our probability still remains high, hopefully over 65%
    * In additon to above we want to see during theses same dates what the high low spread was as well to see if there was a correlation between that to give us more confidence to make these bets, if yes then it would be safe to bet all 4 bands and have timely exits, if not then we would need to practice caution. 
    * Also for examples today close was 14823 so a 150 increase would mean I would still have to only bet in one band and now we see that (-150,150) produces 67% probability for the past 5 years. and 61% for the past 200 trading days. So this will def help when looking at eliminating 1 of the 4 bands
    
-- For Looking at Days of the Week this is a quick glance that I got from these visualizations
    * Monday trends negatively heavily betten Open and Close
    * Thursday is the most volatile trading day in terms of spreads
    * Tuesday is the safest day to bet upwards
    * Friday is the safest day to bet within the same range in which it open
    
 ## Things to Watch
 * We one hot encoded the day of the week feature. if we learn it isnt a valuable feature then we will reload the data and drop that column from the dataset compeltely
 
 
 ## Things to Try
We are going to move further with the datast and features we hvae to predict price. However, as we complete our first models we will get more intraday data such as price at every hour, volume of trades at every hour, and other stock indicators that track intraday movement to give our models more information.