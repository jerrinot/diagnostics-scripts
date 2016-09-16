#!/bin/sh

output_dir=plots

red='\033[0;31m'
nc='\033[0m'

if [ $# -gt 1 ]; then
    echo Usage: pAll.sh [force]
    exit 1
fi

argument=${1:-default}
if [ $argument = "force" ]; then
    rm -rf ./"$output_dir"
fi

if [ -d "$output_dir" ]; then
    echo "Directory ${red}`pwd`/$output_dir${nc} already exists. Start pass the start as \"pAll.sh force\" to regenerate plots"
    exit 2
fi

mkdir plots
echo Plotting Pending Invocations
pInvoc.py > ./$output_dir/pending_invocations.html
echo Plotting Metrics
pMetrics.py > ./$output_dir/metrics.html

echo Metric plotting completed. Now you can server them over HTTP by running \"pPublish.py\"