from piston.handler import BaseHandler
from manutinfra.manutencao_infra.models import Ordem_Manutencao , Ordem_Infraestrutura
from piston_mini_client.failhandlers import NotFoundError
import json

class Handler_Manutencao (BaseHandler):
	allowed_methods = ('GET','POST',"DELETE","PUT")
	model = Ordem_Manutencao
	
	def read (self, request):
		ordens_manut = Ordem_Manutencao.objects.all()

		return ordens_manut
	
	def create(self, request, **kwargs):

		dados = request.data
#		dados = json.loads(raw_dados)
#		ordem = self.model.create(solicitante=dados['solicitante'],setor=dados['setor'],descricao=dados['descricao'],equipamento=dados['equipamento'])
		ordem = Ordem_Manutencao(solicitante=dados['solicitante'],setor=dados['setor'],descricao=dados['descricao'],equipamento=dados['equipamento'],criador=request.user)
		ordem.save()
		return 'Gerada ordem de numero : '+ str(ordem.id)


#		attrs = self.flatten_dict(request.POST)
		
#		solicitantej = request.POST['solicitante']
#		setorj = request.POST['setor']
#		descricaoj = request.POST['descricao']
#		equipamentoj = request.POST['equipamento']
#		ordem = Ordem_Manutencao(solicitante=attrs['solicitante'],setor=attrs['setor'],descricao=attrs#['descricao'],equipamento=attrs['equipamento'])
#		ordem = Ordem_Manutencao(solicitante=solicitantej,setor=setorj,descricao=descricaoj,equipamento=equipamentoj)
#		Ordem_Manutencao(solicitante=solicitantej,setor=setorj,descricao=descricaoj,equipamento=equipamentoj)

#			ordem.save()
            
#			return ordem


class Handler_Manutencao_ID (BaseHandler):
	allowed_methods = ('GET','POST',"DELETE","PUT")
	model = Ordem_Manutencao
	
	def read (self, request, ordem_id):
		ordens_manut = Ordem_Manutencao.objects.filter(id = ordem_id)			
		if ordens_manut.__len__() == 0:
			ordens_manut = "Nenhuma ordem encontrada"
		return ordens_manut


class Handler_Manutencao_Aprovacao (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Manutencao
	
	def read (self, request):
		ordens_manut_aprov = Ordem_Manutencao.objects.filter(status = 'em_aprovacao')
		if ordens_manut_aprov.__len__() == 0:
			ordens_manut_aprov = "Nenhuma ordem encontrada"
		return ordens_manut_aprov


class Handler_Infra (BaseHandler):
	allowed_methods = ('GET','POST',"DELETE","PUT")
	model = Ordem_Infraestrutura
	
	def read (self, request):
		ordens_infra = Ordem_Infraestrutura.objects.all()
		return ordens_infra

	def create(self, request , **kwargs):
		dados_infra = request.data
		ordem = Ordem_Infraestrutura( solicitante = dados_infra['solicitante'],setor=dados_infra['setor'],descricao=dados_infra['descricao'],empresa=dados_infra['empresa'],criador=request.user)
		ordem.save()
		return 'Gerada ordem de numero : '+ str(ordem.id)


class Handler_Infra_ID (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Infraestrutura
	
	def read (self, request, ordem_id):
		ordens_infra = Ordem_Infraestrutura.objects.filter(id = ordem_id)
		if ordens_infra.__len__() == 0:
			ordens_infra = "Nenhuma ordem encontrada"
		return ordens_infra

class Handler_Infra_Aprovacao (BaseHandler):
	allowed_methods = ('GET',)
	model = Ordem_Infraestrutura
	
	def read (self, request):
		ordens_infra_aprov = Ordem_Infraestrutura.objects.filter(status = 'em_aprovacao')
		if ordens_infra_aprov.__len__() == 0:
			ordens_infra_aprov = "Nenhuma ordem encontrada"
		return ordens_infra_aprov

