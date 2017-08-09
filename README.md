# Projeto de Desenvolvimento Web II

### Comandos

#### Virtualenvwrapper:
```
sudo apt install virtualenvwrapper
mkvirtualenv rango
workon rango
```

#### Dependências:
```
pip freeze
pip install Django==1.9
pip install Pillow
pip freeze > /requirements.txt
cat requirements.txt
```

#### Para instalar as dependências pelo arquivo requirements.txt:
```
pip install -r requirements.txt 
```

#### Criar link simbólico:
```
ln -s /home/alice/twd/ django 
```

#### Adicionar contribuidores no contributors.txt:
```
echo “Alice Borges” >> contributors.txt
```

#### Configurar o git:
```
git init
```
```
git remote add origin https://github.com/aliceborges/des.web.git
git pull --rebase origin master
```
##### ou:
```
git clone https://github.com/aliceborges/des.web.git
```
```
git config --global user.name "Alice"
git config --global user.email "alice@gmail.com"
git push -u origin master
```

#### Commit:
```
git status
git add .
git commit -m ""
git push -u origin master
```

#### Adicionando o Django:
```
django-admin startproject tango_with_django_project
cd tango_with_django_project
python manage.py runserver
```

### Desenvolvendo com o PyCharm:

#### Abrir o projeto
#### Fazer as devidas alterações
#### Crtl + k para commitar



