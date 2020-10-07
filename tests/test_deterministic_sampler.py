import unittest

from opentelemetry.ext.honeycomb.sampling import DeterministicSampler
from opentelemetry.sdk.trace.sampling import Decision

class TestDeterministicSampler(unittest.TestCase):

    def test_always_sample(self):
        sampler = DeterministicSampler(1)
        result = sampler.should_sample(None, 12345, "foo", None, ())
        self.assertEqual(result.decision, Decision.RECORD_AND_SAMPLE)
