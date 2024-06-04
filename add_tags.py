# Primeiro instale as dependencias
# pip3 install datadog-api-client
# se necessario atualizar:
# python.exe -m pip install --upgrade pip
 
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi
from datadog_api_client.v1.model.host_tags import HostTags
 
# Defina os nomes dos hosts e as tagsclear
#  desejadas
hosts = ["NBARC0053", "gabriel-VirtualBox"]
tags = ["tribo:teste_linux", "team:teste_linux", "squad:teste_linux"]
 
# Configuração do cliente da API
configuracao = Configuration(
    host="https://api.us5.datadoghq.com",
    api_key={
        'apiKeyAuth': '7f4bef18899dd94bfc9a86659ccfc586',
        'appKeyAuth': '3a7b11bd18034fd815bafd5b57ca5db8eda11e53'
    }
)
 
# Função para adicionar tags a um host
def adicionar_tags_ao_host(nome_do_host, tags, instancia_api):
    corpo = HostTags(
        host=nome_do_host,
        tags=tags,
    )
    try:
        # Atualiza as tags do host especificado
        resposta = instancia_api.update_host_tags(nome_do_host, corpo)
        print(f"Tags atualizadas no host {nome_do_host}: {resposta}")
 
        # Verificação de todas as tags associadas ao host
        todas_as_tags = instancia_api.get_host_tags(nome_do_host)
        print(f"Todas as tags associadas ao host {nome_do_host}: {todas_as_tags}")
    except Exception as e:
        print(f"Erro ao atualizar tags no host {nome_do_host}: {e}")
 
# Criação da instância do cliente da API
with ApiClient(configuracao) as cliente_api:
    instancia_api = TagsApi(cliente_api)
    # Adiciona tags para cada host na lista
    for host in hosts:
        adicionar_tags_ao_host(host, tags, instancia_api)
