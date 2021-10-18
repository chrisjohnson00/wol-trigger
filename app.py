from configurator.utility import get_config
import logging
import pulsar
from json import dumps
import pygogo as gogo

# logging setup
kwargs = {}
formatter = gogo.formatters.structured_formatter
logger = gogo.Gogo('struct', low_formatter=formatter).get_logger(**kwargs)


def send_message(message):
    pulsar_server = get_config('PULSAR_SERVER')
    pulsar_topic = get_config('PULSAR_TOPIC')
    if pulsar_server and pulsar_topic:
        client = pulsar.Client(f"pulsar://{pulsar_server}")
        producer = client.create_producer(pulsar_topic)
        producer.send(dumps(message).encode('utf-8'))
        logger.info("Message sent", extra={'message_body': message, 'topic': pulsar_topic})
        client.close()
    else:
        logger.warning("PULSAR_SERVER or PULSAR_TOPIC was not found in configs, no messages will be sent")


def main():
    # message = { 'name': 'nfs2',
    #                     'mac_address': 'b8:ca:3a:5d:28:b8',
    #                     'ip': '192.168.1.132',
    #                     'port': '22'
    #                   }
    message = {'name': get_config('COMPUTER_NAME'),
               'mac_address': get_config('MAC_ADDRESS'),
               'ip': get_config('IP_ADDRESS'),
               'port': get_config('PORT_NUMBER')}
    send_message(message)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting")
    main()
