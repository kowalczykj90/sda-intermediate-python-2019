if __name__ == '__main__':
    while True:
        text = input('Provide a number: ')
        # if text.isdigit():
        # if isinstance(int(text), int):
        try:
           input_number = int(text)
        except (ValueError, TypeError) as error:
            print('Podałeś złą liczbę')
        except KeyError:
            print('Try again')
        else:
            print(f'Podałeś mi liczbę: {input_number}')
        finally:
            print('Spróbujmy jeszcze raz')
