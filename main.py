import gspread
import config


if __name__ == '__main__':
    
    gc = gspread.service_account(filename=config.key_json)

    sh = gc.open(config.file_name_book)
    
    list_of_dicts = sh.sheet1.get_all_values()

    print(list_of_dicts)