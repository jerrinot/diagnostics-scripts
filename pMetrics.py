#!/usr/bin/python

from hzdiag.simplemtricplotter import SimpleMetricPlotter

pending_invocations_template = """
<html>
    <head>
        <title>Simple Metrics</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
    <body>
        <a id="toc">
            <h1>Metrics</h1>
        <a/>
        <ul>
            {{#data}}
                <li><a href="#{{name}}">{{name}}</a>
            {{/data}}
        </ul>
        {{#data}}
            <a id="{{name}}"><h2>{{name}}</h2></a>
            {{{plot}}}
            <a href="#toc">[Table of Content]</a>
        {{/data}}
    </body>
</html>t
"""

# SimpleMetricPlotter('operation.invocations.pending').plot(pending_invocations_template)
SimpleMetricPlotter([   'operation.completedCount',
                        'operation.queueSize',
                        'operation.priorityQueueSize',
                        'operation.responseQueueSize',
                        'operation.runningPartitionCount',
                        'operation.runningGenericCount',
                        'operation.invocations.pending',
                        'operation.invocations.responses[normal]',
                        'operation.invocations.responses[backup]',
                        'operation.invocations.responses[error]',
                        'operation.invocations.responses[missing]',
                        'operation.invocations.responses[timeout]',
                        'operation.invocations.heartbeatPacketsReceived',
                        'operation.invocations.backupTimeouts',
                        'cluster.clock.clusterTimeDiff',
                        'event.eventQueueSize',
                        'event.totalFailureCount',
                        'executor.[hz:async].completedTaskCount',
                        'executor.[hz:client].completedTaskCount',
                        'executor.[hz:scheduled].completedTaskCount',
                        'partitions.replicaSyncRequestsCounter',
                        'gc.majorTime',
                     ]).plot(pending_invocations_template)
