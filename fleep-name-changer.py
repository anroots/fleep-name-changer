#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Randomly assign oneself middle names in Fleep

Based on https://github.com/anroots/spotify-fleep-nowplaying
Author: ando@sqroot.eu 2016-05-25
Licence: MIT

Usage example (change Fleep display name every 30 seconds):

▶ ./fleep-name-updater.py --email=<fleep-email> --password='<fleep-password>' --sleep-duration=30 --prefix=Ando --suffix=Roots
Starting polling. Hit CTRL+C to stop.
[ok]: Ando "Mad" Roots
[ok]: Ando "The Silencer" Roots
[ok]: Ando "Dark" Roots
"""

import random
import requests
import json
import time
import click
import sys

# Set up CLI usage
@click.command()
@click.option('--email', prompt='Email', help='Your Fleep account email')
@click.option(
    '--sleep-duration', default=60,
    help='How many seconds to wait between status updates')
@click.option('--prefix', default='Ando', help='Name prefix (First Name)')
@click.option('--suffix', default='Roots', help='Name suffix (Last Name)')
@click.option('--password', prompt='Password', help='Your Fleep account password')

def main(email, password, sleep_duration, prefix, suffix):

    # Login to Fleep
    credentials = login(email, password)
    if not credentials:
        click.echo('Invalid credentials, unable to login.', err=True)
        sys.exit(1)

    click.echo('Starting polling. Hit CTRL+C to stop.')

    while True:
        new_name = "%s \"%s\" %s" % (prefix, get_middle_name(), suffix)

        # Update display name on Fleep
        if update_name(credentials, new_name):
            click.echo("[ok]: %s" % new_name)
        else:
            click.echo('Fleep API responded with an error', err=True)

        time.sleep(sleep_duration)

def login(email, password):
    """Login to Fleep, return session information"""
    response = requests.post(
        "https://fleep.io/api/account/login",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"email": email, "password": password})
        )
    if response.status_code is not 200:
        return False
    data = response.json()
    return {
        'ticket': data["ticket"],
        'token_id':response.cookies["token_id"],
        'display_name': data['display_name']
    }


def get_middle_name():
    clever_names = [
      'The Doctor',
      'Annoyed',
      'PHP',
      'Mr-Know-It-All',
      'Grumpy',
      'Whichdoctor',
      'Quick Shot',
      'Security',
      'Tokenizer',
      'Punisher',
      'Funny',
      'Lannister',
      'The Silencer',
      '#kickban',
      'The Janitor',
      'The Gray',
      'Who?',
      'Gentleman',
      'Azog',
      'Dark',
      'The Immutable',
      '#oldschool',
      'The Dark',
      '<?var_dump()?>',
      'Robert\'); DROP TABLE students;--',
      'The Wizard',
      'Clever',
      'Creepy',
      'Mad',
      'Mad',
      'Mad',
      'Coder',
      'Java'
    ]
    return random.choice(clever_names)

def update_name(credentials, name):
    """Change display name in Fleep"""
    response = requests.post(
        "https://fleep.io/api/account/configure",
        headers={"Content-Type": "application/json"},
        cookies={"token_id": credentials['token_id']},
        data=json.dumps({"display_name": name, "ticket": credentials['ticket']})
        )
    return response.status_code == 200


if __name__ == '__main__':
    main()