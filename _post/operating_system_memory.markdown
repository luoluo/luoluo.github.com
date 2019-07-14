---
layout: post
title: "Operating System Memory Summary V0.3"
date: 2019-07-01 19:53
comments: true
categories: [OS]
---

####Overview
<div class="image-div"> <img class="content-image" src="/static/img/memory_overview.png" alt="x" width=550 /> </div>

#### Memory Technology:

+ SRAM
+ * use six transistors per bit to prevent the information from being disturbed when read; don't need refresh
+ * L1 L2 L3 cache
+ DRAM
+ * requires data to be written back after being read; need refresh
+ * main memory
+ SDRAM
+ * have a programmable register to hold the number of bytes requested, and hence can send many bytes over several cycles per request
+ DDR
+ * double data rate
+ * transfer data on both the rising edge and falling edge of the DRAM clock signal
+ FLASH Memory
+ * Flash memory is a type of EEPROM (Electronically Erasable ProgrammableRead-Only Memory),
+ * normally read-only but can be erased
+ * it holds it contents without any power
+ HDD

####Summary
<div class="image-div"> <img class="content-image" src="/static/img/memory_summary.png" alt="x" width=650 /> </div>

#### Summary of 10 advanced cache optimization
<div class="image-div"> <img class="content-image" src="/static/img/cache_opt.png" alt="x" width=650 /> </div>

#### The Intel Core i7's Cache

The i7 supports the x86-64 instruction set architecture, a 64-bit extension of the 80x86 architecture. The i7 is an out-of-order execution processor that includes four cores.

Each core in an i7 can execute up to four 80x86 instructions per clock cycle, using a multiple issue, dynamically scheduled, 16-stage pipeline. 

The i7 can also support up to two simultaneous threads per processor, using a technique called simultaneous multithreading

The i7 can support up to three memory channels, each consisting of a separate set of DIMMs, and each of which can transfer in parallel. Using DDR3-1066 (DIMM PC8500), the i7 has a peak memory bandwith of just over 25 GB/sec

i7 uses 48-bit virtual addresses and 36-bit physical addresses, yielding a maximum physical memory of 36 GB. Memory management is handled with a twolevel TLB.
<div class="image-div"> <img class="content-image" src="/static/img/intel_i7_tlb.png" alt="x" width=500 /> </div>

i7’s three-level cache hierarchy. The first-level caches are virtually indexed and physically tagged, while the L2 and L3 caches are physically indexed.
<div class="image-div"> <img class="content-image" src="/static/img/intel_i7_cache.png" alt="x" width=500 /> </div>

<div class="image-div"> <img class="content-image" src="/static/img/intel_i7.png" alt="x" width=650 /> </div>

####Reference:
[Computer Architecture: A Quantitative Approach 5th Edition](https://www.amazon.com/Computer-Architecture-Quantitative-John-Hennessy/dp/012383872X)  
[Intel i7-4770 (Haswell) performance](https://www.7-cpu.com/cpu/Haswell.html)  
[Understanding CPU caching and performance](https://arstechnica.com/gadgets/2002/07/caching/)  
[Computer memory history](https://www.computerhope.com/history/memory.htm)
