# Objective

The objective of this exercise is to measure the response time trend of popular US retail websites during Thanksgiving and Black Friday 2019.

# Strategy

This experiment **will not inject load** to the websites under test. The script will **send only one HTTP(S) request every one hour** to measure the performance. The actual workload will be from the real users.

I will spin up an EC2 instance (free tier) from AWS in Ohio region and exeute the test. 

# Tools

Apache JMeter 5.2 will be used to design the test. CLI mode will be used for the actual run or Taurus might be used.

# Test Window

Test will start at 12.00 AM EST on Nov 28 and ends at 12.01 AM EST Nov 30.

# Results

Results will be published after collating the results tentatively by 06.00 PM EST on Nov 30.

# Performance Metrics

Results will feature the response time (Average, Min, Max, 95th percentile), Number of Transactions Passsed/Failed, and Throughput.
