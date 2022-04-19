def flights(*args):
    count = 1
    all_flights = {}
    for command in args:
        if command == "Finish":
            return all_flights
        if count % 2 != 0:
            current_town = command
        elif count % 2 == 0:
            if current_town not in all_flights:
                all_flights[current_town] = 0
            all_flights[current_town] += int(command)
        count += 1


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
