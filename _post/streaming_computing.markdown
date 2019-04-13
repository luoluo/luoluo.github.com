---
layout: post
title: "MillWheel & Flink"
date: 2019-04-13 13:45
comments: true
categories: [BigData, Note]
---

####MillWheel

>MillWheel is a framework for building *low-latency* data-processing applications that is widely used at Google. Users specify a directed computation graph and application code for individual nodes, and the system manages *persistent state* and the *continuous flow* of records, all within the envelope of the framework’s *fault-tolerance guarantees*.

####概述
核心诉求：

1. Latency
2. Fault Tolerance
3. Scale
4. Versatile Programming Model(Persistent state/Low watermark/Window)

-----
1. Data should be available to consumers as soon as it is published
2. *Persistent state* abstractions should be available to user code, and should be integrated into the system’s overall consistency model.
3. *Out-of-order* data should be handled gracefully by the system.
4. A monotonically increasing *low watermark* of data timestamps should be computed by the system.
5. *Latency* should stay constant as the system scales to more machines.
6. The system should provide *exactly-once* delivery of records.

系统抽象

<div class="image-div"> <img class="content-image" src="/static/img/millwhell_overview.png" alt="x" width=450 /> </div>
1. inputs and outputs in MillWheel are represented by (key, value, timestamp) triples.
2. Delivery Guarantee: All internal updates within the MillWheel framework resulting from record processing are atomically checkpointed per-key and records are delivered exactly once.


####核心概念

Definition of a single node in a MillWheel topology

	computation SpikeDetector {
		input_streams {
			stream model_updates {
				key_extractor = 'SearchQuery'
			}
			stream window_counts {
				key_extractor = 'SearchQuery'
			}
		}
		output_streams {
			stream anomalies {
				record_format = 'AnomalyMessage'
			}
		}
	}

+ Computations
+ Keys
+ Streams
+ Persistent State
+ Low Watermarks
+ Timers

#####Computations
Application logic lives in computations, which encapsulate arbitrary user code.
Computation code is written to operate in the context of a single key, and is agnostic to the distribution of keys among different machines.

#####Keys
+ Keys are the primary abstraction for aggregation and comparison between different records in MillWheel. 
+ For every record in the system, the consumer specifies a key extraction function, which assigns a key to the record. 
+ Computation code is run in the context of a specific key and is only granted access to state for that specific key.
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_key2.png" alt="x" width=300 /> <img class="content-image" src="/static/img/millwhell_key1.png" alt="x" width=300 /> </div>
Per-key processing is serialized over time, such that only one record can be processed for a given key at once. Multiple keys can be run in parallel.
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_key1.png" alt="x" width=400 /> </div>
Multiple computations can extract different keys from the same stream. Key extractors are specified by the consumer of a stream.
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_key2.png" alt="x" width=400 /> </div>

#####Streams
Streams are the delivery mechanism between different computations in MillWheel.
A computation subscribes to zero or more input streams and publishes one or more output streams, and the system guarantees delivery along these channels.
Key-extraction functions are specified by each consumer on a per-stream basis, such that multiple consumers can subscribe to the same stream and aggregate its data in different ways.

#####Persistent State
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_state.png" alt="x" width=550 /> </div>
Persistent state in MillWheel is an opaque byte string that is managed on a per-key basis.
Persistent state is backed by a replicated, highly available data store (e.g. Bigtable [7] or Spanner [9]), which ensures data integrity in a way that is completely transparent to the end user. 
Common uses of state include counters aggregated over windows of records and buffered data for a join.

#####Low Watermarks
The low watermark for a computation provides a bound on the timestamps of future records arriving at that computation.
Low watermark values are seeded by injectors, which send data into MillWheel from external systems. 
Measurement of pending work in external systems is often an estimate, so in practice, computations should expect a small rate of late records – records behind the low watermark – from such systems.
Definition: 

	low watermark of A = min(oldest work of A, low watermark of C : C outputs to A)

#####Timers
Timers are per-key programmatic hooks that trigger at a specific wall time or low watermark value.
Timers are created and run in the context of a computation, and accordingly can run arbitrary code. 
Once set, timers are guaranteed to fire in increasing timestamp order. They are journaled in persistent state and can survive process restarts and machine failures. 
Timers are per-key programmatic hooks that trigger at a specific wall time or low watermark value. 

####API

	class Computation {
		// Hooks called by the system.
		void ProcessRecord(Record data);
		void ProcessTimer(Timer timer);

		// Accessors for other abstractions.
		void SetTimer(string tag, int64 time);
		void ProduceRecord(
			Record data, string stream);
		StateType MutablePersistentState();
	};

+ Computation API
+ Injector and Low Watermark API 

<div class="image-div"> <img class="content-image" src="/static/img/millwhell1.png" alt="x" width=500 /> </div>



####Fault Tolerance

+ Delivery Guarantees
+ + Exactly-Once Delivery 
+ + Strong Productions 
+ + Weak Productions and Idempotency
+ State Manipulation
+ Checkpoints

#####Exactly-Once Delivery 
Deliveries in MillWheel are retried until they are ACKed in order to meet our at-least-once requirement.
The system assigns unique IDs to all records at production time. We identify duplicate records by including this unique ID for the record in the same atomic write as the state modification.
Since we cannot necessarily store all duplication data in-memory, we maintain a Bloom filter of known record fingerprints, to provide a fast path for records that we have provably never seen before.

######Strong Productions 
Since MillWheel handles inputs that are not necessarily ordered or deterministic, we checkpoint produced records before delivery in the same atomic write as state modification.
We call this pattern of checkpointing before record production strong productions.

######Weak Productions and Idempotency
For weak productions, rather than checkpointing record productions before delivery, we broadcast downstream deliveries optimistically, prior to persisting state.
Empirically, this introduces a new problem, in that the completion times of consecutive stages of the pipeline are now strictly coupled as they wait for downstream ACKs of records. 
Combined with the possibility of machine failure, this can greatly increase end-to-end latency for straggler productions aspipeline depth increases.
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_fault_tolerance0.png" alt="x" width=400 /> </div>

#####Checkpoints
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_snapshot0.png" alt="x" width=550 /> </div>
Barrier separates the records in the data stream into the set of records that goes into the current snapshot, and the records that go into the next snapshot.
Each barrier carries the ID of the snapshot whose records it pushed in front of it. 
Barriers do not interrupt the flow of the stream and are hence very lightweight. 
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_snapshot1.png" alt="x" width=550 /> </div>

Operators that receive more than one input stream
As soon as the operator receives snapshot barrier n from an incoming stream, it cannot process any further records from that stream.
Streams that report barrier n are temporarily set aside. 
Once the last stream has received barrier n, the operator emits all pending outgoing records, and then emits snapshot n barriers itself.
After that, it resumes processing records from all input streams, processing records from the input buffers before processing the records from the streams.
<div class="image-div"> <img class="content-image" src="/static/img/millwhell_snapshot2.png" alt="x" width=550 /> </div>


####References

+ MillWheel: Fault-Tolerant Stream Processing at Internet Scale
+ Apache Flink™: Stream and Batch Processing in a Single Engine
+ Lightweight Asynchronous Snapshots for Distributed Dataflows
+ https://ci.apache.org/projects/flink/flink-docs-release-1.4/internals/stream_checkpointing.html#introduction

