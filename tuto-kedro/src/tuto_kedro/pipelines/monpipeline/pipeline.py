"""
This is a boilerplate pipeline 'monpipeline'
generated using Kedro 0.19.3
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load_and_normalize
from .nodes import split_data
from .nodes import train_model
from .nodes import eval_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=load_and_normalize,
                inputs="digits", #catalog.yml
                outputs=['x','y'],
                name="load",
            ),
            node(
                func=split_data,
                inputs=['x', 'y','parameters'],
                outputs=['X_train', 'X_test', 'y_train', 'y_test'],
                name="split",
            ),
            node(
                func=train_model,
                inputs=['X_train', 'y_train','parameters'],
                outputs='regressor',
                name="train",
            ),
            node(
                func=eval_model,
                inputs=['regressor', 'X_test', 'y_test'],
                outputs='score',
                name="eval",
            )

        ]
    )
