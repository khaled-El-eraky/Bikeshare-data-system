import time
import pandas as pd
import numpy as np

"""Cities_File dictionary"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

"""Function of getting raw input Form User"""
def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # Getting user input for city (chicago, new york city, washington)
    city = input("To view the spicified bikeshare data choose a city from: \n- chicago \n- new york city\n- washington\n" ).lower()
    # Input validation
    while city not in CITY_DATA.keys():
        print("This is invalid input! \nTry it again\n")
        city = input("To view the spicified bikeshare data choose a city from: \n- chicago \n- new york city\n- washington\n" ).lower()

    # Getting user input for month (all, january, february, ... , june)
    month = input("To filter {}'s data by a specific month please select the month or all to show all months\n- january\n- february\n- march\n- april\n- may\n- june\n- all\n\n".format(city)).lower()

    # Getting user input for day of week (all, monday, tuesday, ... sunday)
    day = input("To filter {}'s data by a specific day please select the day or all to show all days \n- monday\n- tuesday\n- wednesday\n- thursday\n- friday\n- saterday\n- sunday\n- all\n\n".format(city)).lower()

    print('-'*40)
    return city, month, day
#------------------------------------------------------

"""Function for loadind data from the choosen city file"""
def load_data(city, month, day):
    # Read the City file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])
    # convert start time into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Creat new columns of month and day of week from start time
    df['months'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.day_name()

    #check if the user need month filter or not
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # Filter by month and creat new date farme
        df = df[df['months'] == month]

    #check if the user need day filter or not
    if day != 'all':
        # Filter by day and creat new date farme
        df = df[df['Day_of_week'].str.startswith(day.title())]

    return df
#------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    print(df['months'].mode()[0])

    # Display the most common day of week
    print(df['Day_of_week'].mode()[0])

    # Display the most common start hour
    df['Hours'] = df['Start Time'].dt.hour
    print(df['Hours'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    print("The most commonly used start station: ", df['Start Station'].mode()[0])

    # Display most commonly used end station
    print("The most commonly used end station: ", df['End Station'].mode()[0])

    # Display most frequent combination of start station and end station trip
    print("frequent combination of start station and end station trip: ", df.groupby(['Start Station' , 'End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#------------------------------------------------------


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print("The total travel time: ", df['Trip Duration'].sum())

    # Display mean travel time
    print("The mean travel time: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    if 'Gender' in df:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        print(df['User Type'].value_counts())

        # Display counts of gender
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print("The earliest year of birth: ", int(df['Birth Year'].min()))
        print("The most recent year of birth: ", int(df['Birth Year'].max()))
        print("The most common year of birth: ", int(df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

def display_data(df):
    """Display rows of data as much as usr want"""
    show_data = input("Do you want to see the first 5 rows of data?\nEnter yes or no\n").lower()
    start_loc = 0
    while show_data == 'yes':
        print(df.iloc[start_loc : start_loc+5])
        start_loc += 5
        show_data = input("Do you want to see the next 5 rows of data?\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
