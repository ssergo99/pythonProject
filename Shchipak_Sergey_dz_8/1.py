import re

RE_MAIL = re.compile(r'^[0-9.A-Za-z]+[@][a-z]+[.][a-z]+$')


def email_parse(argv):
    pars_result = {}
    if len(argv) == 2:
        program, email_adress = argv
        if RE_MAIL.match(email_adress):
            pars_result.setdefault('username', re.split(r'@', email_adress)[0])
            pars_result.setdefault('domain', re.split(r'@', email_adress)[1])
            print(pars_result)
        else:
            raise ValueError('Некорректный формат e-mail')
    else:
        print(f"Необходимо ввести e-mail для обработки")

        exit(1)


if __name__ == '__main__':
    import sys

    exit(email_parse(sys.argv))
