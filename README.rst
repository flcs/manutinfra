ManutInfra
~~~~~~~~~~
IFF - Bacharelado em Sistemas de Informação, Tópicos Avançados 1

Sistema de Manutenção e Infraestrutura
^^^^^^^

Sobre o sistema
-------
A partir do sistema, ordens de serviços de manutenção e infraestrutura do IFF podem ser criadas e gerenciadas.
O sistema foi desenvolvido utilizando Django,um dos mais utilizados e maduros frameworks web baseados em Python.
Também foi utilizada a aplicação Django Piston como ferramenta auxiliar à implementação dos princípios do SOA 
(Service-Oriented Architecture).

Os serviços disponibilizados pelo sistema são:
-------
- Lista de todas as ordens de manutenção::

	/api/ordens_manutencao
- Lista de todas as ordens de infraestrutura::

	/api/ordens_infraestrutura
- Busca de ordem de manutenção utilizando como parâmetro o ID via URL::

	/api/ordens_manutencao/{ID}
- Busca de ordem de infraestrutura utilizando como parâmetro o ID via URL::

	/api/ordens_infraestrutura/{ID}
- Lista de todas as ordens de manutenção com status "em aprovacao"::

	/api/ordens_manutencao/aprovacao
- Lista de todas as ordens de infraestrutura com status "em aprovacao"::

	/api/ordens_infraestrutura/aprovacao

- Criar Ordens de Infraestrutura (Exemplo)::

	curl -u solicitante:solicitante -H 'Content-Type:application/json' -X POST -d '{"setor": "setor", "descricao": "descricao", "equipamento": "equipamento","empresa":"empresa","solicitante":"solicitante"}' http://127.0.0.1:8000/api/ordens_infraestrutura/

- Criar Ordens de Manutenção (Exemplo)::

	curl -u solicitante:solicitante -H 'Content-Type:application/json' -X POST -d '{"setor": "setor", "descricao": "descricao", "equipamento": "equipamento","solicitante":"solicitante"}' http://127.0.0.1:8000/api/ordens_manutencao/


Acesso:
-------
`<http://localhost:8000>`_

- *Login:* solicitante
- *Senha:* solicitante

  


