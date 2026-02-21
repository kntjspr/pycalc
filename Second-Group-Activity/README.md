Members:
Boniel, Gerald
Lerio, Jars Christian
Sisi, Kent Jasper
Sorongon, Charles Juvanne



Real-World Bottleneck: Internet Café Printing Queue



Real-World Bottleneck Discovery
In many internet cafés, printing services are handled by a single staff member. Customers send their files to one computer, and the staff prints each document one by one. The same person also handles checking the file, setting the print format, and collecting payment.
The main bottleneck is that only one worker processes all print jobs sequentially. Even if multiple computers and printers are available, the workflow remains linear because tasks are not distributed.
This limits efficiency because customers must wait in line even if their print jobs are small. During peak hours, delays increase, and the queue becomes longer. The system cannot scale because the workload depends entirely on one processing unit.
This scenario mainly fits data parallelism since printing multiple documents involves performing the same operation on different files. Each document can be processed independently if multiple workers or threads are available.
