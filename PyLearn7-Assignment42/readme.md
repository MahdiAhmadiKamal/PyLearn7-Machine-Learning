# kNN algorithm training and testing on ANSUR II dataset

The Anthropometric Survey of US Army Personnel (ANSUR 2 or ANSUR II) data were published internally in 2012. They were made available publicly in 2017. They have replaced ANSUR I as the most comprehensive publicly available data set on body size and shape. They include 93 measures for over 6,000 adult US military personnel (4,082 men and 1,986 women). In contrast to the ANSUR I data, the new sample includes reservists. Despite the presence of reservists in the sample, it is still not an approximation of the US Civilian population. Consequently, while there is useful information here, designs and standards based on these data will not accommodate most user populations in the intended manner.

## How to Install
Run following command:
```
pip install -r requirements.txt
```

## Results

<img src="pics\output.png" width="571">

<img src="pics\output2.png" width="507">

### Accuracy results for different amounts of k:

|  Features |  k = 3  |  k = 5  |  k = 7 |
|---------------| --------------- | --------------- | --------------- |
|stature, weight|  0.83   | 0.84  | 0.84  |
|stature, weight, biacromial breadth |  0.91   | 0.92  | 0.91  |
|stature , weight, biacromial breadth, foot length|  0.90  | 0.92  | 0.92  |

### How to Run
Execute this command in terminal:
```
python kNN_ANSUR_II_4features.ipynb
```


## Python
The programs are written using [Python](https://www.python.org/) language and the following tools:

<img src="pics/numpy.png" width="300">
<img src="pics/matplotlib.png" width="300">
<img src="pics/pandas.png" width="300">
<img src="pics/scikit-learn.png" width="300">