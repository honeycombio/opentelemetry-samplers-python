# opentelemetry-samplers-python

[![OSS Lifecycle](https://img.shields.io/osslifecycle/honeycombio/opentelemetry-samplers-python)](https://github.com/honeycombio/home/blob/main/honeycomb-oss-lifecycle-and-practices.md)

**STATUS: this project is [archived](https://github.com/honeycombio/home/blob/main/honeycomb-oss-lifecycle-and-practices.md).** You can learn more about sampling with OpenTelemetry in our [docs](https://docs.honeycomb.io/getting-data-in/opentelemetry/python/#sampling).

Questions? You can chat with us in the **Honeycomb Pollinators** Slack. You can find a direct link to request an invite in [Spread the Love: Appreciating Our Pollinators Community](https://www.honeycomb.io/blog/spread-the-love-appreciating-our-pollinators-community/).

---

**NOTE**: This is experimental and is subject to change a _lot_ or go away entirely. Use with caution.

Honeycomb Samplers for use with the OpenTelemetry Python SDK

## Samplers

### Deterministic Sampler

This is a port of the deterministic sampler included in our [Python Beeline](https://github.com/honeycombio/beeline-python). To use it, just instantiate it with a sample rate:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
from opentelemetry.ext.honeycomb.sampling import DeterministicSampler

sampler = DeterministicSampler(5) # every trace has a 20% chance of being sampled
trace.set_tracer_provider(TracerProvider(sampler=sampler))

trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("Test span"):
    with tracer.start_as_current_span("bar"):
        with tracer.start_as_current_span("baz"):
            print("Hello world from OpenTelemetry Python!")
```
