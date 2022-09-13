def print_func(func, *args):
    name_func = func.__name__.replace('_', ' ')
    name_func_for_print = name_func[0].upper() + name_func[1:]
    print(f'Функция с именем "{name_func_for_print}" имеет аргумент(ы): ', end='')
    print(*args, sep=', ')

def open_browser(browser_name):
    print_func(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_func(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func(find_registration_button_on_login_page, page_url, button_text)

open_browser('Chrome')
go_to_companyname_homepage('www.google.com')
find_registration_button_on_login_page('www.google.com', 'registration')