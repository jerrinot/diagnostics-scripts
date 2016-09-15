#!/usr/bin/python

from hzdiag.simplemtricplotter import SimpleMetricPlotter

pending_invocations_template = """
<html>
    <head>
        <title>Simple Metrics</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
    <body>
        <h1>Metrics</h1>
        {{#data}}
            <h2>{{name}}</h2>
            {{{plot}}}
        {{/data}}
    </body>
</html>
"""

# SimpleMetricPlotter('operation.invocations.pending').plot(pending_invocations_template)
SimpleMetricPlotter([   'operation.completedCount',
                        'operation.queueSize',
                        'operation.priorityQueueSize',
                        'operation.responseQueueSize',
                        'operation.runningPartitionCount',
                        'operation.runningGenericCount',
                        'operation.invocations.responses[normal]',
                        'operation.invocations.responses[backup]',
                        'operation.invocations.responses[error]',
                        'operation.invocations.responses[missing]',
                        'operation.invocations.responses[timeout]',
                        'cluster.clock.clusterTimeDiff',
                        'event.eventQueueSize',
                        'event.totalFailureCount',
                        'executor.[hz:async].completedTaskCount',
                        'executor.[hz:client].completedTaskCount',
                        'executor.[hz:scheduled].completedTaskCount',
                        'partitions.replicaSyncRequestsCounter',
                        'gc.majorTime',
                     ]).plot(pending_invocations_template)
