from api import CovidAPI
import datetime


def test():
    today = datetime.date.today()
    print("Today is {}".format(today))

    usa_data = CovidAPI().get_usa_data()
    md_data = CovidAPI().get_md_data()
    dc_data = CovidAPI().get_dc_data()
    va_data = CovidAPI().get_va_data()
    data_list = [usa_data, md_data, dc_data, va_data]

    for d in data_list:
        region = d.get('region')
        positive = d.get('positive')
        positive_increase = d.get('positive_increase')
        death = d.get('death')
        death_increase = d.get('death_increase')
    
        text1 = "As of today in {}, there have been {} total cases".format(region, positive)
        text2 = "This is an increase of {} from yesterday.".format(positive_increase)
        text3 = "As of today, there have been {} total deaths".format(death)
        text4 = "This is an increase of {} from yesterday.".format(death_increase)
        
        text_list = [text1, text2, text3, text4]
        
        for row in text_list: 
            print(row)


test()

