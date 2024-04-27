TASK1
run the executable file on terminal1 the the below command on terminal 2:
    sudo tcpdump -i any port 587 -w capture.pcap
open capture.pcap with wireshark to get the password in human redable form
run the below command to decode it 
    echo "(thepswd)" | base64 -d

Task2