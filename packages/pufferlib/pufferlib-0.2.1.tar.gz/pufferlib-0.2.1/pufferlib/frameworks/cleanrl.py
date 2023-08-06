from pdb import set_trace as T

import torch
from torch.distributions import Categorical

import pufferlib
import pufferlib.models
import pufferlib.frameworks.base


def make_policy(policy_cls, lstm_layers=0):
    '''Wrap a PyTorch model for use with CleanRL

    Args:
        policy_cls: A pufferlib.models.Policy subclass that implements the PufferLib model API
        lstm_layers: The number of LSTM layers to use. If 0, no LSTM is used

    Returns:
        A new PyTorch class wrapping your model that implements the CleanRL API
    '''
    assert issubclass(policy_cls, pufferlib.models.Policy)
    if lstm_layers > 0:
        policy_cls = pufferlib.frameworks.base.make_recurrent_policy(
            policy_cls, batch_first=False)

    class CleanRLPolicy(policy_cls):
        '''Temporary hack to get framework running with CleanRL

        Their LSTMs are kind of weird. Need to figure this out'''
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _compute_hidden(self, x, lstm_state=None):
            if lstm_layers > 0:
                batch_size = lstm_state[0].shape[1]
                x = x.reshape((-1, batch_size, x.shape[-1]))
                hidden, state, lookup = self.encode_observations(x, lstm_state)
                return hidden, state
            else:
                hidden, _ = self.encode_observations(x)

            return hidden

        # TODO: Cache value
        def get_value(self, x, lstm_state=None, done=None):
            if lstm_layers > 0:
                hidden, lstm_state = self._compute_hidden(x, lstm_state)
            else:
                hidden = self._compute_hidden(x, lstm_state)
            return self.critic(hidden)

        # TODO: Compute seq_lens from done
        def get_action_and_value(self, x, lstm_state=None, done=None, action=None):
            if lstm_layers > 0:
                hidden, lstm_state = self._compute_hidden(x, lstm_state)
            else:
                hidden = self._compute_hidden(x, lstm_state)

            value = self.critic(hidden)
            flat_logits = self.decode_actions(hidden, None, concat=False)

            multi_categorical = [Categorical(logits=l) for l in flat_logits]

            if action is None:
                action = torch.stack([c.sample() for c in multi_categorical])
            else:
                action = action.view(-1, action.shape[-1]).T

            logprob = torch.stack([c.log_prob(a) for c, a in zip(multi_categorical, action)]).T.sum(1)
            entropy = torch.stack([c.entropy() for c in multi_categorical]).T.sum(1)

            return action.T, logprob, entropy, value, lstm_state
   
    return CleanRLPolicy
