import time
import pandas as pd

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

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    dow = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        try:
            city = input('Which city do you want to  explore?\n(chicago, new york city, washington)\n')
            if city in ['chicago','new york city','washington']:
                break
            else:
                print('Invalid input! Try again!')
                continue
        except:
            print('An error occured! Try again!')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('''Which month do you want to explore ?\n(all, january, february, march, april, may, june)\n''')
            if month in months:
                break
            else:
                print('Invalid input! Try again!')
                continue
        except:
            print('An error occured! Try again!')
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('''Which day do you want to explore ?\n(all, monday,..., sunday)\n''')
            if day in dow:
                break
            else:
                print('Invalid input! Try again!')
                continue
        except:
            print('An error occured! Try again!')
            continue

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        print('Most common month:', months[df['month'].mode()[0]-1].title(), df[df['month']==df['month'].mode()[0]].count()[0])

    # TO DO: display the most common day of week
    if day == 'all':
        print('Most common day of the week:', df['day_of_week'].mode()[0], df[df['day_of_week']==df['day_of_week'].mode()[0]].count()[0])

    # TO DO: display the most common start hour
    print('Most common start time:', df['Start Time'].dt.hour.mode()[0], df[df['Start Time'].dt.hour==df['Start Time'].dt.hour.mode()[0]].count()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station:', df['Start Station'].mode()[0], df[df['Start Station']==df['Start Station'].mode()[0]].count()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station:', df['End Station'].mode()[0], df[df['End Station']==df['End Station'].mode()[0]].count()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip', df.groupby(['Start Station','End Station']).size().idxmax(), df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of users:\n' + str(df['User Type'].value_counts()))

    if city in ['chicago', 'new york city']:

        # TO DO: Display counts of gender
        print('Counts of gender:\n' + str(df['Gender'].value_counts()))

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        print('Most common year of birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    i=0
    print(df.iloc[i:i+5])
    while True:
        try:
            x=input('Do you want to see the next 5 rows? (yes, no):')
            if x =='yes':
                i+=5
                try:
                    print(df.iloc[i:i+5])
                    continue
                except:
                    print('There are no rows left!')
                    break
            elif x=='no':
                break
            else:
                print('Wrong input! Try again!')
                continue
        except:
            print('An error occured! Try again!')
            continue

def main():
    while True:
        global city, month, day
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
