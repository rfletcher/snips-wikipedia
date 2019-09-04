#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import sys

from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import wikipedia as wiki

def subscribe_intent_searchWikipedia(hermes, intentMessage):
    """
    :param hermes:
    :param intentMessage:
    :return:
    """
    if len(intentMessage.slots.article_indicator) > 0:
        article = intentMessage.slots.article_indicator.first().value
        wiki.set_lang('en')
        try:
            results = wiki.search(article, 5)
            lines = 2
            summary = wiki.summary(results[0], lines)
            if "==" in summary or len(summary) > 250:
                # We hit the end of the article summary or hit a really long
                # one.  Reduce to first line.
                lines = 1
                summary = wiki.summary(results[0], lines)

            summary = re.sub(r'\([^)]*\)|/[^/]*/', '', summary).encode('utf8')
            hermes.publish_end_session(intentMessage.session_id, summary)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            hermes.publish_end_session(intentMessage.session_id, "An error occured")
    else:
        hermes.publish_end_session(intentMessage.session_id, "An error occured")

if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("rfletcher:searchWikipedia", subscribe_intent_searchWikipedia).loop_forever()
