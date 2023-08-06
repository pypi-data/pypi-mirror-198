import plotly.express as px
import ipywidgets as widgets
from sklearn.metrics import confusion_matrix, f1_score , classification_report
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

class Pgplot:
    """
    A class to visualize machine learning models using various plots and visualizations.

    Parameters:
    -----------
    model : object
        A trained machine learning model object.

    Methods:
    --------
    plot_cm(X, y):
        Plots a confusion matrix for a given set of features X and labels y.

    plot_f1(X):
        Plots the F1 score for a clustering model based on a given set of features X.

    kmeans_n_clusters(X):
        Plots a scatterplot of the data with the KMeans clustering algorithm applied
        for different numbers of clusters.

    rf_n_estimators(X, y):
        Plots the performance of a Random Forest classifier based on the number of estimators.
    """
    
    def __init__(self, model):
        self.model = model
    
    def plot_cm(self, X, y):
        """
        Plots a confusion matrix for a given set of features X and labels y.

        Parameters:
        -----------
        X : numpy array
            A 2D numpy array of features.
        y : numpy array
            A 1D numpy array of labels.
        """
        y_pred = self.model.predict(X)
        cm = confusion_matrix(y, y_pred)
        labels = list(set(y)) # define labels here
        
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_xlabel('Predicted Label')
        ax.set_ylabel('True Label')
        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)
        #ax.legend(title='Confusion Matrix')
        plt.show()
    
    def plot_f1(self, X):
        """
        Plots the F1 score for a clustering model based on a given set of features X.

        Parameters:
        -----------
        X : numpy array
            A 2D numpy array of features.
        """
        labels = self.model.labels_
        f1 = f1_score(y_true=X[:, -1], y_pred=labels, average=None)
        
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.bar(range(len(labels)), f1)
        ax.set_xlabel('Cluster')
        ax.set_ylabel('F1 Score')
        #ax.legend(title='F1 Score')
        plt.show()

    
    def kmeans_n_clusters(self, X):
        """
        Plots a scatterplot of the data with the KMeans clustering algorithm applied
        for different numbers of clusters.

        Parameters:
        -----------
        X : numpy array
            A 2D numpy array of features.
        """
        kmeans = None
        
        def update_plot(n_clusters,point_color):
            nonlocal kmeans

            kmeans = KMeans(n_clusters=n_clusters)
            kmeans.fit(X)

            labels = kmeans.labels_
            centers = kmeans.cluster_centers_
            
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.scatter(X[:, 0], X[:, 1], c=labels)
            ax.scatter(centers[:, 0], centers[:, 1], marker='*', s=100, c='#050505')
            ax.set_title('KMeans Clustering')
            #ax.legend()
            plt.show()
            print(f'Inertia: {kmeans.inertia_}')

        n_clusters_slider = widgets.IntSlider(min=2, max=20, step=1, description='Number of Clusters:', value=2)
        color_picker = widgets.ColorPicker(description='Point Color', value='#1f77b4')
        widgets.interact(update_plot, n_clusters=n_clusters_slider,point_color=color_picker)
        

    def rf_n_estimators(self, X, y,xlabel='Feature 1',ylabel='Feature 2',title="Random Forest Classifier"):
        """
        Generates an interactive plot showing the performance of a random forest classifier on a given dataset with respect to 
        the number of decision trees (estimators) used in the model. The plot displays the data points colored by their predicted 
        class label, and the plot title displays the number of decision trees used.
        Parameters:
        -----------
        X : array-like of shape (n_samples, n_features)
            The input data.
        y : array-like of shape (n_samples,)
            The target values.
        xlabel : str, optional (default='Feature 1')
            Label for the x-axis of the plot.
        ylabel : str, optional (default='Feature 2')
            Label for the y-axis of the plot.
        Returns:
        --------
        None
        """
        def fit_rf(n_estimators, point_color):
            rf = RandomForestClassifier(n_estimators=n_estimators)
            rf.fit(X, y)
            
            y_pred = rf.predict(X)
            report = classification_report(y_true=y, y_pred=y_pred)
            print(report)
            
            fig, ax = plt.subplots(figsize=(7, 5))
            ax.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
            ax.set_xlabel(f'{xlabel}')
            ax.set_ylabel(f'{ylabel}')
            ax.set_title(f'{title} (n_estimators={n_estimators})')
            #ax.legend(title='Predictions')
            plt.show()

        n_estimators_slider = widgets.IntSlider(min=10, max=200, step=10, description='Number of Estimators:', value=10)
        color_picker = widgets.ColorPicker(description='Point Color', value='#1f77b4')
        widgets.interact(fit_rf, n_estimators=n_estimators_slider, point_color=color_picker)