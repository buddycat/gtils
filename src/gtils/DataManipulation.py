from datetime import datetime, timedelta

class DataManipulation:
    ''' Instantiates a number of helpful data manipulation tools.'''

    def __init__(self):
        pass

    def human_dates(self, date_value):
        '''This function will convert unix datetime stamps into 
        human readable format. This function can be used directly on an int,
        a string containing an int, list if iterated, etc. 
        
        You can call this function on a whole Pandas dataframe by using
        df = df.applymap(human_dates) 
        (keep in mind this may modify other 10-digit numbers if they are 
        the only contents of a cell)

        Or call it on a specific field by using
        df['field_name'] = df['field_name'].apply(human_dates)'''

        if len(str(date)) == 10:
            try:
                date = int(date)
                human_date = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d')
                return human_date
            except:
                return date
        if len(str(date)) == 12:
            try:
                date = int(float(date))
                human_date = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d')
                return human_date
            except:
                return date
        else:
            return date
        
    def calculate_days_past(self, number_of_days):
        ''' This function will give you the date x number of days past, useful
        when calculating query dates.
        
        Input number, output is a date as a string (YYYY-MM-DD).'''

        today = datetime.now()
        num_days = timedelta(days = (number_of_days - 1))
        desired_date = today - num_days
        
        return str(desired_date).split()[0]
    
    def defang_links(self, fanged_string):
        ''' This function can be used in stream to defang returned objects that will
        present as a hyperlink within Jupyter. It will not defang domains or IPs alone.
        
        Input string, output string.'''

        clean_string = fanged_string.replace(':\\','[:]\\').replace('://','[:]//').replace('www.', 'www[.]').replace('http', 'hxxp')

        return clean_string