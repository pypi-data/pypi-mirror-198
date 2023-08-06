'''
UI create widgets
'''
# Author: Matt Clifford <matt.clifford@bristol.ac.uk>
from functools import partial

import numpy as np
from PyQt6.QtWidgets import QPushButton, QLabel, QSlider, QCheckBox, QComboBox, QLineEdit
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt

import IQM_Vis
from IQM_Vis.UI.custom_widgets import ClickLabel
from IQM_Vis.utils import gui_utils, plot_utils, image_utils

# sub class used by IQM_Vis.main.make_app to initialise widgets and general UI functions for widgets
class widgets():
    def init_widgets(self):
        '''
        create all the widgets we need and init params
        '''
        # first setup the slider data
        self.sliders = {'transforms': {}, 'metric_params': {}}
        self._init_sliders(self.sliders['transforms'], self.checked_transformations, param_group='transforms')
        self._init_sliders(self.sliders['metric_params'], self.metric_params, param_group='metric_params')

        self.widget_row = {}
        for i, data_store in enumerate(self.data_stores):   # create each row of the widgets
            self.widget_row[i] = {'images':{}, 'metrics':{}, 'metric_images':{}}
            '''image and transformed image'''
            for image_name in ['original', 'transformed']:
                self.widget_row[i]['images'][image_name] = {}
                # image widget
                self.widget_row[i]['images'][image_name]['data'] = QLabel(self)
                self.widget_row[i]['images'][image_name]['data'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                # image label
                self.widget_row[i]['images'][image_name]['label'] = QLabel(self)
                self.widget_row[i]['images'][image_name]['label'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.widget_row[i]['images'][image_name]['label'].setText(image_name)

            '''metric images'''
            for metric_image in data_store.metric_images:
                if metric_image in self.checked_metric_images:
                    self.widget_row[i]['metric_images'][metric_image] = {}
                    self.widget_row[i]['metric_images'][metric_image]['data'] = QLabel(self)
                    self.widget_row[i]['metric_images'][metric_image]['data'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                    # image label
                    self.widget_row[i]['metric_images'][metric_image]['label'] = QLabel(self)
                    self.widget_row[i]['metric_images'][metric_image]['label'].setAlignment(Qt.AlignmentFlag.AlignCenter)

            '''metrics graphs'''
            im_pair_name = gui_utils.get_image_pair_name(data_store)
            self.widget_row[i]['metrics']['info'] = {}
            self.widget_row[i]['metrics']['info']['label'] = QLabel(self)
            self.widget_row[i]['metrics']['info']['label'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.widget_row[i]['metrics']['info']['label'].setText('Metrics '+im_pair_name)
            if self.metrics_info_format == 'graph':
                self.widget_row[i]['metrics']['info']['data'] = gui_utils.MplCanvas(self)
            else:
                self.widget_row[i]['metrics']['info']['data'] = QLabel(self)
                self.widget_row[i]['metrics']['info']['data'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.widget_row[i]['metrics']['info']['data'].setText('')
            # metrics avgerage graphs
            if self.metrics_avg_graph:
                self.widget_row[i]['metrics']['avg'] = {}
                self.widget_row[i]['metrics']['avg']['label'] = QLabel(self)
                self.widget_row[i]['metrics']['avg']['label'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.widget_row[i]['metrics']['avg']['label'].setText('IQM Averages')
                self.widget_row[i]['metrics']['avg']['data'] = gui_utils.MplCanvas(self, polar=True)
                self.widget_row[i]['metrics']['avg']['data'].setToolTip('Mean metric value over the range of each transform.')
            if self.metric_range_graph:
                self.widget_row[i]['metrics']['range'] = {}
                self.widget_row[i]['metrics']['range']['label'] = QLabel(self)
                self.widget_row[i]['metrics']['range']['label'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.widget_row[i]['metrics']['range']['label'].setText('Response Profiles')
                self.widget_row[i]['metrics']['range']['data'] = gui_utils.MplCanvas(self)
                self.widget_row[i]['metrics']['range']['data'].setToolTip('Single tranformation value range for all metrics.')

        '''buttons'''
        self.widget_controls = {'button': {}, 'slider': {}, 'label': {}, 'check_box': {}}
        self.widget_controls['button']['reset_sliders'] = QPushButton('Reset', self)
        self.widget_controls['button']['reset_sliders'].clicked.connect(self.reset_sliders)
        if self.metrics_avg_graph or self.metric_range_graph:
            # Update graphs
            self.widget_controls['button']['force_update'] = QPushButton('Update Graphs', self)
            self.widget_controls['button']['force_update'].setToolTip('Update graphs using all the current slider values.')
            self.widget_controls['button']['force_update'].clicked.connect(self.display_images)
            self.widget_controls['button']['force_update'].clicked.connect(self.redo_plots)
            # Change plot limits
            self.widget_controls['check_box']['graph_limits'] = QCheckBox('Squeeze plots')
            self.widget_controls['check_box']['graph_limits'].setToolTip('Set the scale of the plots to the metric data range.')
            self.widget_controls['check_box']['graph_limits'].setCheckState(Qt.CheckState.Unchecked)
            self.widget_controls['check_box']['graph_limits'].stateChanged.connect(self.change_plot_lims)

        if self.metric_range_graph:
            # buttons to control which graph to show
            self.widget_controls['button']['next_metric_graph'] = QPushButton('->', self)
            self.widget_controls['button']['next_metric_graph'].clicked.connect(partial(self.change_metric_range_graph, 1))
            self.widget_controls['button']['prev_metric_graph'] = QPushButton('<-', self)
            self.widget_controls['button']['prev_metric_graph'].clicked.connect(partial(self.change_metric_range_graph, -1))
        if self.dataset:
            # control what image is used from the dataset
            self.widget_controls['button']['next_data'] = QPushButton('->', self)
            self.widget_controls['button']['next_data'].clicked.connect(partial(self.change_data, 1))
            self.widget_controls['button']['prev_data'] = QPushButton('<-', self)
            self.widget_controls['button']['prev_data'].clicked.connect(partial(self.change_data, -1))
            self.widget_controls['label']['data'] = QLabel(self)
            self.widget_controls['label']['data'].setText('Change Image:')


        '''sliders'''
        self.params_from_sliders = {}
        for param_group, slider_group in self.sliders.items():
            self.params_from_sliders[param_group] = {}
            for key, item_sliders in slider_group.items():
                self.widget_controls['slider'][key] = {}
                self.widget_controls['slider'][key]['data'] = QSlider(Qt.Orientation.Horizontal)
                self.widget_controls['slider'][key]['data'].setMinimum(0)
                self.widget_controls['slider'][key]['data'].setMaximum(len(item_sliders['values'])-1)
                for func in item_sliders['value_change']:
                    self.widget_controls['slider'][key]['data'].valueChanged.connect(func)
                for func in item_sliders['release']:
                    self.widget_controls['slider'][key]['data'].sliderReleased.connect(func)
                self.params_from_sliders['transforms'][key] = item_sliders['init_ind']
                self.widget_controls['slider'][key]['label'] = QLabel(self)
                self.widget_controls['slider'][key]['label'].setAlignment(Qt.AlignmentFlag.AlignRight)
                self.widget_controls['slider'][key]['label'].setText(f"{key}:")
                self.widget_controls['slider'][key]['value'] = QLabel(self)
                self.widget_controls['slider'][key]['value'].setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.widget_controls['slider'][key]['value'].setText(str(self.params_from_sliders['transforms'][key]))

        self.set_image_name_text()
        self._init_experiment_widgets()

    def _init_experiment_widgets(self):
        self.widget_experiments = {'images': {}, 'preamble': {}}
        ''' pre experiments screen '''
        self.widget_experiments['preamble']['text'] = QLabel(self)
        self.widget_experiments['preamble']['text'].setText('Write info here about the experiment ...')
        self.widget_experiments['preamble']['start_button'] = QPushButton('Start', self)
        self.running_experiment = False
        self.widget_experiments['preamble']['start_button'].clicked.connect(self.toggle_experiment)

        ''' images '''
        for image in ['Reference', 'A', 'B']:
            self.widget_experiments['images'][image] = {}
            self.widget_experiments['images'][image]['data'] = ClickLabel(image)
            self.widget_experiments['images'][image]['data'].setAlignment(Qt.AlignmentFlag.AlignCenter)
            # image label
            self.widget_experiments['images'][image]['label'] = QLabel(image, self)
            self.widget_experiments['images'][image]['label'].setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_experiments['images']['A']['data'].clicked.connect(self.clicked_image)
        self.widget_experiments['images']['B']['data'].clicked.connect(self.clicked_image)

    '''
    setup/helper functions
    '''
    def _init_sliders(self, sliders_dict, info_dict, param_group):
        '''
        generic initialiser of sliders (will change the dicts input rather than returning - like C++ pointers &)
            sliders_dict: holds the slider widgets
            info_dict: info to initialise the sliders
        '''
        for key, info_item in info_dict.items():
            sliders_dict[key] = {}
            sliders_dict[key]['release'] = [self.display_images]
            sliders_dict[key]['value_change'] = [partial(self.generic_value_change, key, param_group), self.display_images]
            if 'function' in info_item.keys():
                sliders_dict[key]['function'] = info_item['function']
            if 'init_value' not in info_item.keys():
                info_item['init_value'] = 0
            if 'values' in info_item.keys():
                sliders_dict[key]['values'] = info_item['values']
            else:
                if 'num_values' not in info_item.keys():
                    info_item['num_values'] = 21   # make default value for steps in slider range
                sliders_dict[key]['values'] = np.linspace(info_item['min'], info_item['max'], info_item['num_values'])
                # see if we need to make odd numbers (for use with kernel sizes)
                if 'normalise' in info_item.keys():
                    if info_item['normalise'] == 'odd':
                        sliders_dict[key]['values'] = sliders_dict[key]['values'][sliders_dict[key]['values']%2 == 1]
                        info_item['num_values'] = len(sliders_dict[key]['values'])
            # get ind of the initial value to set the slider at
            sliders_dict[key]['init_ind'] = np.searchsorted(sliders_dict[key]['values'], info_item['init_value'], side='left')

    def _init_image_settings(self):
        self.widget_settings = {}

        # post processing
        self.post_processing_options = {'None': None,
                                        'Crop Centre': IQM_Vis.utils.image_utils.crop_centre}
        init_val = 'None'
        for i, data_store in enumerate(self.data_stores):
            if hasattr(data_store, 'image_post_processing'):
                if data_store.image_post_processing != None:
                    name = f"Custom {i}"
                    self.post_processing_options[name] = data_store.image_post_processing
                    init_val = name
        combobox = QComboBox()
        combobox.addItems(list(self.post_processing_options.keys()))
        combobox.setCurrentText(init_val)
        combobox.activated.connect(self.change_post_processing)
        self.widget_settings['image_post_processing'] = {'widget': combobox, 'label': QLabel('Image Post Processing:')}

        # image display size
        lineedit = QLineEdit()
        lineedit.setValidator(QIntValidator())
        lineedit.setMaxLength(3)
        lineedit.setText(str(self.image_display_size))
        lineedit.textChanged.connect(self.change_display_im_size)
        self.widget_settings['image_display_size'] = {'widget': lineedit, 'label': QLabel('Image Display Size:')}

    '''
    ==================== functions to bind to sliders/widgets ====================
    '''
    # sliders value changes
    def generic_value_change(self, key, param_group):
        index = self.widget_controls['slider'][key]['data'].value()
        self.params_from_sliders[param_group][key] = self.sliders[param_group][key]['values'][index]
        self.display_slider_num(key, param_group) # display the new value ont UI

    def display_slider_num(self, key, param_group, disp_len=5):
        # display the updated value
        value_str = str(self.params_from_sliders[param_group][key])
        value_str = gui_utils.str_to_len(value_str, disp_len, '0', plus=True)
        self.widget_controls['slider'][key]['value'].setText(value_str)

    def reset_sliders(self):
        for _, slider_group in self.sliders.items():
            for key, item_sliders in slider_group.items():
                self.widget_controls['slider'][key]['data'].setValue(item_sliders['init_ind'])
        self.display_images()
        self.redo_plots()

    def set_image_name_text(self):
        for i, data_store in enumerate(self.data_stores):
            self.widget_row[i]['images']['original']['label'].setText(data_store.get_reference_image_name())
            self.widget_row[i]['images']['transformed']['label'].setText(gui_utils.get_transformed_image_name(data_store))
            for metric_image in data_store.metric_images:
                if metric_image in self.checked_metric_images:
                    metric_name = gui_utils.get_metric_image_name(metric_image, data_store)
                    if len(metric_name) > 20:
                        metric_name = metric_image
                    self.widget_row[i]['metric_images'][metric_image]['label'].setText(metric_name)

    def change_plot_lims(self, state):
        if state == 2:  # 2 is the checked value
            self.plot_data_lim = self.data_lims['range_data']
        else:
            self.plot_data_lim = self.data_lims['fixed']
        self.redo_plots(calc_range=False)

    def change_post_processing(self, i):
        option = self.widget_settings['image_post_processing']['widget'].currentText()
        for data_store in self.data_stores:
            if hasattr(data_store, 'image_post_processing'):
                data_store.image_post_processing = self.post_processing_options[option]
        self.display_images()
        self.redo_plots()

    def change_display_im_size(self, txt):
        if txt == '':
            txt = 1
        old_size = self.image_display_size
        self.image_display_size = max(1, int(txt))
        # self.construct_UI()
        self.display_images()
        # if old_size > self.image_display_size:
        #     self.setMaximumSize(self.main_window.sizeHint())
        # if old_size < self.image_display_size:
        #     self.setMinimumSize(self.main_window.sizeHint())

    def update_progress(self, v):
        self.pbar.setValue(v)
        if v == 0:
            self.status_bar.showMessage('Done', 3000)

    def update_status_bar(self, v):
        self.status_bar.showMessage(v)

    def toggle_experiment(self):
        if self.running_experiment:
            self.reset_experiment()
            self.running_experiment = False
            self.widget_experiments['preamble']['start_button'].setText('Start')
        else:
            self.start_experiment()
            self.widget_experiments['preamble']['start_button'].setText('Reset')
            self.running_experiment = True

    def reset_experiment(self):
        self.init_style('light')
        self.menu_bar.setEnabled(True)

    def start_experiment(self):
        self.init_style('dark')
        self.menu_bar.setEnabled(False)
        self.experiments_tab.setCurrentIndex(1)
        self.experiment_transforms = plot_utils.get_all_single_transform_params(self.checked_transformations)


        ''' quick proto type to display some images '''
        ref = self.data_stores[0].get_reference_image()
        gui_utils.change_im(self.widget_experiments['images']['Reference']['data'], ref, resize=self.image_display_size)
        self.exp_im_ind = {'A': 0, 'B': len(self.experiment_transforms)//2}
        self.change_experiment_images(A_ind=self.exp_im_ind['A'], B_ind=self.exp_im_ind['B'])

    def change_experiment_images(self, A_ind, B_ind):
        A_trans = list(self.experiment_transforms[A_ind])[0]
        A = image_utils.get_transform_image(self.data_stores[0],
                                             {A_trans: self.checked_transformations[A_trans]},
                                             self.experiment_transforms[A_ind])
        B_trans = list(self.experiment_transforms[B_ind])[0]
        B = image_utils.get_transform_image(self.data_stores[0],
                                             {B_trans: self.checked_transformations[B_trans]},
                                             self.experiment_transforms[B_ind])

        gui_utils.change_im(self.widget_experiments['images']['A']['data'], A, resize=self.image_display_size)
        self.widget_experiments['images']['A']['data'].setObjectName(f'{self.data_stores[0].get_reference_image_name()}-{self.experiment_transforms[A_ind]}')
        gui_utils.change_im(self.widget_experiments['images']['B']['data'], B, resize=self.image_display_size)
        self.widget_experiments['images']['B']['data'].setObjectName(f'{self.data_stores[0].get_reference_image_name()}-{self.experiment_transforms[B_ind]}')

    def clicked_image(self, image_name, widget_name):
        print(f'clicked {widget_name}, name: {image_name}')
        self.exp_im_ind[widget_name] += 1
        if self.exp_im_ind[widget_name] == len(self.experiment_transforms):
            self.exp_im_ind[widget_name] -= 1
        self.change_experiment_images(A_ind=self.exp_im_ind['A'], B_ind=self.exp_im_ind['B'])
