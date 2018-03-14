class echo:
    def __enter__(self):
        print('-------Enter----------')
        return 'Value'

    def __exit__(self, *args):
        print('-------Exit-----------')


with echo() as e:
    print(e)
    print('Code Block')
