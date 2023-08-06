## mlcakes

Some functional modules for machine learning.

## file structure

```
|- evaluation
    |- binary_class.py # metrics for binary class task.
    |- multi_class.py  # metrics for multi class task.
```

## API

###  `evaluation.binary_class.Metrics`

**Parameters:**

-  y_pred

> Model predicted labels [list or numpy.array]. such as: [1,0,1,0,1,0]

- y_true

> Real labels [list or numpy.array]. such as: [1,1,1,0,1,0]

- y_score

> The binary classification model predicts the probability value that a sample is positive. such as [0.1, 0.8, 0.7, 0.6, 0.3, 0.2]

- output

> JSON file name, used to save all metrics. such as model_metrics.json

- plot_roc

> Bool value, whether to draw the ROC curve. such as True or False.

- roc_fig

> Filename, used to save the ROC curve. such as roc_curve.pdf, roc_curve.png

**Example**

```py
import numpy as np
from evaluation.binary_class import Metrics

y_pred = np.random.choice(2, size=100)
y_true = np.random.choice(2, size=100)
y_score = np.random.random(100)
    
Evaluation = Metrics(y_pred=y_pred, y_score=y_score, y_true=y_true, plot_roc=True ,roc_fig='aa.png')
print(Evaluation.metrics_)
```

###  `evaluation.multi_class.Metrics`

**Parameters:**

-  y_pred

> Model predicted labels [list or numpy.array]. such as: [1,2,1,0,1,0]

- y_true

> Real labels [list or numpy.array]. such as: [1,1,2,0,1,0]

- y_score

> The multi classification model predicts the probability value, shape should be [samples, num_class]. such as [[0.1, 0.2, 0.7], [0.2, 0.1, 0.7], [0.7, 0.2, 0.1], [0.1, 0.2, 0.7], [0.1, 0.2, 0.7], [0.1, 0.2, 0.7]]

- output

> JSON file name, used to save all metrics. such as model_metrics.json


**Example**

```py
import numpy as np
from evaluation.binary_class import Metrics

y_pred = np.random.choice(5, size=100)
y_true = np.random.choice(5, size=100)
y_score = np.random.random((100,5))
def softmax(x):
    a = np.sum(np.exp(x), axis=1)
    return np.exp(x) / a[:, None]

y_score = softmax(y_score)

Evaluation = Metrics(y_pred=y_pred, y_score=y_score, y_true=y_true)

print(Evaluation.metrics_)
```

