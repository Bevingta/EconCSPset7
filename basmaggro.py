#!/usr/bin/env python

import sys

from gsp import GSP
from util import argmax_index

class BasmAggro:
    """Balanced bidding agent"""
    def __init__(self, id, value, budget):
        self.id = id
        self.value = value
        self.budget = budget

    def initial_bid(self, reserve):
        return self.value / 2


    def slot_info(self, t, history, reserve):
        """Compute the following for each slot, assuming that everyone else
        keeps their bids constant from the previous rounds.

        Returns list of tuples [(slot_id, min_bid, max_bid)], where
        min_bid is the bid needed to tie the other-agent bid for that slot
        in the last round.  If slot_id = 0, max_bid is 2* min_bid.
        Otherwise, it's the next highest min_bid (so bidding between min_bid
        and max_bid would result in ending up in that slot)
        """
        prev_round = history.round(t-1)
        other_bids = [a_id_b for a_id_b in prev_round.bids if a_id_b[0] != self.id]

        clicks = prev_round.clicks
        def compute(s):
            (min, max) = GSP.bid_range_for_slot(s, clicks, reserve, other_bids)
            if max == None:
                max = 2 * min
            return (s, min, max)
            
        info = list(map(compute, list(range(len(clicks)))))
#        sys.stdout.write("slot info: %s\n" % info)
        return info


    def expected_utils(self, t, history, reserve):
        """
        Figure out the expected utility of bidding such that we win each
        slot, assuming that everyone else keeps their bids constant from
        the previous round.

        returns a list of utilities per slot.
        """
        # TODO: Fill this in
        # compute position effect: pos_1 = c_1/c_1, pos_2 = c_2/c_1, ... pos_m = c_m/c_1
        # not sure if correct, but at least gives an idea of
        # how effective each position is wrt to each other
        clicks = history.round(t-1).clicks
        position_effect = [_ / clicks[0] for _ in clicks]
        """
        Calculating utilities: Expected value of pos k is:
        position_effect[k] * (v_i - min_bid_k)
        In GSP, we pay min_bid_k (min_bid to get k last round) and we expect value based on 
        the position effect therein
        """
        info = self.slot_info(t, history, reserve)
        utilities = []   # Change this
        for slot in range(len(info)):
            # factoring in reserve price, must pay at least rp, otherwise no alloc
            # so if min_bid > rp, normal
            # if rp inbetween min & max, we have to at least pay rp
            # and if rp > max, no alloc and on utility
            min_bid = info[slot][1]
            max_bid = info[slot][2]
            if min_bid > reserve:
                utilities.append(position_effect[slot] * (self.value - info[slot][1]))
            elif max_bid > reserve > min_bid:
                utilities.append(position_effect[slot] * (self.value - reserve))
            else:  # reserve > max_bid
                utilities.append(0)  # no allocation

        return utilities

    def target_slot(self, t, history, reserve):
        """Figure out the best slot to target, assuming that everyone else
        keeps their bids constant from the previous rounds.

        Returns (slot_id, min_bid, max_bid), where min_bid is the bid needed to tie
        the other-agent bid for that slot in the last round.  If slot_id = 0,
        max_bid is min_bid * 2
        """
        i =  argmax_index(self.expected_utils(t, history, reserve))
        info = self.slot_info(t, history, reserve)
        return info[i]

    def bid(self, t, history, reserve):
        # The Balanced bidding strategy (BB) is the strategy for a player j that, given
        # bids b_{-j},
        # - targets the slot s*_j which maximizes his utility, that is,
        # s*_j = argmax_s {clicks_s (v_j - t_s(j))}.
        # - chooses his bid b' for the next round so as to
        # satisfy the following equation:
        # clicks_{s*_j} (v_j - t_{s*_j}(j)) = clicks_{s*_j-1}(v_j - b')
        # (p_x is the price/click in slot x)
        # If s*_j is the top slot, bid the value v_j

        (slot, min_bid, max_bid) = self.target_slot(t, history, reserve)

        # TODO: Fill this in.
        bid = 0  # change this

        """
            bidding max_bid - 1 in order to drain other players
        """
        if slot != 0 and min_bid < self.value:
            bid = max_bid - 1
        else:  # j == 0 or min_bid > self.value
            bid = self.value
        
        return bid

    def __repr__(self):
        return "%s(id=%d, value=%d)" % (
            self.__class__.__name__, self.id, self.value)
