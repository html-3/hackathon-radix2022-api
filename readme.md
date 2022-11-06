# Flask API Boilerplate
Um repositório para usar como base para futuros projetos com o microframework Flask. As seguintes extensões foram implementadas.    

- [x] Flask SQLAlchemy
- [x] Flask Migrate
- [ ] Flask JWTManager
- [x] Flask Marshmallow
- [ ] Flask CORS
- [ ] Google Cloud
- [ ] Pytest

As seguintes funcionalidades estao disponiveis no projeto atual:

- [x] Tabela de usuarios (com tipos admin, mode e client)
- [x] Tabela de postagens
- [ ] Tabela de comentarios
- [x] Modelos abstratos
- [x] Validacao de usuarios
- [ ] Validacao de postagens
- [ ] Validacao de login
- [ ] Interface de requisicoes
- [ ] Validacao de comentarios

## Uso
1. Criar arquivo `.env` para configurar variaveis de ambiente locais.
2. Instalar pipenv para rodar app em ambiente virtual.
3. Inicializar pipenv com o seguinte comando.
```bash
pipenv shell
```
3. Iniciar app com o seguinte commando.
```bash
python run.py
```
4. Manipular arquivo `dd.py` para alterar conteudos iniciais do banco.

## Material de leitura
[Qovery](https://www.qovery.com/pricing)
