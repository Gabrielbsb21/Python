class Pessoa(object):
    pass

def set_name(pessoa, name):
    pessoa.name = name

macho = Pessoa()
set_name(macho, 'Gabriel')
print(macho.name)
