import utils as u
import read
import charts

def run ():
    data = read.read_csv('data.csv')
    print('WELCOME TO THE WORLD POPULATION')
    print("**** Choose an option ****")
    print("1 - Population by country")
    print("2 - Mean population by continent")
    option = input('Type option => ')
    if option == '1':
        print("Choose a country, use Capitalize letter")
        country = input('Type country => ') 

        result = u.population_by_country(data, country)

        if len(result) > 0:
            country = result[0]    
            labels, values = u.get_population(country)
            charts.generate_bar_chart(labels, values)
    elif option == '2':
        print('Choose a continent\n Asia, Africa, Europe, North America, South America, Oceania')
        continent = input('What continent do you want see => ')
        labels, values = u.get_mean_population(data, continent)
        charts.generate_pie_chart(labels, values)
    
    else:
        print('Option not found')

if __name__ == '__main__':
  run()