#!/usr/bin/python

from parse import parse
from datetime import datetime
import plotly as py
import pystache
import os
import formic


def parse_invocations_from_diagnostics_file(filename):
    state = dict()
    inside_history = False
    for line in open(filename):
        line = line.strip()
        if "Invocations[" in line:
            timestamp_string = parse("{} Invocations[", line)[0]
            timestamp = datetime.strptime(timestamp_string, '%d-%m-%Y %I:%M:%S')
            state[timestamp] = dict()
        elif line == "History[":
            inside_history = True
        elif "[" in line:
            inside_history = False
        elif inside_history:
            ops = parse("{} samples={}", line)
            operation = ops[0]
            count = int(ops[1].rstrip(']'))
            current_tick = state[timestamp]
            current_tick[operation] = count
    return state


def parse_files(filenames, parser):
    state = dict()
    for filename in filenames:
        current_state = parser(filename)
        state = dict(current_state.items() + state.items())
    return state


def calculate_top_operations(state):
    last_timestamp = max(state.keys())
    last_tick = state[last_timestamp]
    top_operations = []
    for w in sorted(last_tick, key=last_tick.get, reverse=True):
        if len(top_operations) < 10:
            top_operations.append(w)
    return top_operations


def create_series_map(state, top_operations):
    sorted_timestamps = sorted(state.keys())
    series = dict()
    for timestamp in sorted_timestamps:
        operations = state[timestamp]
        for current_operation in top_operations:
            count = operations.get(current_operation, 0)
            series.setdefault(current_operation, []).append(count)
    return series


def create_all_series(sorted_timestamps, series) :
    allSeries = []
    for operation in series:
        values = series[operation]
        currentSerie = {'x': sorted_timestamps, 'y': values, 'fill': 'tozeroy', 'name': operation}
        allSeries.append(currentSerie)
    return allSeries


def create_plot_html_markup_for_invocations(files):
    state = parse_files(files, parse_invocations_from_diagnostics_file)

    top_operations = calculate_top_operations(state)
    series = create_series_map(state, top_operations)
    sorted_timestamps = sorted(state.keys())
    all_series = create_all_series(sorted_timestamps, series)
    s = py.offline.plot(all_series, show_link=False, output_type='div')
    return s


# key = member
# value = list of file for a given member
def find_diagnostics_files():
    files = dict()
    fileset = formic.FileSet(include="**/diag*.log", directory=".")
    for currentFile in fileset:
        basename = os.path.basename(currentFile)
        member = parse("diagnostics-{}-{}-{}.log", basename)[0]
        files.setdefault(member,[]).append(currentFile)
    return files


def plotInvocations(template):
    all_files = find_diagnostics_files()
    plots = []
    for current_member in all_files:
        member_files = all_files[current_member]
        plot = create_plot_html_markup_for_invocations(member_files)
        plots.append({'name': current_member, 'plot': plot})
    print pystache.render(template, {'data': plots})


invocation_history_template = """
<html>
    <head>
        <title>Invocations Analysis</title>
        </head>
    <body>
        <h1> Invocation History per Member </h1>
        {{#data}}
            <h2>{{name}}</h2>
            {{{plot}}}
        {{/data}}
    </body>
</html>
"""


plotInvocations(invocation_history_template)