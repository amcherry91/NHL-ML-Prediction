# NHL Machine Learning Prediction Model

Algorithm using python and Tensorflow to predict NHL results using a linear regression model. The end-goal is to create an unsupervised neural network to train the AI and make predictions to enable greater accuracy for applications such as betting or NHL Fantasy teams.

 # Installation

See the [TensorFlow install guide](https://www.tensorflow.org/install) for the [pip package](https://www.tensorflow.org/install/pip). 

[Anaconda](https://www.anaconda.com/distribution/) was also used to create and manage the Tensorflow environment. When installing Anaconda, ensure that "Add Anaconda to my PATH environment variable" is __checked__

To install the required libraries to run the script enter the following into your python IDE terminal
```
pip install numpy
pip install pandas
pip install keras
pip install sklearn
pip install matplotlib
pip install seaborn
```


## Dataset
The dataset used was a cleaned version of the [NHL Game Data](https://www.kaggle.com/martinellis/nhl-game-data) provided by Martin Ellis on Kaggle.

The game.csv and game_teams_stats.csv were cleaned (some formatting errors are present in raw data) and combined into a single csv file in excel. The game.csv entries were doubled as the game_teams_stats.csv contains 2 rows per 1 game_id. This was done to ensure that both datasets matched (ie, there were 2 rows per match, 1 for away team stats and the 1 row for home team stats).

## Notes
Currently [APIs for NHL statistics](https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api) are not well documented however work is being done to improve this. As documentation and access to the API improves, this model will be updated to reflect those changes and improve the quality and reliability of the results.

