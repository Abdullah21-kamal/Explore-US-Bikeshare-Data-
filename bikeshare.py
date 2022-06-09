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
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    ##added
    city = input ('Which city would you like to see data from? chicago, new york city or washington?\n')
    repeat = 1
    city = city.upper()
    while repeat == 1:
        city = city.upper()
        if city == 'CHICAGO':
            city = 'chicago'
            repeat = 0
        elif city == 'NEW YORK CITY':
            city = 'new york city'
            repeat = 0
        elif city == 'WASHINGTON':
            city ='washington'
            repeat = 0
        else:
            city = input ('Incorrect input!! pleaase enter the city name again!! \n!')
            repeat = 1
    ##added

    # TO DO: get user input for month (all, january, february, ... , june)
    ##added:
    months_check = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month = input ('which month would you filter based on it? [january, february,..., june] enter it as a word!!  or enter "all" to consider all months!!\n' )
    repeat = 1
    month = month.lower()
    while repeat == 1:
        month = month.lower()
        if month in months_check:
            month = month
            repeat = 0
        else:
            month = input ('Incorrect input!! pleaase enter the month again!! \n!')
            repeat = 1
    ##added

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    ##added:
    days_check = ['monday', 'tuesday', 'wednesday', 'thursday', 'fraiday', 'saturday', 'sunday', 'all']
    day = input ('which day would you filter based on it? enter it as a word!! or enter "all" to consider all days!![monday, tuesday, ...] \n')
    repeat = 1
    day = day.lower()
    while repeat == 1:
        day = day.lower()
        if day in days_check:
            day = day
            repeat = 0
        else:
            day = input ('Incorrect input!! pleaase enter the day again!! \n!')
            repeat = 1
    #added
    

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
    ##added:
       
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df.month == month]
     
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week == day.title()]
    ##added

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    ##added:
    
    popular_month = df['month'].mode()[0]
    print('Most Frequent month:', popular_month)
    ##added
    
    # TO DO: display the most common day of week
    ##added:
    
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent day:', popular_day)
    ##added
    
    # TO DO: display the most common start hour
    ##added:
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    
    #popular_hour = (df['hour'].value_counts()).index[0]
    
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent Start Hour:', popular_hour)
    print('Count: ', df['hour'].value_counts()[popular_hour])
    ##added

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    ##added:
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)
    print('Count: ',df['Start Station'].value_counts()[popular_start_station] )
    ##added

    # TO DO: display most commonly used end station
    ##added:
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)
    print('Count: ',df['End Station'].value_counts()[popular_end_station] )
    ##added
    
    # TO DO: display most frequent combination of start station and end station trip
    ##added:
    df['frequent_combination'] = df['Start Station'] + '  >>>>  ' + df['End Station'] 
      
    most_frequent_combination = df['frequent_combination'].mode()[0]    
    print('the most Frequent Start Station:', most_frequent_combination)
    print('Count: ',df['frequent_combination'].value_counts()[most_frequent_combination] )
    ##added

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    df.drop('frequent_combination', axis = 1, inplace = True)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n....Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('The total travel time = ',df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print('The mean travel time = ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #added:
    print('the count of user type = ')
    print(df['User Type'].value_counts())
    #added
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Calculating the count of user gender = ')
        print('the coun of gender is: ')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('The most recent year of birth: ', df['Birth Year'][df['Birth Year'].idxmin()])


        print('The earliest year of birth: ', df['Birth Year'][df['Birth Year'].idxmax()])


        print('The most common year of birth: ', df['Birth Year'].mode()[0])
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        more = 'yes'
        see_rows = 0
        while(more == 'yes'):
            need_to_see_data = input('\nWould you like to see 5 rows from the data?!? Enter "yes" in lower case or any other word if "no"!!\n') 
            if need_to_see_data != 'yes':
                more = 'no'
            else:
                print(df.iloc[see_rows:see_rows + 5,:])
                see_rows += 5
        
        restart = input('\nWould you like to restart? Enter yes or no!!\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
