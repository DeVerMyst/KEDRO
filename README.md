# Kedro

29-03-2024

**Kévin** and **Boris** Tutorial
### step by step

##### VENV
`py -m venv .venv`
`.venv/Scripts/activate`

##### install
`pip install kedro`

##### initialisation
`kedro new --name=<your-project-name> --tools=lint,test,log,docs,data,viz, kedro_viz, kedro-datasets --example=no`

###### example:
`kedro new --name=tuto_kedro --tools=lint,test,log,docs,data,viz --example=no` 

* catalog.yml 
  * all input/output of the proejct
* MNIST dans RAW

##### RUN
`kedro run`

##### VIZ
`kedro viz run`

##### copy data to DATA RAW

#### create pipeline
`kedro pipeline create  monpipeline`

* fichier conf + fichier pipeline

`src/nomduprojet/pipelines/nomdupipeline/node|pipelines.py`

* first step of data processing
  * normalization
  * node.py
```python
def load_and_normalize(digits):
    x = digits[0]
    y = digits[1]
    x = x / 255
    return x, y 
``` 
* pipeline.py
```python
  from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load_and_normalize


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=process_function,
                inputs="dataset",
                outputs="preprocessed_dataset",
                name="preprocess_x_node",
            ),
        ]
    )
``` 
```python
            node(
                func=load_and_normalize,
                inputs="digits", #catalog.yml
                outputs=['x','y'],
                name="load",
            ),
```

