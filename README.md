# Dirt simple analysis of a log file for message frequencies

It helps to see all the kinds of messages your logging produces, and get a sense of how frequent messages are.  This simple script does that.

I was going to do some sort of fancy clustering type thing, but then realized the vast majority of what you want to generalize over are the digits: the date, time, count, process id, user id, etc.  So right now this script is hardwired to abstract away digits (all digits) and simply count the resulting message types.

The output is sorted on message type, which should make it easy to compare multiple runs to identify new messages, or do month-to-month count comparisons, etc.


# Where I'd like this to go

There are lots more things one could do if you wanted to be intelligent about parsing log messages&mdash;but log message parsing is a large and well-traveled area, and I don't want to repeat that code.

Ideally, I'd add this functionality to an existing log viewing tool.  Most log viewers are extensible on the input or parsing side, but I have yet to find one that is extensible on the _analysis_ side.  If you know of one, let me know.   Or if there are already log viewers out there that have this built in, even better!