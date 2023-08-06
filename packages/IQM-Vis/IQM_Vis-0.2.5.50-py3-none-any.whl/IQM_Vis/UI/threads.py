''' thread and signal classes to makethe UI smoother
    useful info about PyQt6 threads: https://www.pythontutorial.net/pyqt/pyqt-qthread/'''
# Author: Matt Clifford <matt.clifford@bristol.ac.uk>
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from IQM_Vis.utils import plot_utils


class get_range_results_worker(QObject):
    progress = pyqtSignal(int)
    completed = pyqtSignal(dict)

    @pyqtSlot(dict)
    def do_work(self, data):
        metric_over_range_results = []
        max_val = 0
        self.stop_flag = [False]
        for i, data_store in enumerate(data['data_stores']):
            results = plot_utils.compute_metrics_over_range(data_store,
                                                            data['trans'],
                                                            data['init_trans'],
                                                            data['metric_params'],
                                                            data['metrics_to_use'],
                                                            pbar_signal=self.progress,
                                                            stop_flag=self.stop_flag)
            if self.stop_flag[0] == True:
                return
            metric_over_range_results.append(results)
            # see max metric values
            for _, item in results.items():
                for key2, item2 in item.items():
                    if '_range_values' not in key2:
                        for val in item2:
                            max_val = max(max_val, val)
        data_return = {'metric_over_range_results': metric_over_range_results,
                       'max_val': max_val}
        self.completed.emit(data_return)

    def stop(self):
        if hasattr(self, 'stop_flag'):
            self.stop_flag[0] = True
