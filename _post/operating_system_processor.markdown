---
layout: post
title: "Operating System Processor Summary V0.1"
date: 2019-08-11 10:53
comments: true
categories: [OS]
---

#### Shared-memory multiporcessor:

+ SMP(symmetric multiprocessors / centralized shared-memeory multiprocessor) => UMA(uniform memory access)
<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_smp.png" alt="x" width=500 /> </div>

+ DSM(distributed shard memory) => NUMA(nonuniform memory access)
<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_dsm.png" alt="x" width=650 /> </div>

#### Coherence vs Consistency
+ Coherence Defines the behavior of reads and writes to the same memory location.
+ Consistency defines the behavior of reads and writes with respect to accesses to other memory locations.

#### Coherence Protocols
+ Snooping
+ * MSI
+ * MESI
+ * MOESI
+ Directory based

#### Snooping coherence protocol example
+ State(MSI):
+ * Invalid
+ * Shared
+ * Modified

<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_snooping1.png" alt="x" width=650 /> </div>
<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_snooping2.png" alt="x" width=650 /> </div>
<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_snooping3.png" alt="x" width=450 /> </div>

#### Directory-based coherence protocol example
<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_directory_based1.png" alt="x" width=500 /> </div>
<div class="image-div"> <img class="content-image" src="/static/img/os_multicore_directory_based2.png" alt="x" width=450 /> </div>

#### Memory consistency models
+ Sequential consistency
+ Processor consistency
+ Relaxed consistency

#### Synchronization
+ Automic operation: single uninterruptible instruction
+ Conditional store: piar of instructions (load locked / store conditional)

####Reference:
[Computer Architecture: A Quantitative Approach 5th Edition](https://www.amazon.com/Computer-Architecture-Quantitative-John-Hennessy/dp/012383872X)  
[Intel i7-4770 (Haswell) performance](https://www.7-cpu.com/cpu/Haswell.html)  
[Understanding CPU caching and performance](https://arstechnica.com/gadgets/2002/07/caching/)  
[Computer memory history](https://www.computerhope.com/history/memory.htm)
