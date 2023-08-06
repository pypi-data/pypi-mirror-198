import json
import os.path
import ssl
import sys
import time
from configparser import ConfigParser

import requests

from pts_cli.bap import BetterArgumentParser
import act.parser as act

import paho.mqtt.client as mqtt

_host = None
_apikey = None
done = False
has_failed = False


def init(host=None, apikey=None):
    config_path = os.path.expanduser(os.path.join(os.getenv("XDG_CONFIG_HOME", "~/.config"), "pts-cli"))
    os.makedirs(config_path, exist_ok=True)

    config_file_path = os.path.join(config_path, 'cli.ini')
    config = ConfigParser()
    config.read(config_file_path)

    if not config.has_section('central'):
        if host is None:
            print("Central controller hostname (without https://): ")
            host = input()
        config.add_section('central')
        config.set('central', 'host', host)

        if apikey is None:
            print("API Key: ")
            apikey = input()

        config.set('central', 'apikey', apikey)

    with open(config_file_path, 'w') as handle:
        config.write(handle)

    global _host
    global _apikey

    _host = config.get('central', 'host')
    _apikey = config.get('central', 'apikey')


def submit(manifest, note, follow, print_jid=False):
    init()

    # Make sure the manifest exists
    if not os.path.isfile(manifest):
        sys.stderr.write(f"File not found: {manifest}\n")
        exit(1)

    with open(manifest, 'r') as handle:
        manifest = handle.read()

    # Make sure there's no syntax errors in the manifest
    act.parse(manifest)

    # Submit
    url = f'https://{_host}/api/v1/jobs'
    payload = {'manifest': manifest}
    if note is not None:
        payload['note'] = note
    response = requests.post(url, json=payload, headers={
        'Authorization': f'Bearer {_apikey}'
    })

    # Count a redirect as login failure
    if len(response.history) > 0:
        sys.stderr.write("API key invalid\n")
        exit(3)

    if response.status_code != 200:
        sys.stderr.write("API error:\n")
        sys.stderr.write(response.content.decode() + "\n")
        exit(4)

    result = response.json()
    if print_jid:
        print(result['id'])
        exit(0)

    print(f"Job submitted as {result['link']}")

    if follow:
        globals()['follow'](result['id'])


def follow(jid):
    init()
    url = f'https://{_host}/api/v1/jobs/{jid}'
    response = requests.get(url, headers={
        'Authorization': f'Bearer {_apikey}'
    })
    job = response.json()

    if job['status'] in ['cancelled', 'success', 'failed', 'timeout']:
        sys.stderr.write(f"This job is already {job['status']}")
        exit(1)

    tids = set()
    for task in job['tasks']:
        tids.add(task['id'])

    if len(job['tasks']) == 1:
        # Follow single task job
        display_log = True
    else:
        sys.stderr.write(f"Job is running on multiple devices, not showing streaming output")
        display_log = False

    proto, host, prefix, _, _, _ = job['tasks'][0]['log_topic']['host']
    client = mqtt.Client(reconnect_on_failure=True)
    port = 1883
    if proto == 'mqtts':
        context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
        client.tls_set_context(context)
        port = 8883

    def on_connect(*args):
        for task in job['tasks']:
            print("Subscribe to ", task['log_topic']['path'])
            client.subscribe(task['log_topic']['path'])

    client.on_connect = on_connect
    client.connect(host, port=port)

    global done
    global has_failed
    done = False
    has_failed = False

    def on_message(client, userdata, message):
        global done
        global has_failed
        topic = message.topic

        tid = int(topic.split('/')[2])
        log = json.loads(message.payload)

        if 'r' in log:
            if log['r']:
                print(f"Task {tid} succeeded")
            else:
                sys.stderr.write(f"Task {tid} failed\n")
                has_failed = True
            tids.remove(tid)

            if len(tids) == 0:
                done = True
            return

        if display_log:
            line = ''
            if 's' in log:
                line += log['s'] + " | "
            line += log['l']
            if 'e' in log and log['e']:
                sys.stderr.write(line + "\n")
            else:
                print(line)

    client.on_message = on_message
    client.loop_start()

    while not done:
        time.sleep(0.2)

    if has_failed:
        exit(1)


def main():
    import argparse

    parser = BetterArgumentParser(description="End-user CLI utility for the Phone Test System",
                                  formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(dest='command', required=True, title='sub-commands:',
                                       description="These are the subcommands implemented,"
                                                   "choose one of the list below")

    initcmd = subparsers.add_parser('init', help="Initial set-up of connection info")
    initcmd.add_argument('--host', help="Hostname of the PTS central controller")
    initcmd.add_argument('--api-key', help="API Key for auth", dest="apikey")

    submitcmd = subparsers.add_parser('submit', help="Submit a new job")
    submitcmd.add_argument('manifest', help="Manifest file")
    submitcmd.add_argument('--note', '-m', help="Add a note to the job")
    submitcmd.add_argument('--follow', '-f', help="Stay connected and show job log output", action='store_true')
    submitcmd.add_argument('--print-jid', help="Print job id instead of user friendly output", dest="print_jid",
                           action="store_true")

    followcmd = subparsers.add_parser('follow', help="Follow and wait on the completion of a submitted job")
    followcmd.add_argument('jid', type=int, help="Job ID to follow")

    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('command')](**kwargs)


if __name__ == '__main__':
    main()
