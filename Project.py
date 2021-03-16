import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('Which city would you like to choose? (Chicago, New York City, or Washington): ')

    while city not in ('Chicago','New York City','Washington'):
        print('invalid input! Please make sure to capitalize the initials!')
        city=input('What is the choice of your city(Chicago, New York City, or Washington): ')
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('What is the choice of your month? (All, January, February, March, April, May, June): ')

    while month not in ('All','January','February','March','April','May','June'):
        print('invalid input! Please make sure to capitalize the initials!')
        month=input('What is the choice of your month(All, January, February, March, April, May, June): ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What is the choice of your day of week?(All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ')
    while day not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        print('invalid input! Please make sure to capitalize the initials!')
        day = input('What is the choice of your day of week?(All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'All':
        months = ['January','February','March','April','May','June']
        month = months.index(month)+1
        df=df[df['month'] == month]
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].value_counts().idxmax()
    if common_month == 1:
       common_month = 'January'
    elif common_month == 2:
         common_month = 'February'
    elif common_month == 3:
         common_month = 'March'
    elif common_month == 4:
         common_month = 'April'
    elif common_month == 5:
         common_month = 'May'
    elif common_month == 6:
         common_month = 'June'

    print('The Chosen or the Most Common Month is: ',common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].value_counts().idxmax()
    print('The Chosen or the Most Common Day is: ',common_day)

    # TO DO: display the most common start hour
    df['Hour'] = pd.DatetimeIndex(df['Start Time']).hour
    common_start=df['Hour'].value_counts().idxmax()
    print('The Chosen or the Most Common Hour is: ',common_start)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    freq_start = df['Start Station'].value_counts().idxmax()
    print('The Most Commonly Used Start Station: ',freq_start)

    # TO DO: display most commonly used end station
    freq_end = df['End Station'].value_counts().idxmax()
    print('The Most Commonly Used End Station: ',freq_end)
    print()
    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The Most Frequent Combination of Start Station and End Station trip: ',combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('The Total Travel Time: ',total_time)
    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('The Mean Travel Time: ',avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count =df['User Type'].value_counts()
    subscriber = count['Subscriber']
    customer = count['Customer']
    print('Counts of Subscribers: ',subscriber)
    print('Counts of Customers: ',customer)
    print()
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        male = gender['Male']
        female = gender['Female']
        print('Counts of Male: ',male)
        print('Counts of Female: ',female)


        # TO DO: Display earliest, most recent, and most common year of birth
        early = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        most_year = df['Birth Year'].value_counts().idxmax()

        print('The Earliest Year of Birth',early)
        print('The Most Recent Year of Birth: ',recent)
        print('The Most Common Year of Birth: ',most_year)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        pass

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
