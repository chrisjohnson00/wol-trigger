# wol-trigger
A small app which is used as part of a k8s cronjob to send a message destined for my WOL microservice

## Project dependencies

    pip install --upgrade pip
    pip install --upgrade pulsar-client fastavro pygogo python-consul
    pip freeze > requirements.txt
    sed -i '/pkg_resources/d' requirements.txt


## Required ENV Vars

 - `COMPUTER_NAME` The name of the computer to wake up
 - `MAC_ADDRESS` The MAC address of the computer to wake up
 - `IP_ADDRESS` The IP address of the computer to wake up
 - `PORT_NUMBER` The port number to use for verification of readyness after wakeup
 - `PULSAR_SERVER` The hostname/ip for Pulsar
 - `PULSAR_TOPIC` The topic to send the wakeup message to
