from parse import parse
from datetime import datetime
import plotly as py
import pystache
import os
import formic
from pkg_resources import resource_string

class SimpleMetricPlotter:
    def __init__(self, metrics):
        self.metrics = metrics


    def parse_invocations_from_diagnostics_file(self, filename, metric):
        state = dict()
        for line in open(filename):
            line = line.strip()
            if "Metrics[" in line:
                timestamp_string = parse("{} Metrics[", line)[0]
                timestamp = datetime.strptime(timestamp_string, '%d-%m-%Y %H:%M:%S')
            elif metric in line:
                line = parse(metric + "={}", line)
                pending_string = line[0].replace(',','')
                count = int(pending_string)
                state[timestamp] = count
        return state


    def parse_files(self, filenames, parser, metric):
        state = dict()
        for filename in filenames:
            current_state = parser(filename, metric)
            state.update(current_state)
        return state


    def create_all_series(self, all_states) :
        allSeries = []
        for member_state in all_states:
            member = member_state['member']
            state = member_state['state']
            sorted_timestamps = sorted(state.keys())
            values = []
            for timestamp in sorted_timestamps:
                values.append(state[timestamp])
            currentSerie = {'x': sorted_timestamps, 'y': values, 'fill': 'tozeroy', 'name': member}
            allSeries.append(currentSerie)
        return allSeries


    def create_plot_html_markup_for_invocations(self, all_files, metric):
        states = []
        for member in all_files:
            current_member_files = all_files[member]
            state = self.parse_files(current_member_files, self.parse_invocations_from_diagnostics_file, metric)
            states.append({'member': member,
                           'state': state})

        all_series = self.create_all_series(states)
        s = py.offline.plot(all_series, show_link=False, output_type='div', include_plotlyjs=False)
        return s


    # key = member
    # value = list of file for a given member
    def find_diagnostics_files(self):
        files = dict()
        fileset = formic.FileSet(include="**/diag*.log", directory=".")
        for currentFile in fileset:
            basename = os.path.basename(currentFile)
            member = parse("diagnostics-{}-{}-{}.log", basename)[0]
            files.setdefault(member,[]).append(currentFile)
        return files

    def get_plotlyjs(self):
        path = os.path.join('offline', 'plotly.min.js')
        plotlyjs = resource_string('plotly', path).decode('utf-8')
        return plotlyjs


    def plot(self, template):
        all_files = self.find_diagnostics_files()
        plots = []
        for metric in self.metrics:
            plots.append({'name': metric, 'plot': self.create_plot_html_markup_for_invocations(all_files, metric)});
        print pystache.render(template, {'data': plots, 'plotly' : self.get_plotlyjs()})
