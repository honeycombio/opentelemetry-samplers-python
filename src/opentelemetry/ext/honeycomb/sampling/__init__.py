import hashlib

from typing import Optional, Sequence

from opentelemetry.sdk.trace import sampling
from opentelemetry.util.types import Attributes

class DeterministicSampler(sampling.Sampler):
    def __init__(self, rate: int):
        if rate < 1:
            raise ValueError("SampleRate must be greater than zero")
        self.rate = rate
        self.upper_bound = MAX_INT32 / rate

    def should_sample(
        self,
        parent_context: Optional["SpanContext"],
        trace_id: int,
        name: str,
        attributes: Attributes = None,
        links: Sequence["Link"] = (),
    ) -> "SamplingResult":
        decision = sampling.Decision.DROP
        sha1 = hashlib.sha1()
        sha1.update(trace_id.encode('utf-8'))
        value, = struct.unpack('>I', sha1.digest()[:4])
        if value < self.upper_bound:
            decision = sampling.Decision.RECORD_AND_SAMPLE
        if decision is sampling.Decision.DROP:
            return sampling.SamplingResult(decision)
        return sampling.SamplingResult(decision, attributes)
