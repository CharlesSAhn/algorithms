'''

Sort the schedule, and make sure when a train arrives or depart, keep track of the required number of platforms.
We will have iterator i and j traversing the arrival and departure lists respectively. At any moment, the difference (i - j) will provide us the required number of platforms.

At the time of either arrival or departure of a train, if i^th arrival is scheduled before the j^th departure,
increment the platform_required and i as well. Otherwise, decrement platform_required count, and increase j. Keep track of the max value of platform_required ever, as the expected result.
'''


def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    arrival.sort()
    departure.sort()

    arrival_index = 0
    departure_index = 0
    max_platforms = 0
    current_platforms = 0

    while arrival_index < len(arrival) and departure_index < len(departure):

        if arrival[arrival_index] < departure[departure_index]:
            current_platforms += 1
            arrival_index += 1

            if current_platforms > max_platforms:
                max_platforms = current_platforms

        elif arrival[arrival_index] > departure[departure_index]:
            current_platforms -= 1
            departure_index += 1

        else:
            departure_index  +=1
            arrival_index += 1

    return max_platforms



arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arrival, departure))


arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
print(min_platforms(arrival, departure))