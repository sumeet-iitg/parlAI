# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
"""Agent does gets the local keyboard input in the act() function.
   Example: python examples/eval_model.py -m local_human -t babi:Task1k:1 -dt valid
"""

from parlai.core.agents import Agent
from parlai.core.worlds import display_messages
import random

class DumbChatAgent(Agent):

    def __init__(self, opt, shared=None):
        super().__init__(opt)
        self.id = 'dumbChat'
        self.episodeDone = False
        self.msgCount = 0
        self.prevResponseIndex = -1

    def observe(self, msg):
        self.observation = msg
        return msg

    def act(self):
        obs = self.observation
        responses = ["What do you think?", "How should I know? I am dumb!", "I am sad :(", "I am happy :)"]
        reply = {}
        reply['id'] = self.getID()
        reply['episode_done'] = False
        if self.msgCount == 0:
            reply_text = "Hi! I am dumb chatbot."
            self.msgCount += 1
        elif '[DONE]' in obs:
            reply['episode_done'] = True
            self.episodeDone = True
            reply_text = "Bye, it was nice chatting!"
        else:
            indices = list(range(0, len(responses)))
            if self.prevResponseIndex != -1:
                indices.remove(self.prevResponseIndex)
            random_index = random.choice(indices)
            reply_text = responses[random_index]
            self.prevResponseIndex = random_index
        reply['text'] = reply_text
        return reply

    def episode_done(self):
        return self.episodeDone
