#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import matplotlib as mpl
import pyleoclim as pyleo
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from ..utils.sampling import confidence_interval
from ..utils.fisher import smooth_series

class RQARes(pyleo.Series):
    '''Class for storing the result of various RQA techniques'''

    def __init__(self, time, value, time_name=None, time_unit=None, value_name=None, value_unit=None, series=None,label=None, m=None,
                tau=None,eps=None,eigenmap=None,w_size=None,w_incre=None):
        super().__init__(time,value,time_name,time_unit,value_name,value_unit,label,sort_ts=None)
        self.time=time
        self.value=value
        self.time_name=time_name
        self.time_unit=time_unit
        self.value_name=value_name
        self.value_unit=value_unit
        self.series=series
        self.label=label
        self.m = m
        self.tau = tau
        self.eps = eps
        self.eigenmap = eigenmap
        self.series = series
        self.w_size = w_size
        self.w_incre = w_incre

    def smooth(self,block_size):
        '''Function to perform block smoothing on your RQA result
        
        Parameters
        ----------
        
        block_size : int
            Number of points to include in each block
            
        Returns
        -------
        
        smoothed_series : ammonyte.RQARes
            Smoothed version of your original RQARes object
            
        See also
        --------
        
        ammonyte.utils.fisher.smooth_series'''

        if block_size is None:
            block_size = int(len(self.time)/15)
            smoothed_series = smooth_series(self,block_size)
        else:
            smoothed_series = smooth_series(self,block_size)

        return smoothed_series

    def confidence_fill_plot(self,ax=None,line_color=None,fill_color=None,fill_alpha=None,transition_interval=None,xlabel=None,ylabel=None,marker=None,
                     markersize=None,linestyle=None,linewidth=None,alpha=None,label=None,title=None,zorder=None,plot_kwargs=None,ci_kwargs=None,
                     background_series=None,background_kwargs=None,legend=True,lgd_kwargs=None):

        '''Function for plotting rqa results with confidence bounds

        Parameters
        ----------

        ax : matplotlib.axes object
            Axes to plot on, if None new plot will be generated

        line_color : str, tuple
            String or rgb tuple to use for line color
        
        fill_color : str, tuple
            String or rgb tuple to use for fill color in between lines

        fill_alpha : float
            Transparency of the fill, default is .1

        transition_interval : list,tuple
            Upper and lower bound for the transition interval

        marker : str
            e.g., 'o' for dots
            See `matplotlib.markers <https://matplotlib.org/stable/api/markers_api.html>`_ for details

        markersize : float
            the size of the marker

        linestyle : str
            e.g., '--' for dashed line
            See `matplotlib.linestyles <https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html>`_ for details

        linewidth : float
            the width of the line

        alpha : float
            Transparency of the line

        label : str
            the label for the line

        xlabel : str
            the label for the x-axis

        ylabel : str
            the label for the y-axis

        title : str
            the title for the figure

        zorder : int
            The default drawing order for all lines on the plot

        plot_kwargs : dict
            Key word arguments for the main plot, see `pyleoclim.Series.plot <https://pyleoclim-util.readthedocs.io/en/latest/core/api.html#series-pyleoclim-series>_ for details

        ci_kwargs : dict
            Key word arguments for calculating the confidence interval. Only to be used if `transition_interval` is not passed. See ammonyte.utils.sampling.confidence_interval for details

        background_series : pyleoclim.Series
            Optional to pass a different series that will be plotted behind the main series plot

        background_kwargs : dict
            Key word arguments for the background plot. If none are passed, the color of the main plot will be re-used 
            and alpha will be set to .2

        legend : bool; {True,False}
            Whether or not to plot the legend

        lgd_kwargs : dict

        Returns
        -------

        fig : matplotlib.figure
            The figure object from matplotlib.
            See `matplotlib.pyplot.figure <https://matplotlib.org/stable/api/figure_api.html>`_ for details.

        ax : matplotlib.axis 
            The axis object from matplotlib. 
            See `matplotlib.axes <https://matplotlib.org/stable/api/axes_api.html>`_ for details.


        See also
        --------

        ammonyte.utils.sampling.confidence_interval

        '''

        ci_kwargs = {} if ci_kwargs is None else ci_kwargs.copy()
        plot_kwargs = {} if plot_kwargs is None else plot_kwargs.copy()
        lgd_kwargs = {} if lgd_kwargs is None else lgd_kwargs.copy()

        series = self.interp(step=1)

        if not transition_interval:
            transition_interval = confidence_interval(series,**ci_kwargs)
        
        if line_color is None:
            line_color=sns.color_palette('colorblind')[0]
        if fill_color is None:
            fill_color=sns.color_palette('colorblind')[0]
        
        #Need to find points in time where the series intersects with the lower and upper confidence boundaries
        value = series.value
        time = series.time
        
        idx_ufill = []
        idx_lfill = []

        upper = max(transition_interval)
        lower = min(transition_interval)

        #Need to find all points that lie above or below our confidence interval
        for idx,v in enumerate(value):
            if v >= upper:
                idx_ufill.append(idx)
            elif v <= lower:
                idx_lfill.append(idx)
        
        if ax is None:
            fig,ax = plt.subplots(figsize=(12,8))

        if background_series:

            if not isinstance(background_series,pyleo.core.Series):
                raise ValueError('background_series does not appear to be a pyleoclim.Series object')
            
            #Standardize background_series values
            background_series.value -= np.mean(background_series.value)
            background_series.value /= max(background_series.value)

            #Adjust scaling to match that of main series
            background_series.value *= max(series.value - np.mean(series.value))
            background_series.value += np.mean(series.value)

            background_kwargs = {} if background_kwargs is None else background_kwargs.copy()

            if 'alpha' not in background_kwargs:
                background_kwargs['alpha'] = .2
            if 'color' not in background_kwargs:
                background_kwargs['color'] = line_color

            background_series.plot(ax=ax, **background_kwargs)

        if fill_alpha is None:
            fill_alpha = .1

        if xlabel is None:
            xlabel = f'{self.time_name} [{self.time_unit}]'

        if ylabel is None:
            ylabel = f'{self.value_name} [{self.value_unit}]'

        if label is None:
            label = self.label

        if label is not None:
            plot_kwargs.update({'label': label})

        if marker is not None:
            plot_kwargs.update({'marker': marker})

        if markersize is not None:
            plot_kwargs.update({'markersize': markersize})

        if linestyle is not None:
            plot_kwargs.update({'linestyle': linestyle})

        if linewidth is not None:
            plot_kwargs.update({'linewidth': linewidth})

        if alpha is not None:
            plot_kwargs.update({'alpha': alpha})

        if zorder is not None:
            plot_kwargs.update({'zorder': zorder})

        series.plot(ax=ax,color=line_color,xlabel=xlabel,ylabel=ylabel,title=title,plot_kwargs=plot_kwargs,lgd_kwargs=lgd_kwargs,legend=legend)
            
        ufill_values = np.zeros(len(time)) + upper
        lfill_values = np.zeros(len(time)) + lower
        
        for i in range(len(time)):
            if i in idx_ufill:
                ufill_values[i] = value[i]
            elif i in idx_lfill:
                lfill_values[i] = value[i]
                                    
        ax.fill_between(time,lower,upper,color=fill_color,alpha=fill_alpha)
        ax.fill_between(time,upper,ufill_values,color=fill_color)
        ax.fill_between(time,lower,lfill_values,color=fill_color)

        if 'fig' in locals():
            return fig, ax
        else:
            return ax

    def confidence_smooth_plot(self,block_size,figsize=(12,8),ax=None,transition_interval=None,
                    color=None,label=None,xlabel=None,ylabel=None,title=None,ci_kwargs=None,
                    background_series=None,background_kwargs=None,hline_kwargs=None,
                    ci_plot_kwargs=None,legend=True,lgd_kwargs=None):

        '''Function for plotting rqa results with confidence bounds

        Parameters
        ----------

        block_size : int
            Size of smoothing block to use

        ax : matplotlib.axes object
            Axes to plot on, if None new plot will be generated

        transition_interval : list,tuple
            Upper and lower bound for the transition interval

        color : str, tuple
            String or rgb tuple to use for marker color

        label : str
            the label for the Fisher Information

        xlabel : str
            the label for the x-axis

        ylabel : str
            the label for the y-axis

        title : str
            the title for the figure

        background_series : pyleoclim.Series
            Optional to pass a different series that will be plotted behind the main series plot

        background_kwargs : dict
            Key word arguments for the background plot. If none are passed, the color of the main plot will be re-used 
            and alpha will be set to .2

        hline_kwargs : dict
            Key word arguments for the Fisher Information statistic plot. Passed to matplotlib.axes.Axes.hlines.

        ci_plot_kwargs : dict
            Key word arguments for the confidence interval plot. Passed to matplotlib.axes.Axes.fill_between.

        legend : bool; {True,False}
            Whether or not to plot the legend

        lgd_kwargs : dict
            Key word arguments for the legend. Passed to matplotlib.axes.Axes.legend.

        Returns
        -------

        fig : matplotlib.figure
            The figure object from matplotlib.
            See `matplotlib.pyplot.figure <https://matplotlib.org/stable/api/figure_api.html>`_ for details.

        ax : matplotlib.axis 
            The axis object from matplotlib. 
            See `matplotlib.axes <https://matplotlib.org/stable/api/axes_api.html>`_ for details.


        See also
        --------

        ammonyte.utils.sampling.confidence_interval

        matplotlib.axes.Axes.hlines

        matplotlib.axes.Axes.fill_between

        '''

        if not isinstance(block_size,int):
            raise ValueError('Block size must be an integer')

        ci_kwargs = {} if ci_kwargs is None else ci_kwargs.copy()
        hline_kwargs = {} if hline_kwargs is None else hline_kwargs.copy()
        ci_plot_kwargs = {} if ci_plot_kwargs is None else ci_plot_kwargs.copy()
        lgd_kwargs = {} if lgd_kwargs is None else lgd_kwargs.copy()

        if not transition_interval:
            transition_interval = confidence_interval(self,**ci_kwargs)
        
        if ax is None:
            fig,ax = plt.subplots(figsize=figsize)

        if xlabel is None:
            if self.time_unit:
                xlabel = f'{self.time_name} [{self.time_unit}]'
            else:
                xlabel = f'{self.time_name}'

        if ylabel is None:
            if self.value_unit:
                ylabel = f'{self.value_name} [{self.value_unit}]'
            else:
                ylabel = f'{self.value_name}'

        if title is None:
            title = self.label

        if label is None:
            if self.value_unit:
                label = f'{self.value_name} [{self.value_unit}]'
            else:
                label = f'{self.value_name}'
        
        if color is None:
            color = sns.color_palette('colorblind')[2]
        
        smoothed_series = self.smooth(block_size=block_size)

        smooth_values = smoothed_series.value
        smooth_times = smoothed_series.time

        hlines = [np.mean(smooth_values[i:i + block_size]) for i in range(0, len(smooth_values), block_size)]
        htime_min = [min(smooth_times[i:i + block_size]) for i in range(0, len(smooth_times), block_size)]
        htime_max = [max(smooth_times[i:i + block_size]) for i in range(0, len(smooth_times), block_size)]

        if 'color' not in hline_kwargs:
            hline_kwargs['color'] = color

        if 'linewidth' not in hline_kwargs:
            hline_kwargs['linewidth'] = 3
        
        if 'label' not in hline_kwargs:
            hline_kwargs['label'] = label

        ax.hlines(hlines,htime_min,htime_max,**hline_kwargs)

        if 'color' not in ci_plot_kwargs:
            ci_plot_kwargs['color'] = color

        if 'alpha' not in ci_plot_kwargs:
            ci_plot_kwargs['alpha'] = .3

        if 'label' not in ci_plot_kwargs:
            ci_plot_kwargs['label'] = 'Bootstrap 95% CI'

        ax.fill_between(self.time,y1=min(transition_interval),y2=max(transition_interval),**ci_plot_kwargs)

        ax.yaxis.label.set_color(color)
        ax.tick_params(axis='y',colors=color)
        ax.spines['left'].set_color(color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel,color=color)
        ax.set_title(title)
        ax.grid(None)

        if background_series:

            ax2 = ax.twinx()

            if not isinstance(background_series,pyleo.core.Series):
                raise ValueError('background_series does not appear to be a pyleoclim.Series object')
            
            # #Standardize background_series values
            # background_series.value -= np.mean(background_series.value)
            # background_series.value /= max(background_series.value)

            # #Adjust scaling to match that of main series
            # background_series.value *= max(self.value - np.mean(self.value))
            # background_series.value += np.mean(self.value)

            background_kwargs = {} if background_kwargs is None else background_kwargs.copy()

            if 'alpha' not in background_kwargs:
                background_kwargs['alpha'] = .2

            if 'legend' not in background_kwargs and not legend:
                background_kwargs['legend'] = False

            if 'label' not in background_kwargs and legend:
                background_kwargs['label'] = 'Original series'

            if 'color' not in background_kwargs:
                background_kwargs['color'] = 'grey'

            ax2.yaxis.label.set_color(background_kwargs['color'])
            ax2.tick_params(axis='y',colors=background_kwargs['color'])
            ax2.spines['right'].set_visible(True)
            ax2.spines['right'].set_color(background_kwargs['color'])
            ax2.spines['left'].set_visible(False)
            background_series.plot(ax=ax2, **background_kwargs)

        if legend:
            ax.legend(**lgd_kwargs)

        if 'fig' in locals():
            return fig, ax
        else:
            return ax

    def plot_eigenmaps(self,groups,axes,figsize=(12,12),cmap='viridis',cmap_kwargs = None,ax=None,title=None):
        '''Function to display eigenmaps

        Only works when the RQARes has been created via the laplacian eigenmaps function
        
        Parameters
        ----------

        groups : list,tuple; (start,stop)
            List of lists or tuples containing start stop time indices for coloring. Should be ordered in time.

        axes : list,tuple
            Axes of the eigenvectors. Should be list or tuple of length 2.
        
        figsize : list,tuple
            Size of the figure

        cmap : str, list
            Color map to use for color coding according to time. Can either be the name of a color map or a list of colors
        
        cmap_kwargs : dict
            Dictionary of key word arguments for ax.figure.colorbar

        ax : matplotlib.axes.Axes
            Ax object to plot on.

        Returns
        -------

        fig : matplotlib.figure
            The figure object from matplotlib.
            See `matplotlib.pyplot.figure <https://matplotlib.org/stable/api/figure_api.html>`_ for details.

        ax : matplotlib.axis 
            The axis object from matplotlib. 
            See `matplotlib.axes <https://matplotlib.org/stable/api/axes_api.html>`_ for details.

        '''

        if not ax:
            fig, ax = plt.subplots(figsize=figsize)

        if isinstance(cmap,str):
            colors = plt.cm.get_cmap(cmap).colors
        else:
            colors = cmap

        cmap_kwargs = {} if cmap_kwargs is None else cmap_kwargs.copy()
        cmap_plot = mpl.colors.LinearSegmentedColormap.from_list(f'{self.time_name} [{self.time_unit}]',colors=colors,N=len(groups))
        norm = mpl.colors.BoundaryNorm(boundaries=(groups[0][0],*[group[0] for group in groups[1:]],groups[-1][-1]),ncolors=len(groups))
        eigvec = self.eigenmap

        for idx,group in enumerate(groups):

            if not isinstance(group,(list,tuple)) or len(group) != 2:
                raise ValueError(f'Group [{idx}] format is not recognized. Please use [(start,stop),(start,stop),etc.] format for groups.')

            start = group[0]
            stop = group[1]

            if start > max(self.time) or start < min(self.time):
                print('Start value exceed time bounds of RQARes object, ')
                start = max(self.time)

            if stop > max(self.time) or stop < min(self.time):
                raise ValueError(f'Stop time [{stop}] from group [{idx}] is not within the time bounds of your RQARes object.')

            start_index = np.where(self.series.time==start)[0][0]
            stop_index = np.where(self.series.time==stop)[0][0]

            eig1 = eigvec[:,axes[0]][start_index:stop_index]
            eig2 = eigvec[:,axes[1]][start_index:stop_index]
            ax.scatter(eig1,eig2,color=cmap_plot(idx),norm=norm)

        if title is None:
            title = f'Eigenmaps for {self.label}'

        ax.set_title(title)
        ax.set_xlabel(f'$\Phi_{axes[0]}$',labelpad=10)
        ax.set_ylabel(f'$\Phi_{axes[1]}$',labelpad=10)
        ax.ticklabel_format(axis='x', scilimits=[0, 0])
        ax.ticklabel_format(axis='y', scilimits=[0, 0])

        if 'shrink' not in cmap_kwargs:
            cmap_kwargs['shrink'] = .5

        if 'orientation' not in cmap_kwargs:
            cmap_kwargs['orientation'] = 'horizontal'

        if 'label' not in cmap_kwargs:
            cmap_kwargs['label'] = cmap_plot.name

        ax.figure.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_plot),ax=ax, **cmap_kwargs)

        if 'fig' in locals():
            return fig, ax
        else:
            return ax


    def plot_eigenmaps_FI(self,groups,axes,block_smooth=True,cmap='viridis',cmap_kwargs=None,figsize=(18,12),
                          ax=None,FI_axis_lims=None,scale=(1,1,1),title=None):
        '''Function to display eigenmaps as a function of fisher information
        
        Only works when the RQARes has been created via the laplacian eigenmaps function
        
        Parameters
        ----------
        
        groups : list,tuple; (start,stop)
            List of lists or tuples containing start stop time indices for block smoothing.

        axes : list,tuple
            Axes of the eigenvectors to plot against Fisher Information. Should be list or tuple of length 2.

        block_smooth : bool; {True,False}
            Whether or not to calculate and display the mean of the fisher information.

        cmap : str
            Color map to use for color coding according to time

        cmap_kwargs : dict
            Dictionary of key word arguments for ax.figure.colorbar

        figsize : list,tuple
            Size of the figure

        ax : matplotlib.axes.Axes
            Ax object to plot on. If passed must use projection = '3d'.

        FI_axis_lims : list,tuple
            Boundaries for the fisher information axis

        Returns
        -------

        fig : matplotlib.figure
            The figure object from matplotlib.
            See `matplotlib.pyplot.figure <https://matplotlib.org/stable/api/figure_api.html>`_ for details.

        ax : matplotlib.axis 
            The axis object from matplotlib. 
            See `matplotlib.axes <https://matplotlib.org/stable/api/axes_api.html>`_ for details.

        '''

        if not ax:
            fig = plt.figure(figsize=figsize)
            ax = fig.add_subplot(projection='3d')

        if isinstance(cmap,str):
            colors = plt.cm.get_cmap(cmap).colors
        else:
            colors = cmap

        cmap_kwargs = {} if cmap_kwargs is None else cmap_kwargs.copy()
        cmap_plot = mpl.colors.LinearSegmentedColormap.from_list(f'{self.time_name} [{self.time_unit}]',colors=colors,N=len(groups))
        norm = mpl.colors.BoundaryNorm(boundaries=(groups[0][0],*[group[0] for group in groups[1:]],groups[-1][-1]),ncolors=len(groups))
        eigvec = self.eigenmap

        for idx,group in enumerate(groups):

            if not isinstance(group,(list,tuple)) or len(group) != 2:
                raise ValueError(f'Group [{idx}] format is not recognized. Please use [(start,stop),(start,stop),etc.] format for groups.')

            start = group[0]
            stop = group[1]

            if start > max(self.time) or start < min(self.time):
                print('Start value exceed time bounds of RQARes object, ')
                start = max(self.time)

            if stop > max(self.time) or stop < min(self.time):
                raise ValueError(f'Stop time [{stop}] from group [{idx}] is not within the time bounds of your RQARes object.')

            rqa_slice = self.slice(group)
            start_index = np.where(self.series.time==start)[0][0]
            stop_index = np.where(self.series.time==stop)[0][0]

            eig1 = eigvec[:,axes[0]][start_index:stop_index]
            eig2 = eigvec[:,axes[1]][start_index:stop_index]

            if block_smooth:
                FI_block_value = np.mean(rqa_slice.value)
                FI = np.full(len(eig1), FI_block_value)
                ax.scatter(FI,eig1,eig2,color=cmap_plot(idx),norm=norm)
            elif not block_smooth:
                raise ValueError("Value for block smoothing must be passed because I haven't figured out how to properly do it without it yet.")
                # FI = np.concatenate([np.ones(math.floor(len(eig1)/self.w_incre))*value for value in self.value[start_index:stop_index]])
                # print(FI.shape)
                # print(eig1.shape)
                # print(eig2.shape)
                # ax.scatter(FI,eig1,eig2,c = cmap(norm(self.series.time[start_index:stop_index])))

        if FI_axis_lims:
            ax.set_xlim(left=min(FI_axis_lims),right=max(FI_axis_lims))

        ax.set_xlabel('FI',labelpad=10)
        ax.set_ylabel(f'EM Axis {axes[0]}',labelpad=10)
        ax.set_zlabel(f'EM Axis {axes[1]}',labelpad=10)
        ax.ticklabel_format(axis='x', scilimits=[0, 0])
        ax.ticklabel_format(axis='y', scilimits=[0, 0])
        ax.ticklabel_format(axis='z', scilimits=[0, 0])
        ax.set_title(title)

        scale_x,scale_y,scale_z = scale
        ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([scale_x, scale_y, scale_z, 1]))

        if 'shrink' not in cmap_kwargs:
            cmap_kwargs['shrink'] = .5

        if 'orientation' not in cmap_kwargs:
            cmap_kwargs['orientation'] = 'horizontal'

        if 'label' not in cmap_kwargs:
            cmap_kwargs['label'] = cmap_plot.name

        ax.figure.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_plot),ax=ax, **cmap_kwargs)

        if 'fig' in locals():
            return fig, ax
        else:
            return ax