import random
import numpy as np
from collections import deque
from rl.policy import Policy, LinearAnnealedPolicy


class BinnedLinAnnPolicy(LinearAnnealedPolicy):

    """
    LinearAnnealedPolicy for Binned Curriculum Learning

    Description
        The intention of designing this module is to run the existing LinearAnnealedPolicy repeatedly within an interval.
        Specifically, the attr value is repeatedly annealed from value_max to value_min within the interval of steps defined by bins.

        Once all the parameters are defined, a pattern of attr value shows below:
            step 0 ~ int(bins[0] * decreasing_ratio) : attr goes down from value_max to value_min
            step int(bins[0] * decreasing_ratio) ~ bins[0] : attr = value_min
            step bins[i] ~ int(bins[i] + (bins[i + 1] - bins[i]) * decreasing_ratio) : attr goes down AGAIN from value_max to value_min
            ...
            step bins[-1] ~ bins[-1] + nb_steps : attr goes down AGAIN from value_max to value_min
            step bins[-1] + nb_steps ~ inf : attr = value_min

    Parameters
    ----------
    inner_policy : Type[Policy]
        Policy object that chooses agent's action
    attr : str
        A name of instance variable within the inner_policy to be annealed
    value_max : float
        Maximum value of attr variable
    value_min : float
        Minimum value of attr variable
    value_test : float
        Test value of attr variable (constant)
    nb_steps : int
        Annealing steps at last phase
    decreasing_ratio : float
        Ratio of step lengths that are annealed within an interval. Definitely it should between 0.0 and 1.0.
    bins : list[int]
        List of interval boundaries. DO NOT INCLUDE 0 and inf.
    
    Reference
    ---------
    https://github.com/tensorneko/keras-rl2
        See help(rl.policy.LinearAnnealedPolicy).
    """

    def __init__(self, inner_policy, attr, value_max, value_min, value_test, nb_steps, decreasing_ratio, bins):
        super(BinnedLinAnnPolicy, self).__init__(inner_policy, attr, value_max, value_min, value_test, nb_steps)
        self.decreasing_ratio = decreasing_ratio
        self.bins = [0] + bins
        return

    def get_current_value(self):
        if self.agent.training:
            idx = sum([int(int(self.agent.step) >= bin_) for bin_ in self.bins])
            upper = self.bins[idx]
            lower = self.bins[idx - 1]
            if idx == len(self.bins) - 1:
                landing_step = self.nb_steps
            else:
                landing_step = int((upper - lower) * self.decreasing_ratio)
            a = -float(self.value_max - self.value_min) / float(landing_step)
            b = float(self.value_max)
            value = max(self.value_min, a * float(self.agent.step - lower) + b)
        else:
            value = self.value_test
        return value


class InferencePolicy(Policy):

    """
    Policy to Apply to Actual Sokovan Episode

    Description
        It is a policy module for using in the actual application, not for a learning purpose. Note that
        it is difficult to apply this module to keras-rl2 as it is. The basic process is structured to
        select and return the appropriate action when it receives the q_values list, but the rule is added
        to supplement the player's selection. The rule details are as follows:
            1. Search where the player can actually move. For example, if there is a wall in the "up"
               direction of the player and nothing in the others, the result is ["down", "left", "right"].
            2. If the player can't move anywhere, apply greedy-Q policy (this case is unlikely to happen
               logically, but it can happen sometimes if sampler's parameters are too complex and the
               sampler accidentally samples bad case).
            3. If the now-state has already been repeated in the past state as much as the pre-specified
               (response_maxlen - 1), sample one of the movable actions to prevent repeated vain efforts
               of the player, since it is obvious that the model would have given the same action a high
               Q-value. The method of sampling is to softmax transform q-values and use them as weights.
            4. If it does not belong to any of the cases 2. ~ 3., select the action with the highest
               q-value from the movable action.
    
    * Note : self.recent_history contains information about the past state. If the episodes are reset,
             you must delete them by calling the self.reset_recent_history function at the top of the code.
    
    Parameters
    ----------
    rule : bool
        If True, the rule applies. If False, self.select_action is just same as greed-Q policy.
    recent_maxlen : int
        The number of steps to be considered the past states.
    """

    def __init__(self, rule=True, recent_maxlen=5):
        self.rule = rule
        self.recent_maxlen = recent_maxlen
        self.recent_history = deque(maxlen=self.recent_maxlen)
        return
    
    def select_action(self, q_values, env):
        if not self.rule:
            action = q_values.argmax()
        else:
            # Renew recent state history
            self.recent_history.append(env.now_state.copy())

            # Get only movable actions
            player_position = env.now_state['player_position']
            box_position = env.now_state['box_position']
            action_idx = []
            for action, action_str in env.action_decoder.items():
                movable = env.mover.is_movable(player_position, box_position, action_str)
                if movable:
                    action_idx.append(action)
            
            if len(action_idx) == 0:
                # There is no movable action - just argmax Q-values
                action = q_values.argmax()
            elif len(action_idx) == 1:
                # There is the only one movable action - choose it
                # TODO : Delete this condition
                action = action_idx[0]
            elif self.recent_history[-1] in list(self.recent_history)[:-1]:
                # If state repeats - sample new action based on q-value
                q_values_exp = np.exp(q_values[0, action_idx])
                prob = q_values_exp / q_values_exp.sum()
                action = random.choices(action_idx, weights=prob, k=1)[0]
            else:
                # Otherwise, select the action with the highest q-value among the movable actions
                action_list = [action for action in q_values.argsort()[0] if action in action_idx]
                action = action_list[-1]
        
        return action
    
    def reset_recent_history(self, recent_maxlen=None):
        if recent_maxlen is not None:
            self.recent_maxlen = recent_maxlen
        self.recent_history = deque(maxlen=self.recent_maxlen)
        return
