from sklearn.tree import  export_graphviz
from IPython.display import Image
import pydotplus
from io import   StringIO

dot_data = StringIO()
export_graphviz(
    decision_tree=,
    out_file=dot_data,
    feature_names=predictors,
                )