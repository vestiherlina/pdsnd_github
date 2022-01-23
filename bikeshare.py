import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #city input
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('That\'s not a valid city!!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        #time_filter input
        while True:
            time_filter = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter\n').lower()
            if time_filter == 'month' or time_filter == 'day' or time_filter == 'both' or time_filter == 'none':
                break
            else:
                print('Input is not valid! Filter by month, day, both, or none!!')
        #month filter input
        if time_filter == 'month':
            #month input
            while True:
                month = input('Which month? January, February, March, April, May or June?\n').lower()
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                    break
                else:
                    print('Incorrect month!')
            day = 'all'
            break
        #none filter input
        elif time_filter == 'none':
            month = 'all'
            day = 'all'
            print('No filter time!')
            break
        #day filter input
        elif time_filter == 'day':
            month = 'all'
            #day input
            while True:
                try:
                    day = int(input('Which day?Please type your response with integer (e.g., 1=Monday).\n'))
                    if day >= 1 and day <= 7:
                        break
                    else:
                        print('Input day (int) within range 1 to 7!')
                except:
                    print('Input day (int) within range 1 to 7!')
            break
        #both filter input
        else:
            #month input
            while True:
                month = input('Which month? January, February, March, April, May or June?\n').lower()
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                    break
                else:
                    print('Incorrect month!')
            #day input
            while True:
                try:
                    day = int(input('Which day?Please type your response with integer (e.g., 1=Monday).\n'))
                    if day >= 1 and day <= 7:
                        break
                    else:
                        print('Input day (int) within range 1 to 7!')
                except:
                    print('Input day (int) within range 1 to 7!')
            break
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month
    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == ((day)-1)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    count_month = df['month'].value_counts()[common_month]
    print('Most common month:', common_month)
    print('count of common month: ', count_month)

    # TO DO: display the most common day of week
    common_day = df['day'].value_counts().idxmax()
    count_day = df['day'].value_counts()[common_day]
    print('Most common day:', common_day)
    print('count of common day: ', count_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].value_counts().idxmax()
    count_hour = df['hour'].value_counts()[common_hour]
    print('Most common hour:', common_hour)
    print('count: ', count_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most common start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most common end station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most frequent combination station: ', combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    count_duration = df['Trip Duration'].count()
    print('Total travel time: ', total_duration, 'seconds.')
    print('Count: ', count_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Average travel time: ', mean_duration, 'seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Type:\n', user_types)

    # TO DO: Display counts of gender

    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('User Gender:\n', gender)
    else:
        print('Gender column has not found!')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].value_counts().idxmax()
        print('Earliest birth year of user:', earliest)
        print('Most recent birth year of user:', most_recent)
        print('Most common birt year of user:', most_common)
    else:
        print('Birth Year column has not found!')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw(df):
    while True:
        viewdata = input('Do you want to see the raw data? Enter "yes" or "no"!\n').lower()
        if viewdata in ('yes','no'):
            break
        else:
            print('Invalid input!')

    start_loc = 0
    while True:
        if viewdata == "yes":
            end_loc = start_loc + 5
            data_slice = df.iloc[start_loc:end_loc]
            print(data_slice)
            start_loc += 5
            while True:
                viewdata = input('Do you want to see the raw data? Enter "yes" or "no"!\n').lower()
                if viewdata in ('yes','no'):
                    break
                else:
                    print('Invalid input!')
        else:
            break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
