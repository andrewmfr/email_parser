#reads through txt file, looks at hour (of day) an email was sent
#and creates distribution based on the number of emails sent each hour


#opens file
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time_dict = dict()

#reads through text, determines hour email was sent and how many
# emails were sent at that hour
for line in handle :
    if not line.startswith("From") : continue
    line = line.rstrip()
    word_list = line.split()
    time = word_list[5:6]
    if len(time) > 0 :
        hour = (time[0].split(':')[0])
        time_dict[hour] = time_dict.get(hour, 0) + 1

#returns tuple sorted by hour and number of email sent at that hour
for (k, v) in sorted(time_dict.items()) :
    print(k, v)
