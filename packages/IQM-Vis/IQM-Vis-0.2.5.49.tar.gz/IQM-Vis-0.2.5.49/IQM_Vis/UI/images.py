'''
UI image functions
'''
# Author: Matt Clifford <matt.clifford@bristol.ac.uk>

import os

import numpy as np
from PyQt6.QtWidgets import QApplication

from IQM_Vis.utils import gui_utils, plot_utils, image_utils

# sub class used by IQM_Vis.main.make_app to control all of the image widgets
class images:
    def __init__(self):
        self.metric_range_graph_num = 0
    '''
    image updaters
    '''
    def transform_image(self, image):
        for key in self.sliders['transforms']:
            image = self.sliders['transforms'][key]['function'](image, self.params_from_sliders['transforms'][key])
        return image

    def display_images(self):
        for i, data_store in enumerate(self.data_stores):
            # reference image
            reference_image = data_store.get_reference_image()
            gui_utils.change_im(self.widget_row[i]['images']['original']['data'], reference_image, resize=self.image_display_size)
            # transform image
            trans_im = image_utils.get_transform_image(data_store, self.sliders['transforms'], self.params_from_sliders['transforms'])
            gui_utils.change_im(self.widget_row[i]['images']['transformed']['data'], trans_im, resize=self.image_display_size)
            # metrics
            metrics = data_store.get_metrics(trans_im, self.checked_metrics, **self.params_from_sliders['metric_params'])
            self.display_metrics(metrics, i)
            # metric images
            metric_images = data_store.get_metric_images(trans_im, self.checked_metric_images, **self.params_from_sliders['metric_params'])
            self.display_metric_images(metric_images, i)

            QApplication.processEvents()   # force to change otherwise the UI wont respond

    def update_image_widgets(self):
        # display images
        for i in self.widget_row:
            gui_utils.change_im(self.widgets['image'][key], self.image_data[key], resize=self.image_display_size)

    '''
    metric graph updaters
    '''
    def redo_plots(self, calc_range=True):
        if calc_range:  # add an or metrics_range val not been calculated
            if self.metrics_avg_graph or self.metric_range_graph:
                self.get_metrics_over_all_trans_with_init_values()
        if self.metrics_avg_graph:
            self.display_metrics_over_range()
        if self.metric_range_graph:
            self.display_metric_range_plot()

    '''
    change image in dataset
    '''
    def change_data(self, i):
        self.data_num += i
        # check the num is legal
        if self.data_num < 0:
            self.data_num = 0
        if self.data_num > self.max_data_ind:
            self.data_num = self.max_data_ind
        for data_store in self.data_stores:
            try:
                data_store[self.data_num]
            except:
                pass # some datasets will be shorter than others - this is fine though
        self.display_images()
        self.set_image_name_text()
        self.redo_plots()

    '''
    metric updaters
    '''
    def display_metrics(self, metrics, i):
        if self.metrics_info_format == 'graph':
            self.display_metrics_graph(metrics, i)
        else:
            self.display_metrics_text(metrics, i)

    def display_metrics_graph(self, metrics, i):
        bar_plt = plot_utils.bar_plotter(bar_names=[''],
                                        var_names=list(metrics.keys()),
                                        ax=self.widget_row[i]['metrics']['info']['data'],
                                        lim=self.plot_data_lim)
        bar_plt.plot('', list(metrics.values()))
        bar_plt.show()

    def display_metrics_text(self, metrics, i, disp_len=5):
        text = ''
        for key in metrics:
            metric = gui_utils.str_to_len(str(metrics[key]), disp_len, '0')
            text += key + ': ' + metric + '\n'
        self.widget_row[i]['metrics']['info']['data'].setText(text)

    '''
    get metric values when adjusting a single transformation value over its range
    '''
    def get_metrics_over_all_trans_with_init_values(self):
        self.metric_over_range_results = []
        # use the initiased/default values for all sliders
        init_trans_params = {}
        for trans in self.checked_transformations:
            init_trans_params[trans] = self.checked_transformations[trans]['init_value']
        self.status_bar.showMessage('Getting Range plot Values')
        QApplication.processEvents()
        max_val = 0
        for i, data_store in enumerate(self.data_stores):
            results = plot_utils.compute_metrics_over_range(data_store,
                                                            self.checked_transformations,
                                                            init_trans_params,
                                                            self.params_from_sliders['metric_params'],
                                                            self.checked_metrics,
                                                            pbar=self.pbar)
            self.metric_over_range_results.append(results)
            # see max metric values
            for _, item in results.items():
                for key2, item2 in item.items():
                    if '_range_values' not in key2:
                        for val in item2:
                            max_val = max(max_val, val)

        self.status_bar.showMessage('Done', 3000)
        self.data_lims['range_data'] = max_val

    '''
    metric range plot (line plots of range of all sliders)
    '''
    def display_metric_range_plot(self):
        trans_to_plot = list(self.checked_transformations.keys())[self.metric_range_graph_num]
        for i, data_store in enumerate(self.data_stores):
            axes = self.widget_row[i]['metrics']['range']['data']
            plot = plot_utils.get_transform_range_plots(self.metric_over_range_results[i], trans_to_plot, axes, self.plot_data_lim)
            plot.show()

    def change_metric_range_graph(self, add=1):
        max_graph_num = len(list(self.checked_transformations.keys()))
        self.metric_range_graph_num += add
        if self.metric_range_graph_num >= max_graph_num:
            self.metric_range_graph_num = max_graph_num - 1
        elif self.metric_range_graph_num < 0:
            self.metric_range_graph_num = 0
        self.display_metric_range_plot()

    '''
    metric averaging plots (radar plot)
    '''
    def display_metrics_over_range(self):
        # self.status_bar.showMessage('Getting avg. values')
        # QApplication.processEvents()
        for i, data_store in enumerate(self.data_stores):
            # uncomment below if you want to calc over the current trans values instead of init
            # results = plot_utils.compute_metrics_over_range(data_store,
            #                                                 self.checked_transformations,
            #                                                 self.params_from_sliders['transforms'],
            #                                                 self.params_from_sliders['metric_params'],
            #                                                 pbar=self.pbar)
            self.plot_metrics_graphs(self.metric_over_range_results[i], i)
        # self.status_bar.showMessage('Done', 3000)

    def plot_metrics_graphs(self, results, i):
        metrics_names = list(self.data_stores[i].metrics.keys())
        transformation_names = list(self.sliders['transforms'].keys())
        axes = self.widget_row[i]['metrics']['avg']['data']
        radar_plotter = plot_utils.get_radar_plots_avg_plots(results, metrics_names, transformation_names, axes, self.plot_data_lim)
        radar_plotter.show()

    '''
    metric image updaters
    '''
    def display_metric_images(self, metric_images, i):
        for key in metric_images:
            widget = self.widget_row[i]['metric_images'][key]['data']
            gui_utils.change_im(widget, metric_images[key], resize=self.image_display_size)
