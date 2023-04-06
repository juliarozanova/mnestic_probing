from cProfile import label
from typing import List
import pandas as pd
import numpy as np
import umap
import plotly.express as px
import plotly.graph_objects as go
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder

def pca_project(input_matrix):
    pca = PCA(n_components=3)
    projected = pca.fit_transform(input_matrix)
    projected = pd.DataFrame(projected, columns=['x', 'y', 'z'])
    return projected


def umap_project(input_matrix):
    umapper = umap.UMAP(n_components=3).fit(input_matrix)
    projected = umapper.fit_transform(input_matrix)
    projected = pd.DataFrame(projected, columns=['x', 'y', 'z'])
    return projected


def project_and_show(input_matrix, meta_df, label_column):

    projected = pca_project(input_matrix)
    # u_projected = umap_project(input_matrix)

    fig = px.scatter_3d(projected, 
    x=projected.x, 
    y=projected.y, 
    z=projected.z, 
    color=meta_df[f'{label_column}'])

    # u_fig = px.scatter_3d(u_projected, 
    # x=u_projected.x, 
    # y=u_projected.y, 
    # z=u_projected.z, 
    # color=meta_df[f'{label_column}'])

    fig.show()
    # u_fig.show()


def animate(projected_reps: List[pd.DataFrame], meta_df: pd.DataFrame, label_column):

    colors = LabelEncoder().fit_transform(y=meta_df[label_column])

    def get_frame(df):
        return go.Frame(data=[go.Scatter3d(x=df.x, 
                                    y=df.y,
                                    z=df.z,
                                    mode="markers",
                                    marker=dict(
                                        color=colors,
                                        colorscale="Viridis"
                                        )
                                    )
                    ])
    frames = [get_frame(df) for df in projected_reps]

    fig = go.Figure(
        data=[go.Scatter3d(x=projected_reps[0].x, 
                y=projected_reps[0].y, 
                z=projected_reps[0].z,
                mode="markers",
                marker=dict(
                   color=colors,
                   colorscale="Viridis"
    ))],
        layout=go.Layout(
            title="Start Title",
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="Play",
                            method="animate",
                            args=[None])])]
        ),
        frames=frames
        )

    fig.show(renderer='notebook_connected')
