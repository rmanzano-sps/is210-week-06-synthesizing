#!/usr/bin/env python
# -*- utf-8 -*-
"""Send a reminder e-mail blast to each client.test"""

def prepare_email(appointments):
    greeting = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    new_email = [] 
    for info in appointments:
        add_info = greeting.format(info[0], info[1])
        new_email.append(add_info)
    return new_email
