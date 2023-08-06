import argparse
import yaml
import requests
import os
import configparser
import time

def orchestrate(filename):
    # Load the API key and secret from the configuration file
    config_file = os.path.join(os.path.expanduser("~"), ".plutis-cli")
    if not os.path.exists(config_file):
        print("Please authenticate first using 'plutis authenticate --api_key <api_key> --api_secret <api_secret>'")
        return

    config = configparser.ConfigParser()
    config.read(config_file)
    api_key = config.get("plutis", "api_key")
    api_secret = config.get("plutis", "api_secret")

    # Read the YAML file
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    # Send the dictionary as a POST request
    url = "https://api.plutis.io/api/v1/orchestration/create"
    headers = {
        "x-api-key": api_key,
        "x-api-secret": api_secret,
    }
    response = requests.post(url, json=data, headers=headers)

    # Print the response
    if response.status_code == 200:
        print("Orchestration created successfully.")
        res = response.json()
        print(f"\n\nYou can listen to events using 'plutis listen --job_id {res['job_id']}'.")
    else:
        res = response.json()
        print(f"Error in orchestrating stack: {res.message}")

def listen(job_id):
    # Load the API key and secret from the configuration file
    config_file = os.path.join(os.path.expanduser("~"), ".plutis-cli")
    if not os.path.exists(config_file):
        print("Please authenticate first using 'plutis authenticate --api_key <api_key> --api_secret <api_secret>'")
        return

    config = configparser.ConfigParser()
    config.read(config_file)
    api_key = config.get("plutis", "api_key")
    api_secret = config.get("plutis", "api_secret")

    # Send the dictionary as a POST request
    url = f"https://api.plutis.io/api/v1/orchestration/logs?job_id={job_id}"
    headers = {
        "x-api-key": api_key,
        "x-api-secret": api_secret,
    }
    response = requests.get(url, headers=headers)

    # Print the response
    if response.status_code == 200:
        print("Listening for events...\n\nEvents:\n")
        # grab all events thus far
        res = response.json()
        status = res["status"]
        events = res["events"]
        for event in events:
            print(f"{event}\n")
        # keep listening for events
        first_time_queued = True
        total_events = len(events)
        while status != "completed":
            # wait five seconds before polling for more events
            time.sleep(5)
            # check for new events
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                res = response.json()
                print(f"Error in listening for events: {res.message}")
                return
            res = response.json()
            status = res["status"]
            events = res["events"]
            if status == "pending":
                if len(events) > total_events:
                    for event in events[total_events:]:
                        print(f"{event}\n")
                    total_events = len(events)
            if status == "queued":
                if first_time_queued:
                    print("Orchestration job is queued. Waiting for it to start...")
                    first_time_queued = False
        print("Orchestration job completed successfully.")
    else:
        res = response.json()
        print(f"Error in listening for events: {res.message}")


def authenticate(api_key, api_secret):
    config = configparser.ConfigParser()
    config["plutis"] = {"api_key": api_key, "api_secret": api_secret}

    config_file = os.path.join(os.path.expanduser("~"), ".plutis-cli")
    with open(config_file, "w") as file:
        config.write(file)

    print("API key and secret saved successfully.")

def main():
    parser = argparse.ArgumentParser(description="Plutis CLI tool")
    subparsers = parser.add_subparsers(dest="command")
    
    # Orchestrate command
    orchestrate_parser = subparsers.add_parser("orchestrate", help="Process a YAML file and orchestrate the stack")
    orchestrate_parser.add_argument("--yaml", type=str, required=True, help="The YAML file to process")

    # Listen command
    authenticate_parser = subparsers.add_parser("listen", help="Listen for events for a particular orchestration job")
    authenticate_parser.add_argument("--job_id", type=str, required=True, help="The orchestration job ID")

    # Authenticate command
    authenticate_parser = subparsers.add_parser("authenticate", help="Register the API key and secret")
    authenticate_parser.add_argument("--api_key", type=str, required=True, help="The API key")
    authenticate_parser.add_argument("--api_secret", type=str, required=True, help="The API secret")

    args = parser.parse_args()

    if args.command == "orchestrate":
        orchestrate(args.yaml)
    elif args.command == "listen":
        listen(args.job_id)
    elif args.command == "authenticate":
        authenticate(args.api_key, args.api_secret)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
