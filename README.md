# NHL Machine Learning Prediction Model

Algorithm using python and Tensorflow to predict NHL results using a linear regression model. The end-goal is to create an unsupervised neural network to train the AI and make predictions to enable greater accuracy for applications such as betting or NHL Fantasy teams.

 # Installation

See the [TensorFlow install guide](https://www.tensorflow.org/install) for the [pip package](https://www.tensorflow.org/install/pip). 

[Python 3.6](https://www.python.org/downloads/release/python-360/) is required for Tensorflow to work. __Note: Python 3.7 is not currently supported__

[Anaconda](https://www.anaconda.com/distribution/) was also used to create and manage the Tensorflow environment. When installing Anaconda, ensure that "Add Anaconda to my PATH environment variable" is __checked__

One you have downloaded and installed Tensorflow and Anaconda. Open a command terminal and create a new tensorflow environment using the following code
```
conda create -n tensor python=3.6
```

Then install the required libraries either in the the command terminal or the terminal in your IDE

```
pip install numpy
pip install pandas
pip install keras
pip install sklearn
pip install matplotlib
pip install seaborn
```

Load your IDE and create a new project. Ensure that the repository files are saved into the same directory as the new project folder you have just created. 

When selecting a project interpreter navigate to the installtion path of Anaconda and select the following file. __Ensure that you select the pythonW.exe not python.exe__

> <drive>:\<install location>\Anaconda\envs\tensor\pythonw.exe>

Then create a configuration in your IDE by selecting the _NHL v4.py_ file as the script path by navigating the project folder on your local drive.

The script should now run

## How to use
In order to run the algorithm, create a new 

## Dataset
The dataset used was a cleaned version of the [NHL Game Data](https://www.kaggle.com/martinellis/nhl-game-data) provided by Martin Ellis on Kaggle.

The game.csv and game_teams_stats.csv were cleaned (some formatting errors are present in raw data) and combined into a single csv file in excel. The game.csv entries were doubled as the game_teams_stats.csv contains 2 rows per 1 game_id. This was done to ensure that both datasets matched (ie, there were 2 rows per match, 1 for away team stats and the 1 row for home team stats).

## Notes
Currently [APIs for NHL statistics](https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api) are not well documented however work is being done to improve this. As documentation and access to the API improves, this model will be updated to reflect those changes and improve the quality and reliability of the results.

