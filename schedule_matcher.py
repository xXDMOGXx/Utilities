from os.path import exists

schedule_file = "CS1200GroupSchedule.txt"
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
names_list = []
times_list = []


def load_schedule_file(file_name):
    if not exists(file_name):
        print("File "+file_name+" does not exist")
        return False
    file = open(file_name, 'r')
    count = -1
    for line in file:
        char = line[0]
        if char == 'n':
            line = line[3:-1]
            names_list.append(line)
            times_list.append([])
            count += 1
        elif len(line) > 1:
            line = line[5:-1]
            if line == "N/A":
                times_list[count].append([])
            else:
                day_intervals = []
                option_split = line.split(", ")
                for option in option_split:
                    interval_split = option.split("-")
                    intervals = []
                    interval_placement = 0
                    for interval in interval_split:
                        if interval == "noon":
                            intervals.append(12)
                        elif interval == "midnight":
                            if interval_placement == 0:
                                intervals.append(0)
                            else:
                                intervals.append(24)
                        else:
                            time_split = interval.split(":")
                            time = float(time_split[0])
                            minutes = time_split[1]
                            time += (float(minutes[0:2]) / 60)
                            if time_split[1][-2] == 'p':
                                time += 12
                            intervals.append(time)
                        interval_placement += 1
                    day_intervals.append(intervals)
                times_list[count].append(day_intervals)
    file.close()


def return_perms(day_intervals):
    lists = day_intervals
    final_list = []
    for i in range(len(lists[0])):
        for ii in range(len(lists[1])):
            final_list.append([lists[0][i], lists[1][ii]])
    for l in range(len(lists)-2):
        inter_list = []
        for i in range(len(final_list)):
            for ii in range(len(lists[l+2])):
                inter_list.append(final_list[i] + [lists[l+2][ii]])
        final_list = inter_list
    return final_list


def find_overlap_times(perms):
    overlap_times = []
    for p in range(len(perms)):
        start_times = []
        end_times = []
        for i in range(len(perms[p])):
            start_times.append(perms[p][i][0])
            end_times.append(perms[p][i][1])
        start_times.sort(reverse=True)
        end_times.sort()
        start = start_times[0]
        end = end_times[0]
        if end > start:
            overlap_times.append([start, end])
    return overlap_times


def main():
    load_schedule_file(schedule_file)
    num_people = len(names_list)
    for d in range(len(day_list)):
        day_times_list = []
        print(day_list[d] + ": ")
        for i in range(num_people):
            day_times_list.append(times_list[i][d])
        perms = return_perms(day_times_list)
        overlaps = find_overlap_times(perms)
        num_overlaps = len(overlaps)
        if num_overlaps > 0:
            for i in range(num_overlaps):
                t = []
                for time in overlaps[i]:
                    minutes = str(round((time % 1) * 60))
                    if minutes == "0":
                        minutes += "0"
                    time = int(time)
                    if time >= 12:
                        time -= 12
                        minutes += "pm"
                    else:
                        minutes += "am"
                    hour = str(time)
                    t.append([hour, minutes])
                if i+1 != num_overlaps:
                    print(", "+t[0][0]+":"+t[0][1]+" - "+t[1][0]+":"+t[1][1])
                else:
                    print(str(t[0][0])+":"+str(t[0][1])+" - "+str(t[1][0])+":"+str(t[1][1]))
        else:
            print("No Times")


main()
