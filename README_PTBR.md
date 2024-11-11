> [!NOTE]
> [Clique aqui para a versão em Inglês.](https://github.com/JleoDev/AFSBot/blob/main/README.md)

<h1 align="center">Advanced File Stream Bot (AFSBot)</h1>
AFSBot é uma continuação do projeto <a href='https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python'>TG-FileStreamBot</a> mais especificamente a versão em python do úsuario <a href='https://github.com/EverythingSuckz'>EverythingSuckz</a>, onde modificarei e adicionarei funções ao bot porém sua essência de criar links de streaming de arquivos será mantida.

## Como configurar

<details open="open">
	<summary><h3>Variaves de ambiente</h3></summary>

Escreva um arquivo <em>.env<em> como o exemplo abaixo:

```
API_ID=452525
API_HASH=esx576f8738x883f3sfzx83
BOT_TOKEN=55838383:yourtbottokenhere
BIN_CHANNEL=-100
```

<details>
	<summary><h4>Obrigatorias</h4></summary>
	
Para o bot funcionar ele requer pelomenos essas quatro variaveis:

- `API_ID`: É o ID da API Telagram vinculada a sua conta. Obs.: Esse ID pode ser obtido acessando <a href='https://my.telegram.org/auth'>https://my.telegram.org/auth</a>

- `API_HASH`: É o ID da API Telagram vinculada a sua conta. Obs.: Esse hash pode ser obtido acessando <a href='https://my.telegram.org/auth'>https://my.telegram.org/auth</a>

- `BOT_TOKEN`: E o token referente ao seu bot. Obs.: Esse token pode ser obtido conversando com o <a href='https://t.me/BotFather'>@BotFather</a>

- `BIN_CHANNEL`: É o ID do canal ou grupo que sera utilizado para armazenar as mensagens com arquivo que o bot receber. Obs.: Esse ID pode ser obtido encaminhado uma mensagem do canal para <a href='https://t.me/MissRose_bot'>@missrose_bot</a> e depois respondendo a mensagem com o comando /id.

> **Aviso**  
> Não se esqueça de adicionar o bot ao `BIN_CHANNEL` para o funcionamento adequado.

</details>

<details>
	<summary><h4>Opcionais</h4></summary>

- `ALLOWED_USERS`: São os IDs dos usuários do Telegram que o bot deve responder.

> **Nota**
> Deixe este campo vazio para permitir que qualquer pessoa use o bot. Obs.: Você também pode adicionar vários usuários, separando os IDs por vírgula (,).

- `HASH_LENGTH`: Este é o comprimento personalizado do hash para URLs geradas. O comprimento do hash deve ser maior que 5 e menor que 64.

- `SLEEP_THRESHOLD`: Define o limite de espera para exceções de flood wait que ocorrem globalmente na instância do bot. Solicitações que gerem exceções de flood wait abaixo desse limite serão automaticamente executadas novamente após o tempo de espera necessário. Exceções que exijam tempos de espera mais longos serão exibidas no terminal. O valor padrão é 60 segundos. Recomendo deixar este campo vazio.

- `WORKERS`: Define o número máximo de trabalhadores simultâneos para lidar com atualizações recebidas. O valor padrão é 3.

- `PORT`: Define a porta que sua aplicação web irá receber as requisições. O valor padrão é 8080.

- `WEB_SERVER_BIND_ADDRESS`: Define o endereço de ligação do servidor. O valor padrão é 0.0.0.0.

- `NO_PORT`: Pode ser `True` ou `False`. Se definido como `True`, a porta não será exibida.
> **Nota**
> Para usar essa configuração, é necessário definir a `PORT` como 80 para protocolo HTTP ou 443 para protocolo HTTPS para que os links gerados funcionem.

- `FQDN`: Um Nome de Domínio Completamente Qualificado, se presente. O padrão é `WEB_SERVER_BIND_ADDRESS`.

- `HAS_SSL`: Pode ser `True` ou `False`. Se definido como `True`, os links gerados estarão no formato HTTPS.

- `KEEP_ALIVE`: Caso deseje que o servidor se pingue automaticamente a cada `PING_INTERVAL` segundos para evitar inatividade. Útil em camadas gratuitas de PaaS. O padrão é `False`.

- `PING_INTERVAL`: O tempo em ms para que o servidor se pingue a cada vez para evitar inatividade (caso esteja em alguma PaaS). O padrão é `1200`, ou 20 minutos.

- `USE_SESSION_FILE`: Utiliza arquivos de sessão para clientes, em vez de armazenar o banco de dados sqlite do pyrogram na memória.

</details>

<details>
	<summary><h5>Suporte a múltiplos clientes</h5></summary>
	
> **Nota**  
> O que é o recurso multi-cliente e o que ele faz? <br>  
> Esse recurso compartilha as requisições da API do Telegram entre outros bots para evitar que o bot entre em "floodwait" (um tipo de limitação de taxa que o Telegram aplica no backend para evitar sobrecarga nos servidores) e para permitir que o servidor consiga lidar com mais requisições. <br>

Para ativar o multi-cliente, gere novos tokens de bot e adicione-os como variáveis de ambiente com os seguintes nomes de chave.  

`MULTI_TOKEN1`: Adicione o token do seu primeiro bot aqui.  

`MULTI_TOKEN2`: Adicione o token do seu segundo bot aqui.  

Você também pode adicionar quantos bots quiser. (O limite máximo ainda não foi testado)  
`MULTI_TOKEN3`, `MULTI_TOKEN4`, etc.

> **Aviso**  
> Não se esqueça de adicionar todos esses bots ao `BIN_CHANNEL` para o funcionamento adequado.

</details>

</details>

<details>
	<summary><h3>Local ou em uma VPS</h3></summary>

```
git clone https://github.com/JleoDev/AFSBot.git
cd AFSBot
python3 -m venv ./venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m WebStreamer
```

e para parar o bot precione, <kbd>CTRL</kbd>+<kbd>C</kbd>

</details>

## Como usar o bot

> **Aviso**  
> Antes de usar o bot, não se esqueça de adicionar todos os bots (incluindo os multi-cliente) ao `BIN_CHANNEL` como administradores.

`/start` : Para verificar se o bot está ativo.

Para obter um link de streaming instantâneo, basta encaminhar qualquer mídia para o bot e pronto, ele responde instantaneamente com um link direto para essa mensagem de mídia no Telegram.

## Contribução

Sinta-se à vontade para contribuir com este projeto se tiver mais ideias. Você pode criar uma _issue_ para informar o que deseja ou o que está modificando.

## Créditos

- [Eu](https://github.com/JleoDev) organizador do AFSBot.
- [EverythingSuckz](https://github.com/EverythingSuckz) com o [código base](https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python) para o projeto atual.
- [BlackStone](https://github.com/eyMarv) por adicionar suporte multi-cliente ao [código base](https://github.com/EverythingSuckz/TG-FileStreamBot/tree/python) para o projeto atual.
- [TheHamkerCat](https://github.com/TheHamkerCat)
- [Dan](https://github.com/delivrance) pelas bibliotecas [pyrogram](https://github.com/pyrogram/pyrogram) e [tgcrypto](https://github.com/pyrogram/tgcrypto)
- [Saurabh Kumar](https://github.com/theskumar) pela biblioteca [python-dotenv](https://github.com/theskumar/python-dotenv)
- [aio-libs](https://github.com/aio-libs) pela biblioteca [aiohttp](https://github.com/aio-libs/aiohttp)

> **Nota**  
> Também pode ser encontrada uma copia das licenças dos codigos utilizados nesse projeto na pasta licenses deste repositório.

## Licença

Copyright (C) 2024 [JleoDev](https://github.com/JleoDev) de acordo com [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html).

AFSBot é Software Livre: você pode usá-lo, estudá-lo, compartilhá-lo e melhorá-lo à sua vontade. Especificamente, você pode redistribuí-lo e/ou modificá-lo sob os termos da [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html), conforme publicada pela Free Software Foundation, na versão 3 da Licença ou (a seu critério) qualquer versão posterior.